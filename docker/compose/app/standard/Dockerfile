FROM alpine:3.9

COPY ./supervisor /etc/supervisor
COPY ./supervisor.sh /supervisor.sh
COPY ./entrypoint.sh /entrypoint.sh
COPY ./app /app

RUN echo 'http://mirrors.aliyun.com/alpine/v3.9/main/' > /etc/apk/repositories
RUN echo 'http://mirrors.aliyun.com/alpine/v3.9/community/' >> /etc/apk/repositories

RUN apk add --update supervisor
RUN sed -i 's/\r//' /entrypoint.sh
RUN sed -i 's/\r//' /supervisor.sh

RUN chmod +x /entrypoint.sh
RUN chmod +x /supervisor.sh

WORKDIR /app

ENTRYPOINT ["/entrypoint.sh"]
