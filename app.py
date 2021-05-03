from flask import Flask, render_template

app=Flask(__name__)

#add pages here
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')   

@app.route('/contact')
def about():
    return render_template('contact.html') 
    
@app.route('/gallery')
def about():
    return render_template('gallery.html')


if __name__ == '__main__':
    app.run(debug=True)    