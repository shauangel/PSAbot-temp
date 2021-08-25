/* ============== socket.io測試 ============ */
const socket = io('https://soselab.asuscomm.com:55002');
$(document).ready(function() {
    console.log('socket : ' + Object.getOwnPropertyNames(socket))
    socket.on('connect', function(msg) {
      console.log('socket.on : ' + msg);
      socket.emit('connect_event', {data: 'js say connected!'});
    })
  
    socket.on('server_response', function(msg) {
        console.log('server_response : ' + typeof msg + ' ' + msg.data);
     });
  
    socket.on('room_msg', function(msg) {
      console.log('room_msg : ' + msg);
   });
   
});
  
function join_room(){
    socket.emit('join_room' , {'id': socket.id,'room':'room01'});
    localStorage.setItem('room', 'room01');
}

function join_room2(){
    socket.emit('join_room' , {'id': socket.id,'room':'room02'});
    localStorage.setItem('room', 'room02');
}

function leave_room(){
    socket.emit('leave_room' , {'id': socket.id,'room':localStorage.getItem('room')});
}

function say_hi(){
    socket.emit('send_msg' , {'id': socket.id,'room': localStorage.getItem('room'),'msg':'hello~'});
}
