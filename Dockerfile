FROM archlinux:latest
MAINTAINER SilentWind
WORKDIR /
EXPOSE 443
EXPOSE 80

COPY mirrorlist /etc/pacman.d/mirrorlist
COPY vcgencmd /usr/bin/vcgencmd
COPY override.yaml /home/override.yaml
COPY kvmd /home/kvmd
COPY python-gpiod /home/python-gpiod

RUN pacman -Sy && cd /home/kvmd && pacman -U * --noconfirm && pacman -S net-tools supervisor  tesseract-data-chi_sim tesseract-data-eng  --noconfirm && chmod 777 /usr/bin/vcgencmd
RUN sed -i "86c #" /usr/lib/python3.11/site-packages/kvmd/plugins/ugpio/gpio.py  && mv -f /home/override.yaml /etc/kvmd && cd /home/python-gpiod/ &&  python setup.py install
RUN pacman -S inetutils --noconfirm

COPY nginx.conf /etc/kvmd/nginx/nginx.conf
COPY supervisord.conf /home/supervisord.conf

CMD ["/usr/bin/supervisord", "-c",  "/home/supervisord.conf"]