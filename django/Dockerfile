FROM haakenlid/opencv:3.6
MAINTAINER haakenlid

# create user to run app
RUN groupadd --gid 1000 django \
  && useradd --uid 1000 --gid 1000 --shell /bin/bash --create-home django

# install ghostscript for pdf operations
RUN apt-get update && apt-get install -y \
  ghostscript 

# install python dependencies for django
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

# install jupyter notebook with vim key bindings
COPY install-jupyter.sh /app/install-jupyter.sh
RUN /app/install-jupyter.sh

WORKDIR /app/
ENTRYPOINT ["/app/docker-entrypoint.sh"]
