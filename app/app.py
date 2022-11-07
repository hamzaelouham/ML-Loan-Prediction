from flask import Flask , jsonify,request

app = Flask(__name__)

@app.get('/')
def render_home():
    print('home page rendered ...')
    pass



if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)