from flask import Flask, render_template
import requests
import json
app = Flask(__name__)

def blockcypher_api():
    global hash, height, block_time, previous, eth_hash, eth_height, eth_block_time, eth_previous
    blockcypher = requests.get("https://api.blockcypher.com/v1/btc/main").json()
    hash = blockcypher["hash"]
    height = blockcypher["height"]
    block_time = blockcypher["time"]
    previous = blockcypher["previous_hash"]
    blockcypher_eth = requests.get("https://api.blockcypher.com/v1/eth/main").json()
    eth_hash = blockcypher_eth["hash"]
    eth_height = blockcypher_eth["height"]
    eth_block_time = blockcypher_eth["time"]
    eth_previous = blockcypher_eth["previous_hash"]

@app.route("/")
def home():
    blockcypher_api()
    return render_template("index.html",
           hash=hash,
           height=height,
           block_time=block_time,
           previous=previous,
           eth_hash=eth_hash,
           eth_height=eth_height,
           eth_block_time=eth_block_time,
           eth_previous=eth_previous)
