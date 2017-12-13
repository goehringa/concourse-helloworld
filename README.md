## helloworld HTTP server
Flask HTTP server accepts three endpoints that return plain-text responses
```
GET / responds with "hello world"
GET /hello responds with "hello"
GET /world responds with "world
```

Each endpoint also accepts the following query parameters
* uppercase, which if true returns the string but capitalized, e.g. HELLO WORLD
* reversed, which if true returns the reverse of the string, e.g. dlrow olleh

To run this server locally:
```
cd docker
pip install requirements.txt
python helloworld.py
```

## helloworld HTTP server tests
Tests are in docker/helloworld_tests.py
The test cases can be run with
```
cd docker
python helloworld_tests.py
```

## Build docker image
To build the docker image run
```
cd docker
docker build -t helloworld .
```

Now, you can run the container with 
`docker run -p 8080:8080 helloworld`

You can now reach your container at http://localhost:8080

## Upload image to docker hub
(https://hub.docker.com/)

With docker running, log into docker hub `docker login`

Publish the image `docker push username/helloworld`

You can now pull your docker image and run the container on any machine
that has docker installed


## Dgoss Container Tests
(https://github.com/aelsabbahy/goss/tree/master/extras/dgoss)

Dgoss is used to run the container tests in `docker/goss.yaml`

To run the container tests:
```
cd docker
dgoss run -p 8080:8080 username/helloworld
```

## Concourse Continuous Integration
(https://concourse.ci)

The docker-compose.yml file spins up three containers
* Concourse-db for storing pipeline data and build logs
* Concourse-web for the Web UI, API, and pipeline scheduling
* Concourse-worker for running containers

Before you can run docker-compose generate the necessary keys and add them to your .gitignore file
```
mkdir -p keys/web keys/worker

ssh-keygen -t rsa -f ./keys/web/tsa_host_key -N ''
ssh-keygen -t rsa -f ./keys/web/session_signing_key -N ''

ssh-keygen -t rsa -f ./keys/worker/worker_key -N ''

cp ./keys/worker/worker_key.pub ./keys/web/authorized_worker_keys
cp ./keys/web/tsa_host_key.pub ./keys/worker
```

Set CONCOURSE_EXTERNAL_URL in docker-compose.yml to the external IP of your concourse node

For example: `export CONCOURSE_EXTERNAL_URL=http://192.168.99.100:8080`

Now, you can run `docker-compose up`

You should be able to reach the concourse UI at your CONCOURSE_EXTERNAL_URL
The default credentials in docker-compose.yml are:
```
username: concourse
password: changeme
```

Create a credentials.yml file to store your docker hub credentials.

The github-token is necessary to for concourse to send status updates to your repository.

Add credentials.yml to your .gitignore file

```
docker-hub-email: EMAIL
docker-hub-username: USERNAME
docker-hub-password: PASSWORD
docker-hub-image-helloworld: USERNAME/docker-image
github-token: TOKEN
```

To deploy your pipeline run
```
fly -t ci login -c http://your_concourse_url
fly -t ci set-pipeline -p helloworld -c concourse.yml --load-vars-from credentials.yml
```
This will push your pipeline defined in concourse.yml to concourse

Your pipeline will:
1. Trigger when a push is made to the master branch of your repository
2. Fetch the code from your github repository
3. Run the tests for the flask HTTP server
4. Build a docker image and push it to dockerhub
5. Run dgoss container tests on your image
6. Push a build status to github, which you can see under commits
