import random
import re
import sys
import threading
import time
from faker import Faker
from flask import Flask, render_template
from turbo_flask import Turbo

fake = Faker()
app = Flask(__name__)
turbo = Turbo(app)

@app.context_processor
def generateName():
    randomName = fake.name()
    return {'randomPerson': randomName}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/page2')
def page2():
    return render_template('page2.html')

@app.before_first_request
def before_first_request():
    threading.Thread(target=updateName).start()

def updateName():
    with app.app_context():
        while True:
            time.sleep(3)
            turbo.push(turbo.replace(render_template('random_names.html'), 'random-names'))

