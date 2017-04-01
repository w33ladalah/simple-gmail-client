from flask import Flask, render_template, request

from lib.gmail import read_email_from_gmail

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def main():
    mails = []
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        folder = request.form['folder'] if request.form['folder'] else 'Inbox'
        pattern = request.form['pattern'] if request.form['pattern'] else ''
        mails = read_mails(email, password, folder, pattern)

    return render_template('template.html', mails=mails)

def read_mails(email, password, folder, pattern):
    return read_email_from_gmail(email, password, folder, pattern)

if __name__ == "__main__":
    app.run()
