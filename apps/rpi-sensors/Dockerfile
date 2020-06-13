FROM arm32v6/alpine


RUN apk add --update-cache \
    python3 \
    python3-dev \
    py3-pip \
    gcc \
    musl-dev \
    git


WORKDIR /app

COPY . /app

RUN python3 -m pip install -r requirements.txt
RUN git clone https://github.com/adafruit/Adafruit_Python_DHT.git
RUN cd Adafruit_Python_DHT python3 setup.py install

CMD python3 app.py

