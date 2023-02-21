from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

menu = [
        {'name':'About me', 'url':'/'},
        {'name':'Contact', 'url':'contact'},
        {'name':'Send a message', 'url':'feedback'}
        ]


@app.route('/')
def greeting():
    return render_template('greeting.html', menu = menu)

@app.route('/contact')
def contact():
    return render_template('contact.html', menu = menu)


@app.route('/feedback', methods=['GET', "POST"])   
def feedback():
    if request.method == 'POST':
         print(request.form)
    return render_template('feedback.html', menu = menu)  


if __name__ ==  '__main__':
    app.run()       