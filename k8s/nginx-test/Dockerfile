FROM nginx:latest

COPY ./proxy/default.conf /etc/nginx/conf.d/default.conf

RUN mkdir /usr/share/nginx/html/statics

COPY ./statics/ /usr/share/nginx/html/statics

COPY . .

RUN chmod +x command.sh