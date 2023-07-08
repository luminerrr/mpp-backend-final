from xlwings.rest.api import api
from waitress import serve

if __name__ == "__main__":
    #app.run('0.0.0.0',port=server_port)
    serve(api, host='127.0.0.1', port=8080)