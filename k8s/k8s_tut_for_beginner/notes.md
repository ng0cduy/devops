# Notes for k8s
## Main k8s components
### Pod:
![alt text](img/img/pod.png)

* Each pod gets 1 IP addresss
* New IP address on re-creation, when 1 pod is dead and crashed, another pod will be re-created and replace, new IP addressed will be replaced in that

### Service
* a static(img/permanent) IP is attached to each pod. my-app will have its own service and db will have it own service, pod and service are not connect, -> if the pod died, the service still stay alive, so dont have to change the end point
![alt text](img/services.png)

### Ingress
* Traffic will go through into ingress and then forwarding to the service
![alt text](img/services.png)

#### Step for change db name
![alt text](img/step_to_change_db.png)

### Config map
![alt text](img/config_map.png)
* Do not need to rebuilt the image
* Do not put credentials into config map. Save it in ```secret```

### Secret:
![alt text](img/secret.png)

![secret_example ](img/secret_1.png)

### Data storage
#### Volume
![Volume example](img/volume1.png)

#### Replica
* Avoid application downtime and db downtime
![alt text](img/replica.png)
* Service also represent as a load balancer, the service will catch the request and forward it to whichever part is list busy
* Do not need to create the replica, only need to define a blueprint (img/deployments)
* Defind replicas, if 1 application is down, the service will forward to another pod, then user can still continue to use
* DB cannot be replicated via Deployment because data has states
* Need to have a mechanism to avoid the inconsistence of the data, making the databases is synchronize ```StatefulSet```

* ```Deployment for stateless app```
* ```statefulset for statefull apps or databases```
* Deploying statefulset is not easy
* DB are often hosted outside of k8s cluster

### Summarize
![alt text](img/main_k8s_parts.png)
![alt text](img/summarize.png)

## K8s architecture
![alt text](img/kubelet.png)
### Kubelet
* Kubelet interacts with both - the container and node
* Kubelet starts the pod with a container inside
* 1 node containes: ```pods, container runtime and kubelet```
### Kube proxy
* forwards the requests
* E.g: my-app in node 1 will send the request to db in node1, with the help of kube proxy, without sending the request to db in node2
### Container runtime

### Master nodes
![alt text](img/question_related_to_master_node.png)

* There will be 4 processes run on master node

#### API server
![alt text](img/api_server.png)
* like a cluster gateway
* acts as a gatekeeper for authentication

![alt text](img/api_servers_1.png)

* Good since there are just 1 entry point enter to the cluster

### Scheduler
* have intelligence to assign which pod into the node
![alt text](img/Scheduler.png)

![alt text](img/Scheduler1.png)
* Scheduler just decide which node will be assign a pod, but the ```kubelet``` responsible for create the pod into that node

### Controller manager
* when pods die on any nodes, detect it and reschedule those pods ASAP
* It can detects cluster state changes
![alt text](img/Controller_manager.png)

### etcd
* a key-value store
* can be considered as a cluster brain
* Cluster changes get stores in the key value store. E.g: if a pod dies means that the cluster changed, then the etcd will get store in the key value
![alt text](img/etcd.png)

* ``` application data not stored in etcd ```
* ``` etcd only store cluster states change in order to make the master node able to communicate with slave nodes```

### practical example
![alt text](img/k8s_arch_example.png)
* API server are load balanced
* Distributed storage across all master nodes

### Example set up
![alt text](img/k8s_arch_setup1.png)

## Minikube and kubectl setup
### Production Cluster Setup
![alt text](img/Production-Cluster-Setup.png)

### Minukube
1 node cluster contain both master and worker processes
![alt text](img/minikube.png)
* Create Virtual Box on your machine
* Node runs in that Virtual Box
* 1 Node K8s cluster
* Use for testing purpose

### Kubectl
![alt text](img/kubectl.png)

Notes
![alt text](img/kubectl1.png)

## Baisc kubectl commands
![alt text](img/kubectl-command-1.png)

```
kubectl get nodes
kubectl get pod
kubectl get services
kubectl create
kubectl create deployment NAME --image=image [--dry-run] [options] : create a pod
kubectl get deployment
```

![alt text](img/create-a-pod.png)

![alt text](img/layer-of-abstraction.png)

* Everything below Deployment is handled by K8s



* Edit the yaml file, then the old deployment will be terminated, the new deployment will be created
```kubectl edit deployment nginx-depl```
![alt text](img/edit-a-deployment.png)
* Deployment status after edit
![alt text](img/edit-a-deployment-status.png)

* Check logs of a pod
```kubectl logs mongo-depl-85ffbc9879-6rfdp```
![alt text](img/kubectl-get-logs.png)

* Describe a pod
```kubectl describe pod mongo-depl-85ffbc9879-6rfdp```
![alt text](img/kubectl-describe-pod.png)

* Debug a pod using ```exec```
```kubectl exec -it mongo-depl-85ffbc9879-6rfdp -- /bin/bash```
![alt text](img/kubectl-exec.png)

* Delete a deployment
```kubectl delete deployment mongo-depl```
![alt text](img/kubectl-delete-deployment.png)

* Apply ks8 cluster in a yaml file
```kubectl apply -f [filename]```

* Summarize commands:
![alt text](img/kubectl-commands-summarize.png)
![alt text](img/kubectl-commands-summarize-1.png)

## YAML config file in k8s
![alt text](img/config_file_1.png)
* Attributes "spec" are specific to each kind

* 3rd part is status but it is auto generated by k8s
* Compare between Desire state and Actual State
* ```Etcd``` holds the current status of any K8s components

### Template in config file
* Has its own meta-data and spec sections (img/config in config)
![alt text](img/template_example.png)

### Connecting components (img/Labels and Selectors and Ports)
![alt text](img/labels_selectors.png)
* First ```label``` in ```deployment``` is used by ```service```
* ```label``` in ```selector``` is used by ```pod```
```
Service selector → matches Pod labels
Deployment selector → matches Pod template labels
So the Service talks directly to Pods, and the Deployment ensures those Pods exist and have the right labels.
```
### Demo
![alt text](img/demo_config_yaml.png)
![alt text](img/demo_config_yaml-1.png)
* Check if service has correct endpoint or not
![alt text](img/demo_config_yaml-2.png)
* service has the correct endpoint
![alt text](img/demo_config_yaml-3.png)
* Check status
![alt text](img/demo_config_yaml-4.png)

## Demo Project: MongoDB and MongoExpress
![alt text](overview.png)
![alt text](overview1.png)
![alt text](overview2.png)
* Create secrets
![alt text](create_secret.png)
* Secret notes:
![alt text](create_secret_notes.png)
* Create secrets in base64:
![alt text](create_secret_notes_1.png)

* Deployment and Service can be in 1 file, since they belong together
* Using ```---``` in a yaml file to separate between each yaml file

* Service and pod have same IP
![alt text](project1_1.png)

### Create mongo express deployment - service
* Overview
![alt text](mongo-express-1.png)
* Create a config Map
![alt text](config_map.png)