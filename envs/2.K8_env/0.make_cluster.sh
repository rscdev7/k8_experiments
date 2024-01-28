minikube start --driver=docker --container-runtime docker --gpus all --nodes=2 --cpus=2 --memory=4g --disk-size=10g -p k8samp
kubectl create namespace k8samp
minikube profile k8samp
