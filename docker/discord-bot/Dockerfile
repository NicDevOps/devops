FROM python:3.6-slim

COPY ./discord-bot.py /app/discord-bot.py

RUN echo "aaaaa" && echo "bbbbb"

RUN python3 -m pip install discord requests tornado

CMD ["python3", "/app/discord-bot.py"]
