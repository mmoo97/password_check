from flask import Flask, render_template, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, validators

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secretkey'

pass


class MyForm(FlaskForm):
    username = StringField('Username: ', [validators.DataRequired(), ])
    password = PasswordField('Password: ', [validators.DataRequired(), ])
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    username = False
    password = False
    form = MyForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        form.username.data = ''
        form.password.data = ''
        # return redirect(url_for('report'))
        result = False
        if (any(c.islower() for c in password)) and (any(c.isupper() for c in password))\
                and password[-1].isdigit():
            result = True

        return render_template('report.html', password=password, result=result)
    return render_template('index.html', form=form, username=username, password=password)


@app.route('/result')
def report():
    return render_template('report.html', )


if __name__== '__main__':
    app.run(debug=True)
