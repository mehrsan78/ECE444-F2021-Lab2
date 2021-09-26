from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required, ValidationError


app = Flask(__name__)
bootstrap = Bootstrap(app)


app.config['SECRET_KEY'] = 'key'

@app.route('/', methods=['GET', 'POST'])
def index():
    form = FormUofT()

    if form.validate_on_submit():
        old_name = session.get('name')
        old_email = session.get('email')

        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        if old_email is not None and old_email != form.email.data:
            flash('Looks like you have changed your email!')

        session['name'] = form.name.data
        session['email'] = form.email.data
        return redirect(url_for('index'))

    return render_template(
        'index.html',
        form=form,
        name=session.get('name'),
        email=session.get('email')
    )

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


class EmailCheck(object):

    def __call__(self, form, field):
        if '@' not in field.data:
            message = 'Please include an \'@\' in the email address. \'' + field.data + '\' is missing an \'@\'.'
            raise ValidationError(message)

class FormUofT(Form):
    name = StringField('What is your name?', validators=[Required()])
    email = StringField('What is your UofT Email address?', validators=[EmailCheck()])
    submit = SubmitField('Submit')


if __name__ == '__main__':
    app.run(debug=True)
