#FROM ubuntu:14.04
FROM python:3-onbuild
MAINTAINER Carlos Navarro cnavarro@paradigmadigital.com
WORKDIR /usr/src/app
CMD ["python3", "topic_service.py", "2712"]
EXPOSE 2712
