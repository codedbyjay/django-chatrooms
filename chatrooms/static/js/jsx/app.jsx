import { Router, Route, Link, browserHistory } from 'react-router'

var ChatMessage = React.createClass({
    render: function(){
        return (
            <div className="chat-message">
                {this.props.user}:
                {this.props.text}
            </div>
        );
    }
});

var ChatMessages = React.createClass({
    render: function(){
        var messageNodes = this.props.messages.map(function(message){
            return (
                <ChatMessage user={message.user} text={message.text} />
            )
        });
        return (
            <div className="chat-messages">
                {messageNodes}
            </div>
        )
    }
});

var sampleMessages = [
    {user: "jay", text: "blah"},
    {user: "jon", text: "blah"},
];

var ChatRoom = React.createClass({
    render: function(){
        return (
            <div className="chatroom">
            Chatroom goes here
            <ChatMessages messages={sampleMessages} />
            </div>
        );
    }
});

var App = React.createClass({
    render: function(){
        return (
            <div>
                <h1>Main window</h1>
                <div>
                    Options to create a room go here
                </div>
            </div>
        )
    }
});

ReactDOM.render((
    <Router history={browserHistory}>
        <Route path="/" component="{ChatRoom}" />
    </Router>
), document.getElementById("container"))

// ReactDOM.render(
//     <App />,
//     document.getElementById("container")
// )