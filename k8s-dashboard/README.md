# Kubernetes Dashboard

- [Getting Started: How to set up Kubernetes dashboard](https://kb.leaseweb.com/products/kubernetes/getting-started-with-kubernetes/getting-started-how-to-set-up-kubernetes-dashboard)

### Install helm, kubernetes-dashboard

```
> brew install helm
> helm repo add kubernetes-dashboard https://kubernetes.github.io/dashboard/
> helm upgrade --install kubernetes-dashboard kubernetes-dashboard/kubernetes-dashboard --create-namespace --namespace kubernetes-dashboard
```

### Create service account, get token

```
~> kubectl create serviceaccount kubernetes-dashboard -n kubernetes-dashboard~
~> kubectl create token kubernetes-dashboard -n kubernetes-dashboard~

> >kubectl apply -f dashboard-serviceaccount.yaml
> kubectl create token admin-user -n kubernetes-dashboard

```

```
kubectl -n kubernetes-dashboard port-forward svc/kubernetes-dashboard-kong-proxy 8443:443
```