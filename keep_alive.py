from flask import Flask
from threading import Thread

app = Flask('')


@app.route('/')
def home():
  return "ンゴ～"


def run():
  app.run(host='0.0.0.0', port=25252)


def keep_alive():
  t = Thread(target=run)
  t.start()