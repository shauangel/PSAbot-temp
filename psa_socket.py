from flask_socketio import SocketIO,emit, join_room, leave_room
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
# 傳送問題資訊並建立聊天室
@socketio.on('create_room')
def create_room(data):
    # data: {'question':'',tags:[],'asker':{'user_id':'','user_name':'','incognito':''}}
    print('# ---------- client emit join_room ...')
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
    chat_data.insert_chat(chat_dict)
    # 將發問者加入聊天室
    join_room(data['room'])
    # emit('room_msg', {'room': data['room'],'id':data['id'],'msg':'( has entered the room ... )'}, to=data['room'])
    
    