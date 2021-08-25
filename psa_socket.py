from flask_socketio import SocketIO,emit, join_room, leave_room


print('----------import psa socket-----------')

socketio = SocketIO()
def init_socketio(app):
    print('---------- init psa socket-----------')
    socketio.init_app(app,cors_allowed_origins="*")
    
@socketio.on('connect')
def test_connect():
    emit('connect', 'server says connected.')

@socketio.on('connect_event')
def connected_msg(msg):
    print(msg)
    emit('server_response', 'received :' + str(msg))