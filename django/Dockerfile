FROM python:3.5
# create unpriveleged user
RUN adduser --disabled-password --gecos '' lancelot
WORKDIR /app/
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
ENTRYPOINT ["/app/docker-entrypoint.sh"]
CMD ["migrate"]
