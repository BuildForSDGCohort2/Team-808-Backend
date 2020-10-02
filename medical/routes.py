from flask import render_template, url_for, flash, redirect
from medical import app,db, bcrypt
from medical.forms import RegistrationForm, LoginForm
from medical.models import User, Patient

patients = [
    {
        'patient_names': 'Coco jo',
        'dr_names': 'abe rwis',
        'age': '38',
        'gender': 'female',
        'test': 'MRI',
        'result': 'back pain',
        'medical_imaging': '',
        'date_posted': 'April 20, 2020'
    },
    {
        'patient_names': 'bebe deo',
        'dr_names': 'mimi nelo',
        'age': '27',
        'gender': 'male',
        'test': 'scan',
        'result': 'foot',
        'medical_imaging': '',
        'date_posted': 'May 3, 2020'
    }
]



@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/allpatient')
def allpatient():
    return render_template('allpatient.html', patients=patients)

@app.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(firstname=form.firstname.data,lastname=form.lastname.data,jobname=form.jobname.data,hospital=form.hospital.data,rmdc=form.rmdc.data ,email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Account created, you are now able to login', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', form=form)


