FROM haakenlid/opencv
RUN groupadd --gid 1000 django \
  && useradd --uid 1000 --gid 1000 --shell /bin/bash --create-home django
RUN apt-get update && apt-get install -y \
  ghostscript
WORKDIR /app/
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY install-jupyter.sh /app/install-jupyter.sh
RUN /app/install-jupyter.sh
RUN pip install faker

ENTRYPOINT ["/app/docker-entrypoint.sh"]
