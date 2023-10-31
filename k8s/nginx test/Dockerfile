FROM nginx:latest

COPY ./proxy/default.conf /etc/nginx/conf.d/default.conf

COPY k8s/nginx\ test/target /usr/share/nginx/html/
