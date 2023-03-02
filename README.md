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

QUESTION 2

d) kubectl apply -f https://github.com/c0771866/ThinkOn_Assignment/blob/921cf29b3cf364205137ebcc744defdd2722a99a/hpa.yaml

Repeat above steps for container 2

QUESTION 3

The default strategy is rolling update in the container1.yaml file which would allow  rolling deployments and rollback

Question4

i) On AWS console,create a user named dev and assign to "dev" group. Assign programmatic access and obtain the arn

ii) Create a policy. Chooose EKS service. Select least privilege actions required to run this task which is to deploy and roll back - List, Read, Write as may be

iii) Create policy and attach to dev group or dev user as case may be

iv) Run aws eks update -kubeconfig --name<cllustername> --region<regionName>

v) kubectl edit configmap -n kube-system

vi) add userarn to configmap

vii) Map roles and rolebinding

viii) create the required k8s objects role and rolebinding with resources :deployment" and verbs "rollback" "undo" "rollon"

BONUS
  
Namespaces prod and staging should be used for isolation and segmentation


For autoscaling based on network latency

Assuning request counts are being scraped from your monitoring tool e.g Prometheus

then

kubectl apply -f https://github.com/c0771866/ThinkOn_Assignment/blob/3059066e1e157beaa0935639c43e6158dea20933/networklatency.yaml

Then, your HorizontalPodAutoscaler would attempt to ensure that each pod was consuming roughly 70% of its requested CPU, serving 1000 packets per second, and that all pods behind the main-route Ingress were serving a total of 5000 requests per second.

A cron job with the bellcurve.yaml for each container has been provided to autoscale between 7am and 6pm (peak 70% cpu usage) and between 6pm - 7am (off peak 30% cpu usage

Finally follow above steps for container2
