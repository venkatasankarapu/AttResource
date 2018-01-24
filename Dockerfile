
# Docker file for python flask installation


FROM ubuntu:latest

RUN apt-get update
RUN apt-get install -y python python-pip wget
RUN pip install Flask

COPY AttResource.py /src/AttResource.py

EXPOSE 8080
CMD ["python","/src/AttResource.py", "-p 8080"]
