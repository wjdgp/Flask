from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/method_get', methods = ['GET'])
def method_get():
  return render_template('method_get.html')

@app.route('/method_get_act', methods=['GET'])
def method_get_act():
  if request.method == 'GET':
    id_param = request.args['id']
    password_param = request.args.get('password')
  return render_template('method_get.html', id=id_param, password = password_param)



if __name__ == '__main__':
  app.run(debug=True, port='80', host='0.0.0.0')