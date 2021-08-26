/* ============== socket.io測試 ============ */
const socket = io('https://soselab.asuscomm.com:55002');
var room_number;
$(document).ready(function() {
    socket.on('connect', function(msg) {
      console.log('connect response : ' + msg);
    })

    socket.on('room_msg', function(data) {
      console.log('room_msg : ' + data);
      document.getElementById("messages").innerHTML += '<li class="list-group-item">' + data['msg'] +'</li>';
      $("#user_input").val("");
   });
   console.log(socket.id);
   set_room();
});
function set_room(){
    room_number = window.prompt('Room number');
    console.log('current room : ' + room_number);
    join_room(room_number);
}

function change_room(){
    leave_room(room_number);
    set_room();
}

function join_room(room){
    socket.emit('join_room' , {'id': socket.id,'room':room});
}

function leave_room(room){
    socket.emit('leave_room' , {'id': socket.id,'room':room});
}

function send_message(msg){
    socket.emit('send_msg' , {'id': socket.id,'room': room_number,'msg':msg});
}
