FROM nginx:latest

COPY ./proxy/default.conf /etc/nginx/conf.d/default.conf

COPY ./statics/ /usr/share/nginx/html/

USER root 

RUN chmod +x /usr/share/nginx/html/statics/signaler.sh 

USER nginx