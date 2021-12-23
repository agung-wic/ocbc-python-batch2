from flask import Flask, escape, request, render_template
from data import data
# from markupsafe import escape
app = Flask(__name__)


@app.route('/')
def index():
    return "Index Page"


@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/user/<username>')
def show_user_profile(username):
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return f'Subpath {escape(subpath)}'

@app.route('/pirates/<pirates_id>')
def pirates_name(pirates_id):
    return render_template('pirates.html', pirates_id=pirates_id, pirate_list=data[pirates_id])

@app.route('/pirates', methods=['GET', 'POST'])
def pirates():
    if 'pirates_id' in request.form:
        data[request.form['pirates_id']] = []
    return render_template('pirates.html', data = data)


if(__name__) == '__main__':
    app.run(debug=True)
