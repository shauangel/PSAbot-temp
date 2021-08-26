from flask_socketio import SocketIO,emit, join_room, leave_room
from flask import jsonify


print('----------import psa_socket-----------')

socketio = SocketIO()
def init_socketio(app):
    print('---------- init socket_io -----------')
    socketio.init_app(app,cors_allowed_origins="*")
    
@socketio.on('connect')
def test_connect():
    print('---------- connected -----------')
    emit('connect', 'server says connected.')

   
@socketio.on('join_room')
def join_chat_room(data):
    print('---------- client join_room -----------')
    print(data)
    print(data)
    join_room(data['room'])
    emit('room_msg', {
        'msg':
            '('+ data['room'] + ') ' + data['id'] + ' has entered room ' + data['room']}, to=data['room'])
    
@socketio.on('leave_room')
def leave_chat_room(data):
    print('---------- client leave_room -----------')
    print(data)
    leave_room(data['room'])
    emit('room_msg', {
        'msg':
            '('+ data['room'] + ') ' + data['id'] + ' has left room ' + data['room']}, to=data['room'])

@socketio.on('send_msg')
def send_msg(data):
    print('---------- client send_msg -----------')
    print(data)
    emit('room_msg', '('+ data['room'] + ') ' + data['id'] + ' : ' + data['msg'], to=data['room'])


    
    