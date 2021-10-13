from flask import Blueprint,render_template,url_for,redirect,request,flash
from flask_login.utils import login_user,logout_user,current_user,login_required
from emo import db
from .models import User
from werkzeug.security import generate_password_hash,check_password_hash

auth=Blueprint('auth',__name__)

@auth.route('/login',methods=['GET', 'POST'])
def login_page():
    # if request.method == 'POST':
    #     email_address=request.form.get('email_address')
    #     password=request.form.get('password')
        
    #     user=User.query.filter_by(email_address=email_address).first()
        
    #     if user:
    #         flash('email already exists',category='error' )
    #     if user:
    #         if check_password_hash(user.password,password):
    #             flash('successful login',category='success')
    #             login_user(user,remember=True)
    #             return redirect(url_for('views.home_page'))
    #         else: 
    #             flash('error password',category='error')
    #     else:
    #         flash('error email',category='error')
            
    return render_template('login.html')
                        #    ,user=current_user)

@auth.route('/logout')
# @login_required
def logout_page():
    logout_user()
    return redirect(url_for('auth.login_page'))

@auth.route('/register',methods=['GET', 'POST'])
def register_page():
    # if request.method == 'POST':
    #     username=request.form.get('username')
    #     email_address=request.form.get('email_address')
    #     password1=request.form.get('password1')
    #     password2=request.form.get('password2')
    #     if len(email_address)<4:
    #         flash('enter correct email',category='error')
    #     elif len(username)<1:
    #         flash('enter yourname correctly',category='error')
    #     elif password1 != password2: 
    #         flash('password mismatch',category='error')       
    #     elif len(password1)<6:
    #         flash('password1 must be at least 4 characters')
    #     else:
    #         new_user=User(email_address=email_address,first_name=username,password=generate_password_hash(password1,method='sha256'))
    #         db.session.add(new_user)
    #         db.session.commit()
    #         flash('account created successfully',category='success')
    #         login_user( new_user ,remember=True)
    #         return redirect(url_for('view.home_page'))
            
    return render_template('register.html')
                        #    ,user=current_user)