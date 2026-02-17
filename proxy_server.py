from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app) 

AZURE_ENDPOINT = "https://noviprojekt-nzjjj.polandcentral.inference.ml.azure.com/score"
API_KEY = "D4QF0YSZGHtm0QHpWurNLevzdl0kjT19pl52K5uZBYDOlBmCRDBcJQQJ99CBAAAAAAAAAAAAINFRAZML0IMG"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        
        response = requests.post(
            AZURE_ENDPOINT,
            json=data,
            headers={
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {API_KEY}'
            }
        )
        
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
