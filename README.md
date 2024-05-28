# K8S Things

Random things from my Kubernetes journey.

### Proxy

Run `kubectl proxy` in a terminal.

Get the Pod name:

```
> export POD_NAME=$(kubectl get pods -o go-template --template '{{range .items}}{{.metadata.name}}{{"\n"}}{{end}}')
> echo Name of the Pod: $POD_NAME
Name of the Pod: hello-world-python-deployment-6659bd6b85-9d2tm
```

Access the app:  http://localhost:8001/api/v1/namespaces/default/pods/hello-world-python-deployment-6659bd6b85-mhcms/proxy/

## Logs

- `kubectl logs [service-name]`

```
➜  terraform git:(main) kubectl get all
NAME                                                 READY   STATUS    RESTARTS   AGE
pod/hello-world-python-deployment-6659bd6b85-9d2tm   1/1     Running   0          17h
pod/hello-world-python-deployment-6659bd6b85-mhcms   1/1     Running   0          17h

NAME                                    TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
service/hello-world-python-service-v1   NodePort       10.105.122.240   <none>        9000:31103/TCP   20h
service/hello-world-python-service-v2   LoadBalancer   10.97.23.127     localhost     9001:30551/TCP   17h
service/kubernetes                      ClusterIP      10.96.0.1        <none>        443/TCP          21h

NAME                                            READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/hello-world-python-deployment   2/2     2            2           20h

NAME                                                       DESIRED   CURRENT   READY   AGE
replicaset.apps/hello-world-python-deployment-5bf69967d7   0         0         0       20h
replicaset.apps/hello-world-python-deployment-6659bd6b85   2         2         2       17h

➜  terraform git:(main) kubectl logs service/hello-world-python-service-v1
Found 2 pods, using pod/hello-world-python-deployment-6659bd6b85-9d2tm
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:6000
 * Running on http://10.1.0.38:6000
Press CTRL+C to quit
192.168.65.3 - - [27/May/2024 00:24:35] "GET / HTTP/1.1" 200 -
```

## Links

- [Learn Kubernetes Basics](https://kubernetes.io/docs/tutorials/kubernetes-basics/)
- [NodePort Service](https://medium.com/@rashmibr/kubernetes-nodeport-service-ce418b98818e)