# Hello World Python

- Just a hello world-level Flask app
- A K8s deployment
- 2 K8s services -- one is a `NodePort`, the other is `LoadBalancer`

```
> kubectl apply -f deployment.yaml
> kubectl apply -f service.yaml

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
