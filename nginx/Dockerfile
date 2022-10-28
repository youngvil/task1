#---------------------------------------------------------------------------
# Dockefile to build Docker Image of Apache WebServer running on Ubuntu
#
# Made by Denis Astahov ADV-IT  13-March-2019
#---------------------------------------------------------------------------

FROM nginx:latest
RUN rm /etc/nginx/conf.d/*
COPY nginx.conf /etc/nginx/conf.d/
