FROM centos

RUN yum clean all
RUN yum update -y
RUN yum install -y epel-release
RUN yum install -y python-pip

WORKDIR /data

RUN useradd -ms /bin/bash flask

COPY requirements.txt /data
RUN pip install --trusted-host pypi.python.org -r requirements.txt

COPY helloworld.py /data

RUN chown -R flask:flask /data

EXPOSE 8080

USER node
CMD ["python", "helloworld.py"]
