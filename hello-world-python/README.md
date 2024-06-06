# Hello World Python

Just a hello world-level Flask app for use with Kubernetes on Docker Desktop.

- `ConfigMap`
- `Deployment`
- 2 `Services` -- one is a `NodePort`, the other is `LoadBalancer`

```
> kubectl apply -f hello-world-config.yaml
> kubectl apply -f hello-world-deployment.yaml
> kubectl apply -f hello-world-service.yaml
```

## K8s on Docker Desktop

```
# Get port details with either of these commands:
> kubectl get all
> kubectl get svc hello-world-python-service-v1
NAME                            TYPE       CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
hello-world-python-service-v1   NodePort   10.105.122.240   <none>        9000:31103/TCP   3h15m

# NodePort
> curl localhost:31103
Hello, World!

# LoadBalancer
> curl localhost:9001  # this is the LoadBalancer
Hello, World!
```

## K8s on Minikube

```
> kubectl port-forward service/hello-world-python-service-v2 9001:9001

> curl localhost:9001
Hello, World! The value of the env var FOO is K8s-FOO, and BAR is K8s-BAR
```