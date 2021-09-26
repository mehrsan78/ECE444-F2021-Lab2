from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/')

def user():
  return render_template('user.html', name='Mehrsan', current_time = datetime.utcnow())

if __name__ == '__main__':
  app.run(debug=True)
