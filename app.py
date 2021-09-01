from flask import Flask, jsonify, request, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from werkzeug.utils import redirect

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class DbModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_URL = db.Column(db.String(150), nullable=False)
    short_URL = db.Column(db.String(100))

    def __repr__(self):
        return '<Shorties %r>' % self.id

@app.route('/', methods = ['POST', 'GET'])
def home():
    if request.method == 'POST':
        url_content = request.form['content']
        new_url = DbModel(full_URL=url_content)

        try:
            db.session.add(new_url)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding you URL to the database'
    else:
        urls = DbModel.query.order_by(DbModel.id).all()
        print('done')
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