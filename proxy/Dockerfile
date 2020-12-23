FROM nginxinc/nginx-unprivileged:latest

USER root

COPY ./default.conf /etc/nginx/conf.d/default.conf
COPY ./uswgi_params /etc/nginx/uswgi_params

RUN mkdir -p /vol/static
RUN chmod 755 /vol/static

USER nginx
