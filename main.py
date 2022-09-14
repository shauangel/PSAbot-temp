#!/usr/bin/env python3
# -*- coding: utf-8 -*-
host="0.0.0.0",
"""
Created on Mon Mar 15 16:44:08 2021

@author: linxiangling
"""
from flask import Flask

#from flask_apscheduler import APScheduler
#from flask_security import Security
from flask_cors import CORS
from views import register_blueprint
#from lib import config
from os import urandom
from models.PSAbotLoginManager import PSAbotLoginManager,UserModel

# from views.chat_socket import socketio,init_socketio
""" associated tags """
from datetime import date
import schedule
import time
from models import inner_post, tag

###test wsgi server
from werkzeug.middleware.proxy_fix import ProxyFix


def create_app():
    app = Flask(__name__)
    app.jinja_env.auto_reload = True
    app.config['SECRET_KEY'] = urandom(24).hex()
    #app.config.from_object(config.Config())
    CORS(app)
    # models setup
    #models.setup(app)
    
    # security setup

    # Security(app, models.user.USER_DATASTORE,login_form=models.user.ExtendedLoginForm)
    #''' --- login manager ---- '''
    #login_manager = PSAbotLoginManager(app)
    #@login_manager.user_loader
    #def user_loader(user_id):  
    #    user_now = UserModel(user_id)   
    #    return user_now
    # register app
    register_blueprint(app)
    # socket io
    # print('create_app() call init_socketio(app).')
    # init_socketio(app)
    

    return app

def check_associated_tag():
    if date.today().day != 1:
        return
    new=inner_post.check_associated_tag() #tuple list
    for i in new:
        associated_tag_id=tag.add_new_associated_tag(i)
        tag.add_child_associated(i, associated_tag_id)

def test_wsgi_app(environ, start_response):
	# scheduler=APScheduler()
    app = create_app()
    # scheduler.init_app(app)
    # scheduler.start()
    #####app.run(host='0.0.0.0',port=55001,debug=True) 
    #"192.168.111.128",port=55001
    app.wsgi_app = ProxyFix(app.wsgi_app)
	app.run()

    """ 每個月一號的0:00檢查是否新增 associated tag """
    schedule.every().day.at("02:00").do(check_associated_tag)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    # scheduler=APScheduler()
    app = create_app()
    # scheduler.init_app(app)
    # scheduler.start()
    app.run(host='0.0.0.0',port=55001,debug=True)
    #app.run(host='0.0.0.0', port=55001)    
    #"192.168.111.128",port=55001
    
    """ 每個月一號的0:00檢查是否新增 associated tag """
    schedule.every().day.at("02:00").do(check_associated_tag)
    while True:
        schedule.run_pending()
        time.sleep(1)




