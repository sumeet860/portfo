# Flask
from flask import Flask, render_template, url_for, request, redirect
import csv


app = Flask(__name__)

# print(__name__)


@app.route('/')
def my_home():

    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def write_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email}, {subject}, {message}')


def write_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_csv(data)
            return redirect('thankyou.html')
        except:
            return 'Information not saved into database. Please try again'
    else:
        return 'try again'


'''
if __name__ == '__main__':
    debug = True
    app.run()
'''
