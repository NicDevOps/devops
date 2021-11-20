docker build -t localhost:5000/hello-world .

docker run --rm -it localhost:5000/hello-world

docker images

kubectl config get-contexts

kubectl get nodes

kubectl apply -f pod.yaml

kubectl get pods

kubectl describe pod hello-world

kubectl delete pod hello-world

docker run -d -p 5000:5000 --restart=always --name registry registry:2

docker ps

docker push localhost:5000/hello-world

kubectl apply -f pod.yaml

kubectl get pod

PYTHONUNBUFFERED=1

python3 -u app.py