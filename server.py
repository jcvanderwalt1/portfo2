from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)

@app.route('/') # Decorator
def home():
    return render_template('index.html')

@app.route('/<string:page_name>') # Decorator
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a') as database_txt:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        firstname = data["firstname"]
        lastname = data["lastname"]
        file = database_txt.write(f'{firstname}, {lastname},{email},{subject},{message}\n')

def write_to_csv(data):
    with open('database.csv', mode='a') as database_csv:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        firstname = data["firstname"]
        lastname = data["lastname"]
        csv_write = csv.writer(database_csv,delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_write.writerow([firstname,lastname,email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('thankyou.html')
        except:
            return 'did not send to database'
    else:
        return 'something went wrong, try again'