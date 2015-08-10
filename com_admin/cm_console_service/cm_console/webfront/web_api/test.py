# -*- coding:utf-8 -*-
from flask import render_template
from cm_console.api import app


@app.route('/webfront/hello', methods=['GET', ])
def index():
    return render_template('hello.html')


@app.route('/webfront/hello1', methods=['GET', ])
def index1():
    return render_template('hello1.htm')


@app.route('/webfront/themelocale', methods=['GET', ])
def show_theme():
    return render_template('themelocale/add.htm')


@app.route('/webfront/themelocale/viewdetial/<mid>', methods=['GET', ])
def show_detail(mid):
    return render_template('themelocale/edit.htm', model_id=mid)
