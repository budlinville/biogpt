# PythonLambdaDockerECR
PythonLambdaDockerECR

* Learn how to run lambda on docker container and deploy Base image on ECR and use on Lambda 


#### Commands 
```
docker build -t biogpt .
docker run -p 9000:8080 biogpt:latest
curl -XPOST "http://localhost:9000/2022-02-23/functions/function/invocations" -d '{}'
```