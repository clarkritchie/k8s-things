# Hello World Python

- Just a hello world-level Flask app
- A K8s deployment
- 2 K8s services -- one is a `NodePort`, the other is `LoadBalancer`

```
kubrctl apply -f deployment.yaml
kubrctl apply -f service.yaml 
kubrctl get all
curl localhost:9001  # this is the LoadBalancer
```
