from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)  #Flask class instantiates an app
print(__name__)

@app.route("/")
def my_home():
    return render_template('index.html')  #uses template

@app.route("/<string:page_name>")  #works dynamically now for any pages added
def html_page(page_name):
    return render_template(page_name)  #uses template

def write_to_file(data):
    with open('database.txt', mode='a')  as database: #append mode
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2: #append mode
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"',quoting = csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong. Try again.'