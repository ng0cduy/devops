```
# Create the namespace 'dev'
kubectl create namespace dev

# Deploy the pod named 'dev-nginx-pod' using image 'nginx:latest' in the 'dev' namespace
kubectl run dev-nginx-pod --image=nginx:latest --restart=Never -n dev

# Create a pod named 'httpd-pod' with a container named 'httpd-container' and resource limits
cat <<EOF | kubectl apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: httpd-pod
spec:
  containers:
  - name: httpd-container
    image: httpd:latest
    resources:
      limits:
        cpu: "500m"
        memory: "128Mi"
EOF
```