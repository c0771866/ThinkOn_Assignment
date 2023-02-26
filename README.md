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

Deploy the Metrics Server with the following command:

kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml

kubectl get deployment metrics-server -n kube-system

Deploy mysql database

  
PROCEDURE

a) docker build -t user-image .

b) docker push <docker-hub-registry>/user-image:1

c) kubectl apply -f https://github.com/c0771866/ThinkOn_Assignment/blob/ad1ac61740cb3d2fc3cc339c37f60a0befda3176/container1.yaml

Deploy horizontal port operator

d) kubectl apply -f 

Repeat above steps for container 2

Question4
IAM controls should include creating the required necessary role binding and roles in the aws eks config map in the kubesystem namespace

add userarn to configmap

Map roles and rolebinding

create the require role and rolebinding object


Namespaces prod and staging should be used for isolation and segmentation


For autoscaling based on network latency

Assuning request counts are being scraped from your monitoring tool e.g Prometheus

then

kubectl apply -f https://github.com/c0771866/ThinkOn_Assignment/blob/3059066e1e157beaa0935639c43e6158dea20933/networklatency.yaml

Then, your HorizontalPodAutoscaler would attempt to ensure that each pod was consuming roughly 70% of its requested CPU, serving 1000 packets per second, and that all pods behind the main-route Ingress were serving a total of 5000 requests per second.
