from flask import Flask, render_template
import requests
import json
app = Flask(__name__)

def blockcypher_api():
    global hash, height, block_time, previous
    blockcypher = requests.get("https://api.blockcypher.com/v1/eth/main").json()
    hash = blockcypher["hash"]
    height = blockcypher["height"]
    block_time = blockcypher["time"]
    previous = blockcypher["previous_hash"]

@app.route("/")
def home():
    blockcypher_api()
    return render_template("index.html", hash=hash, height=height, block_time=block_time, previous=previous)
