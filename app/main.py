#!/usr/bin/env python3

from flask import Flask, jsonify, request, Response
import os
import redis
import json
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
r = redis.StrictRedis(host='redis', port=6379, db=0)

@app.route('/store/<uuid>', methods=['GET', 'POST'])
def users(uuid):
    if request.method == 'GET':
        data = r.get(uuid)
        return Response(data, mimetype='application/json')

    elif request.method == 'POST':
        content = request.get_json(force=True)
        if not content:
            return jsonify(status='Provide json'), 500
        data = json.dumps(content)
        r.set(uuid, data)
        return jsonify(status='Stored new user')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
