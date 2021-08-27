from flask_socketio import SocketIO,emit, join_room, leave_room, close_room, rooms
from flask import session
from models import chat_data
from datetime import datetime

socketio = SocketIO()
def init_socketio(app):
    print('# ---------- init socket_io ...')
    socketio.init_app(app,cors_allowed_origins='*')
# --------------- test socket.io --------------- #
@socketio.on('connect')
def test_connect():
    print('# ---------- trigger connect event ...')
    emit('connect', 'server says connected.')

   
@socketio.on('join_room')
def join_chat_room(data):
    print('# ---------- client emit join_room ...')
    print(data)
    join_room(data['room'])
    emit('room_msg', {'room': data['room'],'id':data['id'],'msg':'( has entered the room ... )'}, to=data['room'])
    
@socketio.on('leave_room')
def leave_chat_room(data):
    print('# ---------- client emit leave_room ...')
    print(data)
    leave_room(data['room'])
    emit('room_msg', {'room': data['room'],'id':data['id'],'msg':'( has left the room ... )'}, to=data['room'])

@socketio.on('send_msg')
def send_msg(data):
    print('# ---------- client emit send_msg ...')
    print(data)
    emit('room_msg', {'room': data['room'],'id':data['id'],'msg':data['msg']}, to=data['room'])
    
# ---------------------------------------------- #
# ------------------- PSAbot ------------------- #
# # client連線
# @socketio.on('connect')
# def connect():
#     print('# ---------- trigger connect event ...')
#     # 加入使用者個人房間
#     join_room(session['user_id'])
#     emit('connect', 'join room' + session['user_id'],to=session['user_id'])

# # 解除連線
# @socketio.on('disconnect')
# def disconnect():
#     print('# ---------- trigger disconnect event ...')
#     # 加入使用者個人房間
#     close_room(session['user_id'])
    
# 傳送問題資訊並建立聊天室
@socketio.on('create_room')
def create_room(data):
    # data: {'question':'',tags:[],'asker':{'user_id':'','user_name':'','incognito':''}}
    print('# ---------- client emit create_room ...')
    print(data)
    chat_dict = {
        '_id':'',
        'tags': data['tags'],
        'question': data['question'],
        'time':datetime.now().replace(microsecond=0),
        'members': 
        [
            {
            'user_id':data['asker']['user_id'],
            'user_name':data['asker']['user_name'],
            'incognito':data['asker']['incognito']
            }
        ],
        'chat_logs':[]
    }
    room_id = chat_data.insert_chat(chat_dict)
    # 將發問者加入聊天室
    join_room(room_id)
    # emit('room_msg', {'room': data['room'],'id':data['id'],'msg':'( has entered the room ... )'}, to=data['room'])

# # 使用者加入聊天室
# @socketio.on('join_room')
# def join_room(data):
#     print('# ---------- client emit join_room ...')
#     print(data)
#     # data : { '_id','user_id','incognito'}
#     chat_data.insert_member(data)
#     join_room(data['_id'])

@socketio.on('send_message')
def send_message(data):
    print('# ---------- client emit sent_message ...')
    print(data)
    # 如果該client有在
    if data['_id'] in rooms():   
        # data : { '_id','user_id','time','type','content'}
        chat_data.insert_message(data)
        emit('received_message', data, to=data['_id'])
    else:
        emit('received_message',
             {
                 '_id':data['user_id'],
                 'user_id':'system',
                 'time':datetime.now().replace(microsecond=0),
                 'type':'string',
                 'content':'Client isn\'t in room ' + data['_id'] + ', can\'t send messages.'},to=data['user_id'])

# 關閉聊天室(不刪除紀錄)
@socketio.on('close_chat')
def close_chat(data):
    print('# ---------- client emit remove_chat ...')
    print(data)
    # 如果該room id有在client的room中
    if data['_id'] in rooms():   
        # data : { '_id','user_id','time','type','content'}
        close_room(data['_id'])
    else:
        emit('received_message',
             {
                 '_id':data['user_id'],
                 'user_id':'system',
                 'time':datetime.now().replace(microsecond=0),
                 'type':'string',
                 'content':'Client isn\'t in room ' + data['_id'] + ', can\'t close the chat.'},to=data['user_id'])
    