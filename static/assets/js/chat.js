/* ============== socket.io測試 ============ */
var socket = io('https://soselab.asuscomm.com:55002');
var room_number;
$(document).ready(function() {
    socket.on('connect', function(response) {
      console.log('connect response : ' + response);
      if(room_number == null) set_room();
    })

    socket.on('room_msg', function(response) {
      console.log('room_msg : ' + response);
      document.getElementById("messages").innerHTML += '<li class="list-group-item">' 
                                                        + '(Room ' +  response['room'] + ') '
                                                        + '<b>' + response['id'] + '</b> : '
                                                        +  response['msg'] +'</li>';
      $("#user_input").val("");
   });
});
function set_room(){
    room_number = window.prompt('Room number');
    console.log('current room : ' + room_number);
    join_room(room_number);
    document.getElementById("user_info").innerHTML = '<b>Socket id :</b> ' + socket.id + ' <b>Room :</b> ' + room_number;
}

function change_room(){
    set_room();
    leave_room(room_number);
}

function join_room(room){
    socket.emit('join_room' , {'id': socket.id,'room':room});
}

function leave_room(room){
    socket.emit('leave_room' , {'id': socket.id,'room':room});
    document.getElementById("messages").innerHTML = ""
}

function send_message(){
    socket.emit('send_msg' , {'id': socket.id,'room': room_number,'msg': $("#user_input").val()});
}
