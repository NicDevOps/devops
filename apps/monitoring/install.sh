#!/bin/bash

set -x

ARCH=$(uname -m)

if [ $ARCH = "x86_64" ];
then
  curl -SL https://github.com/prometheus/node_exporter/releases/download/v1.0.0/node_exporter-1.0.0.linux-amd64.tar.gz > node_exporter.tar.gz
else
  curl -SL https://github.com/prometheus/node_exporter/releases/download/v1.0.0/node_exporter-1.0.0.linux-armv6.tar.gz > node_exporter.tar.gz
fi

sudo tar -xvf node_exporter.tar.gz -C /usr/local/bin/ --strip-components=1

sudo chmod +x /usr/local/bin/node_exporter

sudo cp ./files/nodeexporter.service /etc/systemd/system/nodeexporter.service

sudo systemctl daemon-reload
sudo systemctl enable nodeexporter
sudo systemctl start nodeexporter

