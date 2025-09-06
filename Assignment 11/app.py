from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        city = request.form['city']
        phone = request.form['phone']
        return redirect(url_for('details', name=name, email=email, city=city, phone=phone))
    return render_template('register.html')

@app.route('/details')
def details():
    name = request.args.get('name')
    email = request.args.get('email')
    city = request.args.get('city')
    phone = request.args.get('phone')
    return render_template('details.html', name=name, email=email, city=city, phone=phone)

if __name__ == '__main__':
    app.run(debug=True)
