import cProfile
from flask import Flask, render_template, request
from flask_cors import CORS
from model import final_result  # Replace with your actual chatbot module and function

def c_profilefuction():
    app = Flask(__name__)
    CORS(app)

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/chat', methods=['POST'])
    def chat():
        try:
            user_message = request.form['user_message']
            bot_response = final_result(user_message)  # Replace with your actual chatbot function
            return {'bot_response': bot_response['result']}
        except Exception as e:
        # Handle the exception, log it, and return an appropriate response
            return {'error': str(e)}

    if __name__ == '__main__':
        app.run(host='0.0.0.0', port=8000)
if __name__ == '__main__':
    cProfile.run(c_profilefuction())
    
