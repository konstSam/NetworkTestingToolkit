FROM python:3.8-slim-buster

COPY pyookla.py pyookla.py

RUN apt-get update \
    && apt-get install curl -y \
    && curl -s https://install.speedtest.net/app/cli/install.deb.sh | bash \
    && apt-get install ca-certificates -y \
    && apt-get install -y speedtest \
    && python3.8 -m pip install matplotlib 

ENTRYPOINT ["/bin/bash"]

