from flask import Blueprint,render_template,request,flash,jsonify
# from flask.helpers import flash
# from flask_login import login_required,current_user
# from .models import Note
# import json
# from . import db

views=Blueprint('views',__name__)

@views.route('/')
def home_page():
    return render_template('home.html')
                        #    ,user=current_user)

@views.route('/market',methods=['GET', 'POST'])
# @login_required
def market_page():
    # if request.method == 'POST':
    #     note=request.form.get('note')
    #     if len(note)<1:
    #         flash('note short',category='error')
    #     else:            
    #         new_note=Note(data=note,user=current_user.id)
    #         db.session.add(new_note)
    #         db.session.commit()
    #         flash('note added',category='success')
            
    # if request.method == "GET":
    #     notss = Note.query.filter_by(user_id=None)
    #     user_id_notss = Note.query.filter_by(user_id=current_user.id)
    #     return render_template('market.html', notss=notss,user_id_notss=user_id_notss)

        
        
    return render_template('base.html')

# @views.route('/delete-note', methods=['POST'])
# def delete_note():
#     note=json.loads(request.data)
#     noteId=note['noteId']
#     note=Note.query.id(noteId)
#     if note and note.user(id) == current_user.id:
#             db.session.delete(note)
#             db.session.commit()
#     return jsonify({})