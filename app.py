from AzureDB import AzureDB
from flask import Flask
from flask import request
from flask import render_template
from flask import abort, redirect, url_for, make_response
from flask.helpers import flash
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
            account_info_json = account_info.json()
            return render_template('index.html')
    return '<h1>Request failed!</h1>'





@app.route('/about')
def about():
    return render_template('about.html')   


    
@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/contact', methods=['POST','GET'])
def contact():
    if request.method == "POST":
        if len(request.form['name']) > 2 and len(request.form['mail']) > 3 and len(request.form['text']) > 5:
            res = AzureDB().azureAddData(request.form['name'],request.form['mail'],request.form['text'])
            flash('Komentarz został wysłany', category='success')
        
        else:
            flash('Niepoprawna forma komentarza, sprawdz', category='error')
    
    return render_template('contact.html')

app.route('/comments')
def comments():
    data = AzureDB().azureGetData()
    return render_template("comments.html", data = data)

@app.route('/comments/<int:id>/delete')
def delete_comm(id):
    AzureDB().azureDeleteData(id)
    return redirect('/comments')

@app.route("/comments/<int:id>/edit", methods=['POST', 'GET'])
def edit_comm(id):
    comm = AzureDB().azureGetDataid(id)
    if request.method == "POST":
        if len(request.form['text']) > 5:
            res = AzureDB().azureEditData(request.form['text'], id)
            return redirect('/comments')
        
        else:
            return 'Nie możesz zostawić pustych komentarz!'
    else:
        
        return render_template('edit.html', comm = comm)



#Errors
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug=True)    