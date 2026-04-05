from flask import Blueprint, render_template, request, url_for, redirect, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
import os
import json
from app import db, login_manager
from app.models import User, Encounter
from app.forms import RegistrationForm, LoginForm, EncounterForm

bp = Blueprint('main', __name__)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@bp.route('/')
def home():
    page = request.args.get('page', 1, type=int)
    encounters = Encounter.query.order_by(
        Encounter.id.desc()
    ).paginate(page=page, per_page=6)
    return render_template('home.html', encounters=encounters)


@bp.route('/about')
def about():
    username = request.args.get('username')
    return render_template('about.html', username=username)


@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            flash('Username already exists!', 'danger')
            return redirect(url_for('main.register'))

        mail = User.query.filter_by(email=form.email.data).first()
        if mail:
            flash('Email already registered!', 'danger')
            return redirect(url_for('main.register'))

        new_user = User(
            username=form.username.data,
            email=form.email.data
        )
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()

        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('main.login'))
    return render_template('register.html', form=form)


@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash(f'Welcome back, {user.username}!', 'success')
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.home'))
        flash('Invalid email or password', 'danger')
    return render_template('login.html', form=form)


@bp.route('/logout')
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('main.home'))


@bp.route('/encounter/new', methods=['GET', 'POST'])
@login_required
def new_encounter():
    form = EncounterForm()
    if form.validate_on_submit():
        encounter = Encounter(
            title=form.title.data,
            grade=form.grade.data,
            description=form.description.data,
            location=form.location.data,
            user=current_user
        )
        db.session.add(encounter)
        db.session.commit()
        flash('Encounter submitted successfully!', 'success')
        return redirect(url_for('main.home'))
    return render_template('encounter_form.html', form=form, legend='New Encounter')


@bp.route('/user/<username>/encounters')
@login_required
def user_encounters(username):
    user = User.query.filter_by(username=username).first_or_404()
    page = request.args.get('page', 1, type=int)
    encounters = user.encounters.order_by(Encounter.id.desc()).paginate(page=page, per_page=6)
    return render_template('user_encounters.html', user=user, encounters=encounters)


@bp.route('/encounter/<int:encounter_id>/delete', methods=['POST'])
@login_required
def delete_encounter(encounter_id):
    encounter = Encounter.query.get_or_404(encounter_id)
    if encounter.user != current_user:
        flash('You cannot delete this encounter.', 'danger')
        return redirect(url_for('main.home'))
    db.session.delete(encounter)
    db.session.commit()
    flash('Encounter deleted.', 'success')
    return redirect(url_for('main.user_encounters', username=current_user.username))

@bp.route('/encounter/<int:encounter_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_encounter(encounter_id):
    encounter = Encounter.query.get_or_404(encounter_id)
    if encounter.user != current_user:
        flash('You cannot edit this encounter.', 'alert')
        return redirect(url_for('main.home'))
    form = EncounterForm()
    if form.validate_on_submit():
        encounter.title = form.title.data
        encounter.grade = form.grade.data
        encounter.description = form.description.data
        encounter.location = form.location.data
        db.session.commit()
        flash('Encounter updated.', 'success')
        return redirect(url_for('main.user_encounters', username=current_user.username))
    elif request.method == 'GET':
        form.title.data = encounter.title
        form.grade.data = encounter.grade
        form.description.data = encounter.description
        form.location.data = encounter.location
    return render_template('encounter_form.html', form=form, legend='Edit Encounter')   

@bp.route('/user/<username>/profile')
@login_required
def profile(username):

    user = User.query.filter_by(username=username).first_or_404()
    page = request.args.get('page', 1, type=int)
    encounters = user.encounters.order_by(Encounter.id.desc()).paginate(page=page, per_page=6)
    return render_template('profile.html', user=user, encounters=encounters)
