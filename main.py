from flask import Flask, render_template, url_for, request, redirect


app = Flask(__name__)


@app.route('/', methods=['GET'])
@app.route('/page1', methods=['GET'])
def greeting():
    return render_template('greeting.html')

@app.route('/page2', methods=['GET', "POST"])
def contact():
   if request.method == 'GET':
       return render_template('contact.html')
   elif request.method == 'POST':
       print(request.form)
       return redirect('/page2')


if __name__ ==  '__main__':
    app.run()       