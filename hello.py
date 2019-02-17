from flask import Flask, render_template
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)

@app.route('/')
def index():
    # return '<h1>Hello World!</h1>'
    return render_template('index.html')

    # from flask import make_response
    # response = make_response('<h1> This document carries a cookie! </h1>')
    # response.set_cookie('answer', '42')
    # return response

    # from flask import redirect
    # return redirect('http://www.baidu.com')


@app.route('/user/<user>')
def user(user):
    return render_template('user.html', name=user)
    # return '<h1> Hello, {}! </h1>'.format(name)

    # from flask import abort
    # user = False
    # if not user:
    #     abort(404)
    # return '<h1> Hello, %s! </h1>' % name


if __name__ == '__main__':
    app.run(port = 8000, debug = True)
    # manager.run()
