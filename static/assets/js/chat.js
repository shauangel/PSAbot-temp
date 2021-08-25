/* ============== socket.io測試 ============ */
$(document).ready(function() {
    var socket = io.connect('https://soselab.asuscomm.com:55002')
  
    socket.on('connect', function(msg) {
      console.log('socket.on : ' + msg);
      socket.emit('connect_event', {data: 'js say connected!'});
    })
  
    socket.on('server_response', function(msg) {
        console.log('server_response : ' + typeof msg + ' ' + msg.data);
     });
  
    socket.on('room_msg', function(msg) {
      console.log('room_msg : ' + typeof msg + ' ' + msg.data);
   });
   
  });
  
  function join_room(){
    socket.emit('join_room' , {'id': socket.id});
  }
}