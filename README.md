# ThinkOn_Assignment
TakeHomeSsignment
Kubernetes Deployment
Introduction
This repository contains a Kubernetes deployment for a sample application. The deployment is managed using Kubernetes manifests, which are YAML files that define the desired state of the deployment.

Prerequisites

Before deploying this application, you will need the following:

A Kubernetes cluster
kubectl command-line tool
Docker installed on your local machine (if you want to build and push your own Docker images)


Deployment

Deploy the Metrics Server
Deploy the Metrics Server with the following command:

kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml

kubectl get deployment metrics-server -n kube-system

kubectl apply -f https://github.com/c0771866/ThinkOn_Assignment/blob/1018659b5da80d3b9a2a0c52113c883b6cbe567c/Container1.yaml


Repeat above steps for container 2

Question4
IAM controls should include creating the required necessary role binding and roles in the aws eks config map in the kubesystem namespace

add userarn to configmap

Map roles and rolebinding

create the require role and rolebinding object


Namespaces prod and staging should be used for isolation and segmentation


For autoscaling based on network latency











Then, your HorizontalPodAutoscaler would attempt to ensure that each pod was consuming roughly 50% of its requested CPU, serving 1000 packets per second, and that all pods behind the main-route Ingress were serving a total of 10000 requests per second.
