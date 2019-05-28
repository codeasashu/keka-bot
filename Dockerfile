# pull official base image
FROM python:3.7-alpine

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev

WORKDIR /app

# Requirements have to be pulled and installed here, otherwise caching won't work
RUN pip install --upgrade pip

RUN pip install requests
RUN pip install beautifulsoup4

COPY . .

CMD ["/bin/ash"]