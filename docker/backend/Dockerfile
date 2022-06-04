FROM python:3.10.4

#ENV PYTHONDONTWRITEBYTECODE 1
#ENV PYTHONUNBUFFERED 1
ENV TZ=UTC

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update
RUN apt-get install -y gcc g++ cmake clang python3-dev python-dev python3-pip nano \
    bpython3 postgresql libgmp10-dev build-essential libssl-dev libffi-dev ca-certificates

WORKDIR /app/

RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install setuptools cython
COPY ../requirements.txt /app/requirements.txt

RUN python3 -m pip install -r /app/requirements.txt
# RUN python3 -m pip install pgcli

USER root
EXPOSE 8080 8000
