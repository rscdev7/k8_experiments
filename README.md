# K8 experiments
![Alt -> Project Logo](./readme_data/k8.png)

This sample project aims to explore Kubernetes potential on microservices archiecture. In particular, project was shipped with a minimal 2-microservices that put forward a simple computation.

In particular, microservice 1 (or service-1 in the rest of the document) receive a GET request from client, contact microservice 2 (or service-2 in the rest of the document) in order to acquire needed information and finally answer to the client.

With the aim to build a wide versus, a *docker-compose* version is paired to the K8 one in order to highlight the differences.

# Istructions to run DockerCompose variant

1. Build docker image
>> **$** cd <HOME_REPO>/envs/0.docker_image
>> 


# Istructions to run Kubernetes variant