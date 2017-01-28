FROM nginx:1.11
# In the nginx docker image `sites-enabled` is not used
# Instead site specific config are placed in `conf.d`
# Remove default config files
RUN rm /etc/nginx/conf.d/*
COPY ./conf.d/* /etc/nginx/conf.d/
