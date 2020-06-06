#!/bin/bash

curl -SL https://github.com/prometheus/node_exporter/releases/download/v1.0.0/node_exporter-1.0.0.linux-armv6.tar.gz > node_exporter.tar.gz

sudo tar -xvf node_exporter.tar.gz -C /usr/local/bin/ --strip-components=1

