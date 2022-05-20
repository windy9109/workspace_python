from flask.templating import render_template
from day10.dao_emp import DaoEmp
from flask.globals import request
from flask.app import Flask
from flask.json import jsonify
from flask_cors.extension import CORS


de = DaoEmp()


app = Flask(__name__)
CORS(app)

@app.route('/emp')
def emp():
    return render_template('emp.html')


@app.route('/ajax')
def ajax():
    emps = de.myselects()
    return jsonify({'msg': emps })
    #return jsonify({'msg':'저장완료'})
    
@app.route('/detail', methods=['POST'])
def detail():
    d = request.get_json()
    e_id = d['e_id']
    detail = de.myselect(e_id)
    return jsonify(detail)
    #return jsonify({'msg':'저장완료'})


@app.route('/add', methods=['POST'])
def add():
    aa = request.get_json()
    e_id = aa['e_id']
    e_name = aa['e_name']
    sex = aa['sex']
    addr = aa['addr']
    cnt = de.myinsert(e_id,e_name,sex,addr)
    return jsonify({'cnt': cnt })

@app.route('/update', methods=['POST'])
def update():
    c = request.get_json()
    e_id = c['e_id']
    e_name = c['e_name']
    sex = c['sex']
    addr = c['addr']
    cnt = de.myupdate(e_name,sex,addr,e_id)
    return jsonify({'cnt': cnt })


@app.route('/delete', methods=['POST'])
def delete():
    b = request.get_json()
    e_id = b['e_id']
    cnt = de.mydelete(e_id)
    return jsonify({'cnt': cnt })



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    
    # if __name__ == '__main__':
    # socket_io.run(app, debug=False, host='0.0.0.0', port=7777)