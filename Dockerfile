FROM alpine:latest

LABEL author="KireevI.I."
LABEL version="v0.6"
LABEL paltform="web"

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apk add --no-cache \ 
    bash \
    python3 \ 
    py3-pip \
    chromium \
    chromium-chromedriver 

WORKDIR /usr/src/pokeservice

COPY ./requirements.txt /usr/src/pokeservice/requirements.txt
RUN pip install -r /usr/src/pokeservice/requirements.txt

COPY . /usr/src/pokeservice/

# Set up the environment for Selenium
ENV CHROME_BIN=/usr/bin/chromium-browser
ENV CHROME_DRIVER=/usr/bin/chromedriver

COPY ./startup_script.sh /usr/src/pokeservice/startup.sh
RUN chmod +x /usr/src/pokeservice/startup_script.sh

CMD ["/usr/src/pokeservice/startup_script.sh"]