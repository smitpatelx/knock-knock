FROM python:3.8.7-alpine3.12

ENV PATH="/scripts:${PATH}"

COPY ./requirements.txt ./
RUN apk add --update --no-cache postgresql-client jpeg-dev
RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev
RUN pip install requests
RUN pip install -r ./requirements.txt
RUN apk del .tmp

RUN mkdir /knockknock
COPY . /knockknock
WORKDIR /knockknock

RUN adduser -D knock
RUN chown knock:knock -R ./*
RUN chmod +x ./scripts/*
RUN chown -R knock:knock ./scripts

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static

RUN chown -R knock:knock /vol
RUN chmod -R 755 /vol/web
# RUN chmod -R 755 /usr/local/bin/uwsgi
USER knock

CMD ["scripts/entrypoint.sh"]