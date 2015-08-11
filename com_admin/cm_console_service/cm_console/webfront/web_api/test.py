# -*- coding:utf-8 -*-
from flask import render_template
from cm_console.api import app


@app.route('/webfront/<tmp_name>', methods=['GET', ])
def render_tml(tmp_name):
    tml_src = 'resources/%s' % tmp_name
    return render_template(tml_src)


@app.route('/webfront/themelocale', methods=['GET', ])
def show_theme():
    return render_template('themelocale/add.htm')


@app.route('/webfront/themelocale/viewdetial/<mid>', methods=['GET', ])
def show_detail(mid):
    return render_template('themelocale/edit.htm', model_id=mid)
