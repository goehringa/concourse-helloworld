from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def helloworld():
  response = 'hello world'
  uppercase = request.args.get('uppercase')
  reversed = request.args.get('reversed')
  if uppercase == 'true' and reversed == 'true':
    response = response.upper()
    response = response[::-1]
  elif uppercase == 'true':
    response = response.upper()
  elif reversed == 'true':
    response = response[::-1]
  else:
    response = 'hello world'
  return response

@app.route('/hello', methods=['GET'])
def hello():
  response = 'hello'
  uppercase = request.args.get('uppercase')
  reversed = request.args.get('reversed')
  if uppercase == 'true' and reversed == 'true':
    response = response.upper()
    response = response[::-1]
  elif uppercase == 'true':
    response = response.upper()
  elif reversed == 'true':
    response = response[::-1]
  
  return response

@app.route('/world', methods=['GET'])
def world():
  response = 'world'
  uppercase = request.args.get('uppercase')
  reversed = request.args.get('reversed')
  if uppercase == 'true' and reversed == 'true':
    response = response.upper()
    response = response[::-1]
  elif uppercase == 'true':
    response = response.upper()
  elif reversed == 'true':
    response = response[::-1]
  
  return response

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80)
