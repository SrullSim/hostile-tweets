docker build -t hostile-tweets .
docker tag mongo-app username/hostile-tweets:v1
docker push username/hostile-tweets:v1

 oc delete all --all -n  <namespace>

 oc new-app mongodb/mongodb-community-server:latest --name mongodb
 oc new-app --name hostile-tweets --docker-image=docker.io/<username>/hostile-tweets:v1 -e HOST=mongodb

 oc expose service/hostile-tweets
 oc get route -l app=hostile-tweets