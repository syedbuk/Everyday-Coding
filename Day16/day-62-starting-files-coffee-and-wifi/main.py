from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TimeField, SelectField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class Cafe:
    def __init__(self, cafe, location_url, open_time, closing_time, coffee_rating, wifi_rating, power_outlet_rating):
        self.cafe = cafe
        self.location_url = location_url
        self.open_time = open_time
        self.closing_time = closing_time
        self.coffee_rating = coffee_rating
        self.wifi_rating = wifi_rating
        self.power_outlet_rating = power_outlet_rating


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])

    location_url = StringField(
        'Location',
        validators=[DataRequired(), URL(message="Enter valid URL")]
    )

    open_time = TimeField('Opening Time', format='%H:%M', validators=[DataRequired()])
    closing_time = TimeField('Closing Time', format='%H:%M', validators=[DataRequired()])

    coffee_rating = SelectField(
        'Coffee Rating',
        coerce=int,
        choices=[(1,'⭐'), (2,'⭐⭐'), (3,'⭐⭐⭐'), (4,'⭐⭐⭐⭐'), (5,'⭐⭐⭐⭐⭐')],
        validators=[DataRequired()]
    )

    wifi_rating = SelectField(
        'WiFi Rating',
        coerce=int,
        choices=[(1,'⭐'), (2,'⭐⭐'), (3,'⭐⭐⭐'), (4,'⭐⭐⭐⭐'), (5,'⭐⭐⭐⭐⭐')],
        validators=[DataRequired()]
    )

    power_outlet_rating = SelectField(
        'Power Outlet Rating',
        coerce=int,
        choices=[(1,'⭐'), (2,'⭐⭐'), (3,'⭐⭐⭐'), (4,'⭐⭐⭐⭐'), (5,'⭐⭐⭐⭐⭐')],
        validators=[DataRequired()]
    )

    submit = SubmitField('Submit')


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("Form submitted successfully!")
        # CSV writing will go here
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    list_of_rows = []
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        for row in csv_data:
            cafe = Cafe(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
            list_of_rows.append(cafe)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
