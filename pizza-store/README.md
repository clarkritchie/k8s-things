Deploys the [pizza store app](https://github.com/clarkritchie/pizza-store-app/).

```
> kubrctl apply -f pizza-store.yaml

> kubectl expose deployment pizza-store-deployment --type=LoadBalancer --name=pizza-store-service

> kubectl describe services pizza-store-service

...

> curl localhost
{"message":"more pizza"}
```