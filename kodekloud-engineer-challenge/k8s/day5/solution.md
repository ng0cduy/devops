```bash
# inspect the name of container:
kubectl describe pod 
# Update the deployment image to nginx:1.18
kubectl set image deployment/nginx-deployment nginx-container=nginx:1.18

# Wait for the rollout to complete
kubectl rollout status deployment/nginx-deployment

# Verify that all pods are operational
kubectl get pods
```
