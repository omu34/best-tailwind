# from . import db
# from flask_login import UserMixin
# from sqlalchemy.sql import func


# class User(UserMixin, db.Model):
#     id = db.Column(db.Integer, primary_key=True)     
#     username = db.Column(db.String(length=30), nullable=False)     
#     email_address = db.Column(db.String(length=50),nullable=False, unique=True)
#     password = db.Column(db.String(length=60), nullable=False)    
#     notes = db.relationship('Note', backref='owned_user', lazy=True)
    
# class Note(db.Model):
#     id = db.Column(db.Integer, primary_key=True)    
#     data= db.Column(db.String(length=1000),nullable=False) 
#     date = db.Column(db.DateTime(timezone=True),nullable=False, default=func.now)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    
#     def __repre__(self):
#         return f'User,Note{self.id}'
