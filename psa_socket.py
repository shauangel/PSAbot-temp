from flask_socketio import emit, join_room, leave_room
from main import socketio


print('----------socket-----------')
@socketio.on('connect')
def test_connect():
    print('connected.')
    emit('connect', 'server says connected.')

@socketio.on('connect_event')
def connected_msg(msg):
    print(msg)
    emit('server_response', 'received :' + str(msg))