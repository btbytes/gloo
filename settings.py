#!/usr/bin/env python
# encoding: utf-8
"""
settings.py

Created by Pradeep Gowda on 2008-09-25.
Copyright (c) 2008 Pradeep Gowda. All rights reserved.
"""

import sys
import os
import web

render = web.template.render('templates/', base='base', cache=False)
db = web.database(dbn=os.environ.get('DATABASE_ENGINE', 'mysql'),
                  db='gloo', user="user", passwd="password")
                  
session = web.session.Session(None, web.session.DBStore(db,'sessions'))
def setup_session(app):
    app.add_processor(session._processor)
