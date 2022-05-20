from flask.templating import render_template
from day10.dao_emp import DaoEmp
from flask.globals import request
from flask.app import Flask
de = DaoEmp()


app = Flask(__name__)

@app.route('/list')
def list():
    
    
    emps = de.myselects()
    # update = de.myupdate(e_id, e_name, sex, addr)
    # delete = de.mydelete(e_id)
    return render_template('list.html', emps=emps)

@app.route('/add')
def add():
    return render_template('add.html')


@app.route('/add_act', methods=['POST'])
def add_act():
    e_id = request.form.get('e_id')
    e_name = request.form.get('e_name')
    sex = request.form.get('sex')
    addr = request.form.get('addr')
    cnt = de.myinsert(e_id,e_name,sex,addr)
    return render_template('add_act.html', cnt=cnt)



@app.route('/update')
def update():
    e_id = request.args.get('e_id')
    emp = de.myselect(e_id)
    print(emp)
    return render_template('update.html', emp=emp)


@app.route('/update_act', methods=['POST'])
def update_act():
    e_id = request.form.get('e_id')
    e_name = request.form.get('e_name')
    sex = request.form.get('sex')
    addr = request.form.get('addr')
    cnt = de.myupdate(e_name, sex, addr,e_id)
    
    return render_template('update_act.html', cnt=cnt)



# @app.route('/delete')
# def delete():
#     e_id = request.args.get('e_id');
#     return render_template('update.html', e_id=e_id)


@app.route('/delete_act')
def delete_act():
    e_id = request.args.get('e_id')
    cnt = de.mydelete(e_id)
    return render_template('delete_act.html', cnt=cnt)
    
    


if __name__ == '__main__':
    app.run(debug=True)
    
    
    