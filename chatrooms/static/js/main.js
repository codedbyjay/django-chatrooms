(function(){
    $(document).ready(function(){
        // Setup socket
        console.log("Setting up socket");
        var wsUrl = 'ws://' + window.location.hostname + ':' + window.location.port;
        console.log("Connecting to: ", wsUrl);
        var ws = new WebSocket(wsUrl);
        ws.onmessage = function(message){
            console.log("Got message: ", message);
            var data = JSON.parse(message.data);
            var user = data.user;
            var text = data.text;
            var div = $("<div class='chat-message'><span class='user'>" + user + "</span><span>" + text + "</span></div>");
            $(".chat-messages").append(div);
        };

        $(".send-message").click(function(){
            console.log("Sending message");
            var message = $(".new-message").val();
            ws.send(message);
            $(".new-message").val("");
            $(".new-message").focus();
        })
    });
})();