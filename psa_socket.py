from flask_socketio import emit, join_room, leave_room
from main import socketio


@socketio.on('connect')
def test_connect(data):
    print('received data: type: ' + type(data), 'content: ' + data )
    emit('my response', {'data': 'flask emit Connected'})


@socketio.on('client_msg')
def test_get_msg(data):
     print('received data: type: ' + type(data), 'content: ' + data )
     
@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')
    
    