from hashlib import sha1
from flask import request, Module, render_template, url_for, redirect, session, flash, get_flashed_messages
from context import context_processors
from decorators import requires_auth, requires_admin
from models import Score

views = Module(__name__, 'views')
views.app_context_processor(context_processors)

@views.context_processor
def add_auth():
    return {'auth': session.get('type')}

@views.route('/')
def index():
    den = Score.get_or_insert('den', name='Denver', amount=0)
    sea = Score.get_or_insert('sea', name='Seattle', amount=0)
    den_factor = 100
    sea_factor = 100
    if den.amount > sea.amount:
        sea_factor = sea.amount * 100.0 / den.amount
    elif sea.amount > den.amount:
        den_factor = den.amount * 100.0 / sea.amount
    den_factor *= 0.8
    sea_factor *= 0.8
    return render_template('index.html', den=den, sea=sea, den_factor=den_factor, sea_factor=sea_factor)

@views.route('/login')
def login():
    return render_template('login.html')

@views.route('/login', methods=['POST'])
def login_submit():
    if request.form['password'] == 'GOTRDenver18':
        session['type'] = 'den'
        return redirect(url_for('edit', team='den'))
    if request.form['password'] == 'GOTRSeattle3':
        session['type'] = 'sea'
        return redirect(url_for('edit', team='sea'))
    if request.form['password'] == 'GOTRAdmin1':
        session['type'] = 'admin'
        return redirect(url_for('edit', team='den'))
    return render_template('login.html', error='Incorrect password.')

@views.route('/logout')
def logout():
    session['type'] = None
    return redirect(url_for('index'))

@views.route('/<team>')
def edit(team):
    if team not in ['den', 'sea']:
        return 'Page not found.', 404
    if session.get('type') not in ['den', 'admin']:
        return redirect(url_for('login'))
    score = Score.get_by_key_name(team)
    return render_template('edit.html', score=score)

@views.route('/<team>', methods=['POST'])
def edit_submit(team):
    if team not in ['den', 'sea']:
        return 'Page not found.', 404
    if session.get('type') not in [team, 'admin']:
        return redirect(url_for('login'))
    score = Score.get_by_key_name(team)
    amount = request.form.get('amount', 'empty')
    try:
        score.amount = int(float(amount) * 100)
        score.save()
        flash('Amount updated successfully!', 'success')
        return redirect(url_for('edit', team=team))
    except ValueError:
        return render_template('edit.html', score=score, error='Invalid value "%s".' % amount)
