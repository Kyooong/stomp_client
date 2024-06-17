from flask import Flask, send_from_directory, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('public', 'index.html')

@app.route('/set-cookie')
def set_cookie():
    response = make_response("Cookie has been set")
    response.set_cookie('AccessToken', 'your_access_token_value')
    return response

@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('public', path)

if __name__ == '__main__':
    app.run(port=3000)
