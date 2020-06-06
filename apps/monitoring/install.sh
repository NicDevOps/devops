#!/bin/bash

set -x

sudo cp ./files/nodeexporter.service /etc/systemd/system/nodeexporter.service


sudo systemctl daemon-reload
sudo systemctl enable nodeexporter
sudo systemctl start nodeexporter

