from flask_socketio import emit, join_room, leave_room
from main import socketio


@socketio.on('connect_event')
def connected_msg(msg):
    print(msg)
    emit('server_response', {'data': 'server received :' + msg['data']})

# @socketio.on('client_event')
# def client_msg(msg):
    
    