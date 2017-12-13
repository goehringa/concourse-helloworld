## helloworld HTTP server
FLask Http server accepts three endpoints that return plain-text
* GET / responds with "hello world"
* GET /hello responds with "hello"
* GET /world respond with "world

Each endpoint also acceps the following query parameters
* uppercase, which if true returns the string but capitalized, e.g. HELLO WORLD
* reversed, whichif true returns the reverse of the string, e.g. dlrow olleh

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

## Flask Container
To build the docker image run
`docker build -t helloworld .`

Now, you can run the container with 
`docker run -p 8080:8080 helloworld`
You can now reach your server at http://0.0.0.0:8080/

## Continuous Integration
The docker-compose.yml file spins up three containers
* Concourse-db for storing pipeline data and build logs
* Concourse-web for the Web UI, API, and pipeline scheduling
* Concourse-worker for running containers

Create a credentials.yml file to store your docker hub credentials
Do not check this into git as it has your credentials
```
docker-hub-email: EMAIL
docker-hub-username: USERNAME
docker-hub-password: PASSWORD
docker-hub-image-helloworld: USERNAME/docker-image
```

To update your pipeline run
```
fly -t ci login -c http://your_concourse_url
fly -t ci set-pipeline -p helloworld -c concourse.yml --load-vars-from credentials.yml
```
