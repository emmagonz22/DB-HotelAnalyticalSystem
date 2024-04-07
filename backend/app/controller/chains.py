from app.models.chains import ChainsDAO
from flask import jsonify

class BaseChains:
    def getAllChains(self):
        model = ChainsDAO()
        result = model.getAllChains()
        return jsonify(result)