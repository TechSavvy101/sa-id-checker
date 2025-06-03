from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check_id():
    sa_id = request.form['sa_id']

    if len(sa_id) != 13 or not sa_id.isdigit():
        return render_template('result.html', error="Invalid SA ID Number. It must be 13 digits.")

    try:
        dob_str = sa_id[:6]
        dob = datetime.strptime(dob_str, "%y%m%d").date()
        today = datetime.today().date()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

        gender_code = int(sa_id[6:10])
        gender = "Female" if gender_code < 5000 else "Male"

        return render_template('result.html', dob=dob.strftime("%Y-%m-%d"), gender=gender, age=age)

    except ValueError:
        return render_template('result.html', error="Could not parse the ID number.")

if __name__ == '__main__':
    app.run(debug=True)
