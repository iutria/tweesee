from flask import Flask, request, jsonify
import tweesee
import user

app = Flask(__name__)

@app.route('/')
def index():
    return ''

@app.route('/buscar/<busqueda>', methods = ['GET'])
def search(busqueda):
    # return jsonify(user.user)
    usu = tweesee.buscar(busqueda)
    return jsonify(usu)

def error(error):
    return 'NOT FOUND', 404

if __name__ == '__main__':
    app.register_error_handler(404, error)
    app.run(debug = True, port = 5000)
    
    
 