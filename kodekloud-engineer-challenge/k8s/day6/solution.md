```bash
# Verify that all pods are operational
kubectl get pods

# Rollback the deployment to the previous revision
kubectl rollout undo deployment/nginx-deployment
```
