from flask_socketio import emit, join_room, leave_room
from main import socketio


@socketio.on('connect', namespace='/test')
def test_connect(data):
    print('received data: \ntype: ' + type(data), '\ncontent: ' + data )
    emit('my response', {'data': 'Connected'})

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')
    
    