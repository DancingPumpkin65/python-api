# Fast API advantages:
#     -Data validation: Enforces types in function signatures, and data schemas using Pydantic. 
#    Perform data validation, serialization, and documentation.
#     -Auto documentaion: Swagger UI / ReDoc automatically generated and API documentation updated.
#     -Auto completion and code suggestions: PyCharm, Visual Studio Code, and other editors 
#    support FastAPI.

# Baic Flask API
# from flask import Flask, request, jsonify

# app = Flask(__name__)

# @app.route('/get-user/<user_id>')
# def get_user(user_id):
#     user_data = {
#           'user_id': user_id,
#             'name': 'John Doe',
#             'email': 'john.doe@example.com'
#     }

#     extra = request.args.get('extra')
#     if extra:
#         user_data['extra'] = extra
    
#     return jsonify(user_data), 200

# if __name__ == '__main__':
#         app.run(debug=True)

# 
from fastapi import FastAPI

app = FastAPI()

# Endpoint: the point of entry in a communication channel when two systems are interacting.
# For example: '/hello' in localhost:8000/hello

