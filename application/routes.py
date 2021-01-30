# -*- coding: utf-8 -*-
from flask import render_template
from application import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'SaNya'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': {'username': 'Ипполит'},
            'body': 'Какая гадость эта ваша заливная рыба!!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/user')
def user():
    user = {'username': 'SaNya'}
    return render_template('user.html', title='User Page', user=user)
