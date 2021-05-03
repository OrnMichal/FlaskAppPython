from flask import Flask
from flask import request
from flask import render_template
from flask import abort, redirect, url_for, make_response
app=Flask(__name__)

#add pages here
@app.route('/')
def index():
    return render_template('index.html')

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
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

@app.route('/error_denied')
def error_denied():
    abort(401)

@app.route('/error_internal')
def error_internal():
    return render_template('template.html', name='ERROR 505'), 505


if __name__ == '__main__':
    app.run(debug=True)    