FROM pytorchlightning/pytorch_lightning:base-cuda-py3.6-torch1.8


WORKDIR /root

COPY ./src /root/src

WORKDIR /root/src
RUN pip install -r requirements.txt

