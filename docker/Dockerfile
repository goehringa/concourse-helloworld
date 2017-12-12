FROM centos

RUN yum -y update; yum clean all
RUN yum -y install epel-release; yum clean all
RUN yum -y install python-pip; yum clean all

WORKDIR /data

COPY requirements.txt /data
RUN pip install --trusted-host pypi.python.org -r requirements.txt

COPY helloworld.py /data

EXPOSE 8080

CMD ["python", "helloworld.py"]
