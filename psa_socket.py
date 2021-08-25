from flask_socketio import SocketIO,emit, join_room, leave_room
from flask import jsonify


print('----------import psa socket-----------')

socketio = SocketIO()
def init_socketio(app):
    print('---------- init psa socket-----------')
    socketio.init_app(app,cors_allowed_origins="*")
    
@socketio.on('connect')
def test_connect():
    print('---------- connected -----------')
    emit('connect', 'server says connected.')

@socketio.on('connect_event')
def connected_msg(msg):
    print('---------- connect_event -----------')
    print(type(msg))
    print(msg)
    emit('server_response',msg)
    
@socketio.on('join_room')
def join_chat_room(data):
    print('---------- join_room -----------')
    print(data)
    join_room(data['room'])
    emit('room_msg', data['id'] + ' has entered ' + data['room'], to=data['room'])
    
@socketio.on('leave_room')
def leave_chat_room(data):
    print('---------- leave_room -----------')
    print(data)
    leave_room(data['room'])
    emit('room_msg', data['id'] + ' has left ' + data['room'], to=data['room'])

@socketio.on('send_msg')
def send_msg(data):
    print('---------- send_msg -----------')
    print(data)
    emit('room_msg', '('+ data['room'] + ') ' + data['id'] + ' : ' + data['msg'], to=data['room'])


    
    