# Helm Charts

I thought that this tutorial was pretty good:

- [Helm Charts Tutorial: A Simple Guide for Beginners](https://devopscube.com/create-helm-chart/)


```
cd foobar-chart
helm lint
helm template .
```

```
cd ..
helm install foobar-v0 foobar-chart
helm list

helm upgrade foobar-v0 foobar-chart

helm delete foobar-v0
```