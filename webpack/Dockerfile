FROM node:7.4
COPY package.json /app/package.json
RUN npm install
RUN mkdir /var/build/ && chown node:node /var/build/
USER node
WORKDIR /app
ENTRYPOINT ["./docker-entrypoint.sh"]
