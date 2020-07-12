import tornado.ioloop
import tornado.web
import os
import tornado.websocket

class EchoWebSocket(tornado.websocket.WebSocketHandler):
	def open(self):
		print("WebSocket opened")

	def on_message(self, message):
		print("client: " + message)
		# self.write_message(u"You said: " + message)

	def on_close(self):
		print("WebSocket closed")


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("""
<html>
	<head>
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, user-scalable=no, minimum-scale=1.0, maximum-scale=1.0">
		
		<style>
		body {
			overflow	: hidden;
			padding		: 0;
			margin		: 0;
			background-color: #BBB;
		}
		#info {
			position	: absolute;
			top		: 0px;
			width		: 100%;
			padding		: 5px;
			text-align	: center;
		}
		#info a {
			color		: #66F;
			text-decoration	: none;
		}
		#info a:hover {
			text-decoration	: underline;
		}
		#container {
			width		: 100%;
			height		: 100%;
			overflow	: hidden;
			padding		: 0;
			margin		: 0;
			-webkit-user-select	: none;
			-moz-user-select	: none;
		}
		</style>
	</head>
	<body>
		<div id="container"></div>
		<div id="info">
			<a href="http://learningthreejs.com/blog/2011/12/26/let-s-make-a-3d-game-virtual-joystick/" target="_blank">VirtualJoystick.js</a>
			A library javascript to provide a virtual joystick on touchscreen.
			-
			inspired by this
			<a href="http://sebleedelisle.com/2011/04/multi-touch-game-controller-in-javascripthtml5-for-ipad/">post</a>
			from
			<a href="http://sebleedelisle.com/">seb.ly</a>
			<br/>
			Touch the screen and move
			-
			works with mouse too as debug
			<br/>
			<span id="result"></span>
		</div> 
		<script src="/js/virtualjoystick.js"></script>
		<script>
			var ws = new WebSocket("ws://172.27.192.240:8080/websocket");
			ws.onopen = function() {
			ws.send("Hello, world");
			};
			ws.onmessage = function (evt) {
			alert(evt.data);
			};


			console.log("touchscreen is", VirtualJoystick.touchScreenAvailable() ? "available" : "not available");
	
			var joystick	= new VirtualJoystick({
				container	: document.getElementById('container'),
				mouseSupport	: true,
			});
			joystick.addEventListener('touchStart', function(){
				console.log('down')
			})
			joystick.addEventListener('touchEnd', function(){
				console.log('up')
			})

			setInterval(function(){
				var outputEl	= document.getElementById('result');
				outputEl.innerHTML	= '<b>Result:</b> '
					+ ' dx:'+joystick.deltaX()
					+ ' dy:'+joystick.deltaY()
					+ (joystick.right()	? ' right'	: '')
					+ (joystick.up()	? ' up'		: '')
					+ (joystick.left()	? ' left'	: '')
					+ (joystick.down()	? ' down' 	: '')	
				
				ws.send(joystick.deltaX() + " " + joystick.deltaY());
			}, 1/30 * 1000);
		</script>
	</body>
</html>       
        """)

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r'/js/(.*)', tornado.web.StaticFileHandler, {'path': './static/js'}),
		(r'/websocket', EchoWebSocket)
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8080)
    tornado.ioloop.IOLoop.current().start()