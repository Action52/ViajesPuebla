# We use debian as our base distro for this container.
FROM debian:jessie
MAINTAINER Luis Alfredo Leon
# Refresh apt-get.
RUN apt-get update

# Install some utilities needed
RUN apt-get install -y curl make g++
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN apt-get install -y build-essential libssl-dev libffi-dev python-dev
RUN apt-get install -y python3-venv
RUN apt-get install -y postgresql
RUN apt-get install -y python3-dev libpq-dev
RUN apt-get install -y git

#INSTALL DJANGO AND FRIENDS
RUN pip3 install django
RUN pip3 install djangorestframework
RUN pip3 install django-cors-headers
RUN pip3 install django-rest-auth
RUN pip3 install psycopg2

# Open up external access to port 8000.
EXPOSE  80

RUN git clone https://github.com/Action52/ViajesPuebla.git
WORKDIR ViajesPuebla/backend/viajespuebla


ENTRYPOINT python3 manage.py runserver 80 -D FOREGROUND
