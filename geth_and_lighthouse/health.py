#!/usr/bin/python3

from flask import Flask, jsonify
import requests

app = Flask(__name__)

# Geth and Lighthouse endpoints
GETH_URL = "http://localhost:8545"
LIGHTHOUSE_URL = "http://localhost:5052"
EXT_NET_RPC = "https://sepolia.drpc.org"

# Helper function to convert hex to int
def hex_to_int(hex_value):
    return int(hex_value, 16)

@app.route("/status", methods=["GET"])
def check_status():
    try:
        # Get Geth syncing status
        geth_syncing_response = requests.post(
            GETH_URL,
            json={"jsonrpc": "2.0", "method": "eth_syncing", "params": [], "id": 1}
        ).json()

        if "result" in geth_syncing_response and geth_syncing_response["result"] is not False:
            syncing_data = geth_syncing_response["result"]
            geth_height = hex_to_int(syncing_data.get("currentBlock", "0x0"))
            highest_block = hex_to_int(syncing_data.get("highestBlock", "0x0"))

            if abs(geth_height - highest_block) > 20:
                return jsonify({
                    "status": "unhealthy",
                    "reason": f"Geth is syncing. Current: {geth_height}, Highest: {highest_block}"
                }), 500
        else:
            # If not syncing, fetch the current block
            geth_response = requests.post(
                GETH_URL,
                json={"jsonrpc": "2.0", "method": "eth_blockNumber", "params": [], "id": 1}
            ).json()
            geth_height = hex_to_int(geth_response["result"])

        # Get Lighthouse syncing status
        lighthouse_response = requests.get(f"{LIGHTHOUSE_URL}/eth/v1/node/syncing").json()
        lighthouse_height = int(lighthouse_response["data"]["head_slot"])
        is_syncing = lighthouse_response["data"]["is_syncing"]

        # Fetch the latest block height from the external RPC
        ext_rpc_response = requests.post(
            EXT_NET_RPC,
            json={"jsonrpc": "2.0", "method": "eth_blockNumber", "params": [], "id": 1}
        ).json()
        testnet_tip = hex_to_int(ext_rpc_response["result"])

        # Compare block heights
        if abs(testnet_tip - geth_height) <= 20 and abs(testnet_tip - lighthouse_height) <= 20 and not is_syncing:
            return jsonify({"status": "healthy"}), 200
        else:
            return jsonify({
                "status": "unhealthy",
                "reason": "One or more nodes are out of sync"
            }), 500

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint: /height
@app.route("/height", methods=["GET"])
def get_block_height():
    try:
        geth_response = requests.post(
            GETH_URL,
            json={"jsonrpc": "2.0", "method": "eth_blockNumber", "params": [], "id": 1}
        ).json()
        geth_height = hex_to_int(geth_response["result"])
    except Exception as e:
        return jsonify({"error": f"Geth error: {str(e)}"}), 500

    return jsonify({"geth_height": geth_height}), 200

# Endpoint: /peers
@app.route("/peers", methods=["GET"])
def get_peer_count():
    try:
        peer_response = requests.post(
            GETH_URL,
            json={"jsonrpc": "2.0", "method": "net_peerCount", "params": [], "id": 1}
        ).json()
        peer_count = hex_to_int(peer_response["result"])
    except Exception as e:
        return jsonify({"error": f"Geth peer count error: {str(e)}"}), 500

    return jsonify({"peer_count": peer_count}), 200

# Endpoint: /all
@app.route("/all", methods=["GET"])
def get_all_info():
    try:
        # Fetch Geth block height
        geth_response = requests.post(
            GETH_URL,
            json={"jsonrpc": "2.0", "method": "eth_blockNumber", "params": [], "id": 1}
        ).json()
        geth_height = hex_to_int(geth_response["result"])

        # Fetch Geth syncing status
        geth_syncing_response = requests.post(
            GETH_URL,
            json={"jsonrpc": "2.0", "method": "eth_syncing", "params": [], "id": 1}
        ).json()
        if "result" in geth_syncing_response and geth_syncing_response["result"] is not False:
            syncing_data = geth_syncing_response["result"]
            geth_syncing = True
            highest_block = hex_to_int(syncing_data.get("highestBlock", "0x0"))
        else:
            geth_syncing = False
            highest_block = None

        # Fetch Lighthouse syncing status
        lighthouse_response = requests.get(f"{LIGHTHOUSE_URL}/eth/v1/node/syncing").json()
        lighthouse_height = int(lighthouse_response["data"]["head_slot"])
        lighthouse_syncing = lighthouse_response["data"]["is_syncing"]

        # Fetch testnet tip
        ext_rpc_response = requests.post(
            EXT_NET_RPC,
            json={"jsonrpc": "2.0", "method": "eth_blockNumber", "params": [], "id": 1}
        ).json()
        testnet_tip = hex_to_int(ext_rpc_response["result"])

        # Fetch Geth peer count
        peer_response = requests.post(
            GETH_URL,
            json={"jsonrpc": "2.0", "method": "net_peerCount", "params": [], "id": 1}
        ).json()
        peer_count = hex_to_int(peer_response["result"])

        # Return all data
        return jsonify({
            "geth_height": geth_height,
            "geth_syncing": geth_syncing,
            "geth_highest_block": highest_block,
            "lighthouse_height": lighthouse_height,
            "lighthouse_syncing": lighthouse_syncing,
            "testnet_tip": testnet_tip,
            "peer_count": peer_count
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
