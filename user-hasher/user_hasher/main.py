import hashlib
import logging
import os
from typing import List
import pyjokes
import time
from fastapi import FastAPI, Request, Response, Header, HTTPException, Depends

# Prometheus!  I've never used it, but I have used ELK and DataDog
from aioprometheus import REGISTRY, Counter, Summary, render, MetricsMiddleware
from aioprometheus.service import Service

# *****************************************************************************
# It's not clear from the Prometheus docs if you register a Prometheus server
# one time only (using the prometheus_client lib) and it just "magically works" thereafter
# or if you have to push to it regularly, which seems odd and old-school
#
# TODO add prometheus_client to requirements.txt
#
# Commenting this out for the moment so that it works in Docker Compose on localhost!
#
# from prometheus_client import CollectorRegistry, Gauge, push_to_gateway
# registry = CollectorRegistry()
# PROMETHEUS_SERVER = os.environ.get("PROMETHEUS_SERVER", "localhost")
# PROMETHEUS_PORT = os.environ.get("PROMETHEUS_SERVER", "9091")
# prometheus_server = f'{PROMETHEUS_SERVER}:{PROMETHEUS_PORT}'
# push_to_gateway(f'{PROMETHEUS_SERVER}:{PROMETHEUS_PORT}', job='TODO', registry=registry)
# *****************************************************************************

# Setup logging
logger = logging.getLogger("uvicorn.error")

# *****************************************************************************
# When running on K8S, we'd need to add kubernetes to requirements.txt and
# do something like this -- ideally this is in some sort of optional library
#
# Commenting this out for the moment so that it works in Docker Compose on localhost!
#
# from kubernetes import client, config
# config.load_incluster_config()
# v1 = client.CoreV1Api()

pod_ip = "abc.def.ghi.jkl"
# try:
#     pod_ip = v1.read_namespaced_pod(pod_name, namespace).status.pod_ip
# except Exception as e:
#     logger.fatal("Error getting pod IP:", str(e))

node_ip = "www.xxx.yyy.zzz"
# try:
#     node_name = v1.read_namespaced_pod(pod_name, namespace).spec.node_name
#     node = v1.read_node(node_name)
#     for address in node.status.addresses:
#         if address.type == "InternalIP":
#             node_ip = address.address
#             break
#     print("Node IP:", node_ip)
# except Exception as e:
#     logger.fatal("Error getting node IP:", str(e))
# *****************************************************************************

# Instantiate the app
app = FastAPI()

# Load and log APP_VERSION
APP_VERSION = os.environ.get("APP_VERSION", "dev")
logger.info(f"APP_VERSION={APP_VERSION}")


# TODO it's not clear if metadata like this should be a "label" in Prometheus
def get_request_metadata():
    return {"version": APP_VERSION, "pod_ip": pod_ip, "node_ip": node_ip}


# setup metrics collection
service = Service()

# Request time
REQUEST_TIME = Summary(
    "request_processing_seconds",
    "Time spent processing request",
    const_labels=get_request_metadata(),
)
app.state.request_time = REQUEST_TIME

# Total requests (cumulative)
REQUESTS = Counter(
    "request_total", "Total number of requests", const_labels=get_request_metadata()
)
app.state.events_counter = REQUESTS

# User hashes generated (cumulative)
USER_HASHES = Counter(
    "user_hashes_total",
    "Total number of user hashes created",
    const_labels=get_request_metadata(),
)
app.state.hashes_counter = USER_HASHES


# middlware function to track request time
@app.middleware("http")
async def track_request_duration(request, call_next):
    start_time = time.time()
    response = await call_next(request)
    total_duration = time.time() - start_time
    logger.debug(f"total duration of request {total_duration}")
    REQUEST_TIME.observe({"path": request.url.path}, total_duration)
    return response


# TODO ask about this, as it appears to provide a status_codes_counter, which is built into aioprometheus?
app.add_middleware(MetricsMiddleware)


@app.get("/version")
async def version():
    # TODO do we care about metrics on this route?
    return {"version": APP_VERSION}


@app.get("/user_hash")
async def user_hash(request: Request, user_id: str):
    # increment the route metric counters
    request.app.state.hashes_counter.inc({"type": "user_hash"})
    request.app.state.events_counter.inc({"path": request.scope["path"]})

    # TODO remove this, for demonstration purposes this can return other error codes
    # to prove the counter works
    if user_id == "clark_really_wants_this_job":
        raise HTTPException(status_code=418, detail="you are totes a teapot")

    return hashlib.sha1(
        (user_id + os.environ.get("USER_SALT", "")).encode()
    ).hexdigest()


# TODO ask about Prometheus here, the formatting seems weird but maybe this is what the backend expects
# TODO does this go to the user or to a Prometheus server?  Is there config for that?  See comments above
@app.get("/metrics")
async def handle_metrics(
    request: Request,
    accept: List[str] = Header(None),
) -> Response:
    content, http_headers = render(REGISTRY, accept)
    return Response(content=content, media_type=http_headers["Content-Type"])


@app.get("/joke")
async def get_random_joke():
    cool_envs = ["dev", "localhost"]
    if os.getenv("APP_VERSION").casefold() in cool_envs:
        joke = pyjokes.get_joke()
        return {"joke": joke}
    else:
        raise HTTPException(status_code=404)
