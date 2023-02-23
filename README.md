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

