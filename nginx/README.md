```
kubectl apply -f ./run-my-nginx.yaml
kubectl get pods -l run=my-nginx -o wide
```

```
kubectl get pods -l run=my-nginx
or
kubectl get pods
```

NAME                                             READY   STATUS    RESTARTS   AGE
hello-world-python-deployment-6659bd6b85-9d2tm   1/1     Running   0          17h
hello-world-python-deployment-6659bd6b85-mhcms   1/1     Running   0          17h
my-nginx-684dd4dcd4-489rc                        1/1     Running   0          24m
my-nginx-684dd4dcd4-9h4wl                        1/1     Running   0          24m
pizza-store-deployment-98777fd7-lfnj9            1/1     Running   0          28m

➜  nginx git:(main) ✗ kubectl get pod my-nginx-684dd4dcd4-489rc -o=jsonpath='{.status.podIP}'
10.1.0.49%
