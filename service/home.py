from config.loggin import logger
from flask import jsonify

def home():
    return jsonify(
        {
            'status':True
        }
    )