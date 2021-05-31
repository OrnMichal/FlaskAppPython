from flask import Flask
from flask import request
from flask import render_template
from flask import abort, redirect, url_for, make_response
from flask_dance.contrib.github import make_github_blueprint, github
import secrets
import os

app=Flask(__name__)

app.secret_key=secrets.token_hex(16)
os.environ['OAUTHLIB_INSECURE_TRANSPORT']='1'

github_blueprint = make_github_blueprint(
 client_id="505a6c8d295cc29ce85b",
 client_secret="38b3f1e872dba62e22b8f53441683c1bd6d93445",

)

app.register_blueprint(github_blueprint, url_prefix='/login')


@app.route('/')
def github_login():
    if not github.authorized:
        return redirect(url_for('github.login'))
    else:
        account_info = github.get('/user')
    if account_info.ok:
        return render_template('index.html')
    return '<h1>Request failed!</h1>'





@app.route('/about')
def about():
    return render_template('about.html')   

@app.route('/contact')
def contact():
    return render_template('contact.html') 
    
@app.route('/gallery')
def gallery():
    return render_template('gallery.html')



#Errors
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug=True)    