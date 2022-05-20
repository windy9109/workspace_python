from flask import Flask, jsonify, render_template
from subprocess import call
from flask_socketio import SocketIO, send
import random
from flask import request
import requests
import flask

app = Flask(__name__)
app.secret_key = "mysecret"


socket_io = SocketIO(app)
ans =""


a= (int)(random.random()*9);
b= (int)(random.random()*9);
c= (int)(random.random()*9);
while(a == b or a == c or b == c):
    a= (int)(random.random()*9);
    b= (int)(random.random()*9);
    c= (int)(random.random()*9); 
ans = str(a)+str(b)+str(c);
print("ans", ans)



 

# @app.route("/get_my_ip", methods=["GET"])
# def get_my_ip():
#     return jsonify({'ip': request.remote_addr}), 200   


@app.route('/')
def strike():
    ip= flask.request.remote_addr
    return render_template('strike.html', ip=ip)


    

@socket_io.on("message")
def request(message):
    print("message : "+ message)
    arr = message.split(",")
    
    if arr[0] == "check":
        
        str_3 = arr[1]
        strike = 0
        ball = 0
        
        m1 = str_3[0:1]
        m2 = str_3[1:2]
        m3 = str_3[2:3]
        
        c1 = ans[0:1]
        c2 = ans[1:2]
        c3 = ans[2:3]
        
        if(m1==c1): strike+=1
        if(m2==c2): strike+=1
        if(m3==c3): strike+=1
        
        if(m1==c2) or (m1==c3): ball+=1
        if(m2==c1) or (m2==c3): ball+=1
        if(m3==c1) or (m3==c2): ball+=1
        
        ret = str(strike)+"S"+str(ball)+"B"
        
        
        to_client = dict()
        to_client['message'] = message+","+ret
        send(to_client, broadcast=False)
    else:
        to_client = dict()
        to_client['message'] = message
        send(to_client, broadcast=True)
    
    

if __name__ == '__main__':
    socket_io.run(app,host="0.0.0.0", port=9999)

