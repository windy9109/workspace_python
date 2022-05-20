from flask.templating import render_template
from day10.dao_emp import DaoEmp
from flask.globals import request
from flask.app import Flask
from flask.json import jsonify
de = DaoEmp()


app = Flask(__name__, static_url_path='')

@app.route('/emp')
def emp():
    return render_template('babyl3.html')



if __name__ == '__main__':
    app.run()
    #debug=True