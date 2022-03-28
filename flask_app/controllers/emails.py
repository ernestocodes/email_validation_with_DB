from flask import redirect, render_template, request
from flask_app import app
from flask_app.models.email import Email

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create', methods = ['POST'])
def create_email():
    if not Email.validate(request.form):
        return redirect('/')
    Email.create_email(request.form)
    return redirect ('/success')

@app.route('/success')
def success():
    emails = Email.get_all_emails()
    return render_template('success.html', emails = emails)

@app.route('/destroy/<int:id>')
def delete_email(id):
    id = {
        'id' : id
    }
    Email.delete_email(id)
    return redirect('/success')