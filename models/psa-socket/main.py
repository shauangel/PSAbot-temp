# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 16:38:24 2021

@author: jacknahu
"""

from flask import Flask, request, abort, render_template, jsonify
from flask_socketio import SocketIO, emit, join_room, leave_room, close_room, rooms
from os import urandom
from datetime import datetime
import chat_data
import requests,re

app = Flask(__name__)
app.config['SECRET_KEY'] = urandom(24).hex()
socketio = SocketIO()
socketio.init_app(app,cors_allowed_origins='*')

# --------------- test socket.io --------------- #
# @socketio.on('connect')
# def test_connect():
#     print('# ---------- trigger connect event ...')
#     emit('connect', 'server says connected.')

   
# @socketio.on('join_room')
# def join_chat_room(data):
#     print('# ---------- client emit join_room ...')
#     print(data)
#     join_room(data['room'])
#     emit('room_msg', {'room': data['room'],'id':data['id'],'msg':'( has entered the room ... )'}, to=data['room'])
    
# @socketio.on('leave_room')
# def leave_chat_room(data):
#     print('# ---------- client emit leave_room ...')
#     print(data)
#     leave_room(data['room'])
#     emit('room_msg', {'room': data['room'],'id':data['id'],'msg':'( has left the room ... )'}, to=data['room'])

# @socketio.on('send_msg')
# def send_msg(data):
#     print('# ---------- client emit send_msg ...')
#     print(data)
#     emit('room_msg', {'room': data['room'],'id':data['id'],'msg':data['msg']}, to=data['room'])
    
# ---------------------------------------------- #
# ------------------- PSAbot ------------------- #
# client連線
@socketio.on('connect')
def connect():
    print('# ---------- trigger connect event ...')
    # 加入使用者個人房間
    user_id = request.args.get('user_id')
    join_room(user_id)
    print('client\'s rooms : ' , rooms())
    emit('connect', user_id + 'has connected.',to=user_id)

# 解除連線
@socketio.on('disconnect')
def disconnect():
    print('# ---------- trigger disconnect event ...')
    # 加入使用者個人房間
    
# 傳送問題資訊並建立聊天室
@socketio.on('create_room')
def create_room(data):
    # data: {'question':'',tags:[],'asker':{'user_id':'','user_name':'','incognito':''}}
    print('# ---------- client emit create_room ...')
    print(data)
    chat_dict = {
        '_id':'',
        'tags': data['tags'],
        'keywords': [],
        'question': data['question'],
        'time':datetime.now().replace(microsecond=0),
        'members': 
        [
            {
            'user_id':data['asker']['user_id'],
            'incognito':data['asker']['incognito']
            }
        ],
        'chat_logs':[],
        'end_flag':False
    }
    room_id = chat_data.insert_chat(chat_dict)
    # 將發問者加入聊天室
    join_room(room_id)
    print('new room id : ' + room_id)
    print('client\'s rooms : ' , rooms())
    emit('received_message', {'_id':room_id}, to=data['asker']['user_id'])

# 使用者加入聊天室
@socketio.on('join_room')
def join_chat_room(data):
    print('# ---------- client emit join_room ...')
    print(data)
    # data : { '_id','user_id','incognito'}
    chat_data.insert_member(data)
    join_room(data['_id'])
    print('client\'s rooms : ' , rooms())

@socketio.on('send_message')
def send_message(data):
    print('# ---------- client emit send_message ...')
    print(data)
    # 如果該client有在
    if data['_id'] in rooms():   
        # data : { '_id','user_id','time','type','content'}
        chat_dict = {
            '_id':data['_id'],
            'user_id': data['user_id'],
            'time': datetime.now().replace(microsecond=0),
            'type':data['type'],
            'content':data['content']
        }
        chat_data.insert_message(data)
        emit('received_message', chat_dict, to=data['_id'])
        # ------------------------------------------------- #
        # end_sentences = ['結束討論','結束共同討論','完成討論']
        # match = re.match(r'psabot ',chat_dict['content'],flags=re.IGNORECASE)
        # if match != None and match.span()[0] == 0: # 若是psabot開頭，丟給faq_api
        #   payload = {'sender_id':data['user_id'],'message':(re.sub(r'psabot ','',chat_dict['content'],flags=re.IGNORECASE))}
        #   headers = {'content-type': 'application/json'}
        #   r = requests.post('http://localhost:5006/webhooks/rest/webhook', json=payload,headers=headers )
        # elif chat_dict['content'] in end_sentences:
        #   chat_data.end_chat(chat_dict['_id'],True,1)
        #   current_chat = chat_data.query_chat(data['_id'])
        #   if data['user_id'] == current_chat['members'][0]['user_id']:
        #       replier_id = current_chat['members'][1]['user_id']
        #       payload = {'replier_id':replier_id,'message':'end_discuss'}
        #       headers = {'content-type': 'application/json'}
        #       r = requests.post('http://localhost:5005/webhooks/rest/webhook', json=payload,headers=headers )
        # if chat_data.end_chat(chat_dict['_id'],True,0):
        #       payload = {'replier_id':replier_id,'message':'end_discuss'}
        #       headers = {'content-type': 'application/json'}
        #       r = requests.post('http://localhost:5005/webhooks/rest/webhook', json=payload,headers=headers )
        # 關閉聊天室
        
    else:
        emit('received_message',
             {
                 '_id':data['user_id'],
                 'user_id':'system',
                 'time':datetime.now().replace(microsecond=0),
                 'type':'string',
                 'content':'Client isn\'t in room ' + data['_id'] + ', can\'t send messages.'},to=data['user_id'])

# 關閉聊天室(不刪除紀錄)
# @socketio.on('close_chat')
# def close_chat(data):
#     print('# ---------- client emit remove_chat ...')
#     print(data)
#     # 如果該room id有在client的room中
#     if data['_id'] in rooms():   
#         # data : { '_id','user_id','time','type','content'}
#         close_room(data['_id'])
#     else:
#         emit('received_message',
#              {
#                  '_id':data['user_id'],
#                  'user_id':'system',
#                  'time':datetime.now().replace(microsecond=0),
#                  'type':'string',
#                  'content':'Client isn\'t in room ' + data['_id'] + ', can\'t close the chat.'},to=data['user_id'])

# 取得聊天室歷史訊息
@socketio.on('query_chat')
def get_chat(data):
    chat_dict = chat_data.query_chat(data['_id'])
    # 將聊天紀錄傳給該client的user_id channel
    emit('received_message',chat_dict,to=data['user_id'])


if __name__ == "__main__":
    socketio.run(app,host='0.0.0.0',port=55003,debug=True)