from os import error
from flask import Flask, jsonify, request, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from werkzeug.utils import redirect
import requests
import json

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class DbModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_URL = db.Column(db.String(150), nullable=False)
    short_URL = db.Column(db.String(150))

    def __repr__(self):
        return '<Shorties %r>' % self.id

@app.route('/', methods = ['POST', 'GET'])
def home():
    if request.method == 'POST':
        url_content = request.form['content']
        new_url = DbModel(full_URL=url_content)

        linkRequest = {
        "destination": url_content 
        , "domain": { "fullName": "rebrand.ly" }
        }

        requestHeaders = {
        "Content-type": "application/json",
        "apikey": "4136a72da0db4073bcf211340b9cfb0c",
        }

        r = requests.post("https://api.rebrandly.com/v1/links", 
            data = json.dumps(linkRequest),
            headers=requestHeaders)

        if (r.status_code == requests.codes.ok):
            link = r.json()
            print(link)
            print("Long URL was %s, short URL is %s" % (link["destination"], link["shortUrl"]))
            anotherVariable = link["shortUrl"]
            print(anotherVariable)
            shorty_url = DbModel(short_URL=anotherVariable)
            # dataset1 = (new_url, shorty_url)
            # dataset2 = (DbModel(full_URL=url_content), DbModel(short_URL=anotherVariable))
            # dataset3 = (DbModel(short_URL=anotherVariable), DbModel(full_URL=url_content))
        else:
            print('Sorry there has been the following http error: ' + {{r.status_code}})

        try:
            print('issue 1')
            # db.session.add(dataset1)
            # db.session.add(dataset2)
            # db.session.add(dataset3)
            db.session.add(new_url, shorty_url)
            print('issue 2')
            # db.session.add(shorty_url)
            print('issue 3')
            db.session.commit()
            print('issue 4')
            return redirect('/')
        except:
            # print(error.)
            return 'There was an issue adding you URL to the database'
    else:
        urls = DbModel.query.order_by(DbModel.id).all()
        return render_template('index.html', urls=urls )

@app.route('/delete/<int:id>')
def delete(id):
    url_to_delete = DbModel.query.get_or_404(id)
    try:
        db.session.delete(url_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting this URL'

if __name__ == "__main__":
    app.run(debug=True)