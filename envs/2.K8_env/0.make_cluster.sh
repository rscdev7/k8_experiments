minikube start --driver=docker --nodes=2 --cpus=2 --memory=4g --disk-size=10g -p k8samp
minikube addons enable ingress
kubectl create namespace k8samp
minikube profile k8samp
