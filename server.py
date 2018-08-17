from flask import Flask,request,jsonify
from flask import Flask
import matlab.engine

app = Flask(__name__)
eng = matlab.engine.start_matlab()
@app.route('/matlab', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        print 'POST'
        a,b = request.form['a'], request.form['b']
        ret1, ret2 = eng.A(float(a),float(b), nargout=2) #nargout=2 is necessary!
        print(ret1, ret2)
        response = jsonify({'ret1': ret1, 'ret2':ret2})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    else:
        print 'GET'
        return 'GET'
        

if __name__ == '__main__':
    
    app.run(host='0.0.0.0') # listen to the IP address you required