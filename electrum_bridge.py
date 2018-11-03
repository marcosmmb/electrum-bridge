from flask_jsonpify import jsonify
from flask_restful import Api, Resource
from flask import Flask, request
import subprocess
import json

def command(string, testnet=False):

	args = string.split()

	cmd = []

	cmd.append("electrum")

	for a in args:
		cmd.append(a)

	if testnet:
		cmd.append("--testnet")

	result = subprocess.run(cmd, stdout = subprocess.PIPE).stdout.decode("utf-8")

	try:
		return json.loads(result)
	except:
		return result


class Bridge(Resource):
    def post(self):
        json_dict 	= request.get_json()
        cmd 	= json_dict["command"]
        testnet		= json_dict["testnet"]
        return jsonify(command(cmd, testnet))


app = Flask(__name__)
api = Api(app)

api.add_resource(Bridge, "/")

if __name__ == "__main__":
    app.run(host="188.166.149.243", port=7778)