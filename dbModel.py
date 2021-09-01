#Try to put dbModel in file of its own

# from flask_sqlalchemy import SQLAlchemy
# from app import app
# db = SQLAlchemy(app)

# class DbModel(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     full_URL = db.Column(db.String(150), nullable=False)
#     short_URL = db.Column(db.String(100))

#     def __repr__(self):
#         return '<Shorties %r>' % self.id