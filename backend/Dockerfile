# We use debian as our base distro for this container.
FROM debian:jessie

# Refresh apt-get.
RUN apt-get update
RUN apt-get upgrade

# Install some utilities needed
RUN apt-get install -y curl make g++
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN sudo apt-get install build-essential libssl-dev libffi-dev python-dev
RUN sudo apt-get install -y python3-venv

#CREATE ENVIRONMENT
RUN python3 -m venv envDjango
RUN source envDjango/bin/activate

#INSTALL DJANGO AND FRIENDS
RUN pip3 install django
RUN pip3 install djangorestframework
RUN pip3 install django-cors-headers

COPY src/ /src/
WORKDIR /src

# Open up external access to port 8000.
EXPOSE  8000

# Run startup command.
CMD ["python", "/src/manage.py", "runserver"]
