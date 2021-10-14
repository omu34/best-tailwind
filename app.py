# from bestauth import db, create_app
# db.create_all(app=create_app())

from emo import create_app
app=create_app()
if __name__ == '__main__': 
    app.run(port=3400, debug=True)
