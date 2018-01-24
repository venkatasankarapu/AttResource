
# Docker file for python flask installation


FROM ubuntu:latest

RUN apt-get update
RUN apt-get install -y python python-pip wget
RUN pip install Flask

COPY simpleapp.py /src/simpleapp.py

EXPOSE 8080
CMD ["python","/src/simpleapp.py", "-p 8080"]
