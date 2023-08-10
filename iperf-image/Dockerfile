FROM python:3.8-slim-buster

COPY pyclient.py pyclient.py

RUN apt-get update \
    && python3.8 -m pip install matplotlib \
    && apt install iperf3 -y

EXPOSE 5201

ENTRYPOINT ["/bin/bash"]

