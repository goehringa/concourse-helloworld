# helloworld HTTP server
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

# helloworld HTTP server tests
Tests are in docker/helloworld_tests.py
The test cases can be run with
```
cd docker
python helloworld_tests.py
```

# Flask Container
To build the docker image run
`docker build -t helloworld .`

Now, you can run the container with 
`docker run -p 8080:8080 helloworld`
You can now reach your server at http://0.0.0.0:8080/

