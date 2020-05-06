#!/bin/bash
# 
# Install and run Freqtrade
#
# Step 1 : Download
#
# git clone https://github.com/freqtrade/freqtrade.git
#
# Step 2 : Run script setup.sh
#
#
# cd freqtrade
# ./setup.sh --install
#
# Step 3 : Install necessary dependencies
#
# sudo apt-get update
# sudo apt-get install build-essential git
#
# Step 4 : Common
#
# sudo ./build_helpers/install_ta-lib.sh
#
# Step 5 : Setup virtual environment
#
# python3 -m venv .env
# source .env/bin/activate
#
# Step 6 : install python dependencies
#
# python3 -m pip install --upgrade pip
# python3 -m pip install -e .
#
# Step 7 : Initialize the user_directory
#
# freqtrade create-userdir --userdir user_data/
#
# Step 8 : Create a new configuration file
# 
# freqtrade new-config --config config.json
# 
# Step 9 : Setup pair list for download historical data
#
# cp -a ~/backup/pairs.json ~/freqtrade/user_data/data/binance/
#
# Step 10 : Setup strategies
#
# In this case, copying "Simple" strategy from bakup
#
# cp -a ~/backup/sample_strategy6.py ~/freqtrade/user_data/strategies/
#
# Step 11 : Download historical data
#
# freqtrade download-data --exchange binance
#
# Step 12 : Backtest strategies in wich they represent a "class"
#
# freqtrade backtesting --strategy-list Simple
#
# Step 13 : Exporting backtesting results to json format file
#
# freqtrade backtesting --export trades --export-filename=backtest_simple_strategy.json --strategy-list Simple
#
# Step 14 : Docker-compose
#
# docker-compose run --rm freqtrade download-data --exchange binance --pairs ft_userdata/pairs.json (dont work)
# Creating pair list manualy instead
# docker-compose run --rm freqtrade download-data --pairs ETH/BTC ETH/USDT BTC/USDT XRP/ETH ALGO/BTC ATOM/BTC BAT/BTC BCH/BTC BRD/BTC EOS/BTC IOTA/BTC LINK/BTC LTC/BTC NEO/BTC NXS/BTC XMR/BTC XRP/BTC XTZ/BTC --exchange binance --days 30
# docker-compose run --rm freqtrade backtesting --export trades --export-filename=backtest_simple_strategy.json --strategy SampleStrategy