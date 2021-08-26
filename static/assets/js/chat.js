/* ============== socket.io測試 ============ */
var socket = io('https://soselab.asuscomm.com:55002');
var room_number = [];
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
    room_number.push(window.prompt('Room number'));
    join_room(room_number);
    refresh_info();
}


function join_room(room){
    socket.emit('join_room' , {'id': socket.id,'room':room});
}

function leave_room(room){
    var room_to_leave = window.prompt('Room number')
    socket.emit('leave_room' , {'id': socket.id,'room':room_to_leave});
    room_number.forEach(function(item, index, arr) {
        if(item === room_to_leave) {
            arr.splice(index, 1);
        }
    });
    refresh_info();
}

function refresh_info(){
    document.getElementById("user_info").innerHTML = '<p><strong>Socket id :</strong> ' + socket.id + '<br><strong>Room :</strong> ' + room_number + '</p>';
}
function send_message(){
    socket.emit('send_msg' , {'id': socket.id,'room': room_number,'msg': $("#user_input").val()});
}
