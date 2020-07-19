import tornado.ioloop
import tornado.web
import os
import tornado.websocket
import math
import time
from datetime import datetime, timedelta
import brickpi3
from prometheus_client import start_http_server, Gauge

BP = brickpi3.BrickPi3()

b = Gauge('battery', 'voltage battery')



class Robot(object):
        def __init__(self, name):
                self.name = name
                self.input_sensitivity = 50
                self.state_x = 'X_NEUTRAL'
                self.state_y = 'Y_NEUTRAL'
                self.old_state_x = 'X_NEUTRAL'
                self.old_state_y = 'Y_NEUTRAL'
                self.print_task = datetime.now() + timedelta(seconds=3)
        
        def forward(self):
                BP.set_motor_power(BP.PORT_B + BP.PORT_C, 50)

        def back(self):
                BP.set_motor_power(BP.PORT_B + BP.PORT_C, -50)

        def left(self):
                BP.set_motor_power(BP.PORT_B, -50)
                BP.set_motor_power(BP.PORT_C, 50)

        def right(self):
                BP.set_motor_power(BP.PORT_B, 50)
                BP.set_motor_power(BP.PORT_C, -50)
        
        def stop(self):
                BP.set_motor_power(BP.PORT_B + BP.PORT_C, 0)

        def update(self):
            current_time = datetime.now()

            if current_time > self.print_task:
                print("Battery voltage: %6.3f  9v voltage: %6.3f  5v voltage: %6.3f  3.3v voltage: %6.3f" % (BP.get_voltage_battery(), BP.get_voltage_9v(), BP.get_voltage_5v(), BP.get_voltage_3v3()))
                self.print_task = current_time + timedelta(seconds=3)
                b.set(BP.get_voltage_battery())
        
        def process_input(self, x, y):


            if math.fabs(x) > self.input_sensitivity:
                if x > 0.0:
                    self.state_x = 'X_RIGHT'
                if x < 0.0:
                    self.state_x = 'X_LEFT'
            else:
                self.state_x = 'X_NEUTRAL'

            if math.fabs(y) > self.input_sensitivity:
                if y > 0.0:
                    self.state_y = 'Y_DOWN'
                if y < 0.0:
                    self.state_y = 'Y_UP'
            else:
                self.state_y = 'Y_NEUTRAL'


            #print('x: {}, y: {}'.format(self.state_x, self.state_y))


            if self.old_state_x != self.state_x:
                print('X CHANGED: ' + self.state_x)
                self.old_state_x = self.state_x

                if self.state_x == 'X_LEFT':
                    self.left()

                if self.state_x == 'X_RIGHT':
                    self.right()
            
            if self.old_state_y != self.state_y:
                print('Y CHANGED: ' + self.state_y)
                self.old_state_y = self.state_y

                if self.state_y == 'Y_UP':
                    self.forward()

                if self.state_y == 'Y_DOWN':
                    self.back()

            if self.state_x == 'X_NEUTRAL' and self.state_y == 'Y_NEUTRAL':
                self.stop()

            self.update()






           



class Joystick(object):
        def __init__(self):
                pass

def parse_message(message):
        x_str, y_str = message.split()

        x = float(x_str)
        y = float(y_str)

        return x, y

r = Robot(name='prototype 1')

class EchoWebSocket(tornado.websocket.WebSocketHandler):
        def open(self):
                print("WebSocket opened")

        def on_message(self, message):

                #print(message)

                x, y = parse_message(message)

                #print(f"x: {x}, y: {y}", x, y)

                r.process_input(x, y)

                # print("client: " + message)
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
                        overflow        : hidden;
                        padding         : 0;
                        margin          : 0;
                        background-color: #BBB;
                }
                #info {
                        position        : absolute;
                        top             : 0px;
                        width           : 100%;
                        padding         : 5px;
                        text-align      : center;
                }
                #info a {
                        color           : #66F;
                        text-decoration : none;
                }
                #info a:hover {
                        text-decoration : underline;
                }
                #container {
                        width           : 100%;
                        height          : 100%;
                        overflow        : hidden;
                        padding         : 0;
                        margin          : 0;
                        -webkit-user-select     : none;
                        -moz-user-select        : none;
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
                        var ws = new WebSocket("ws://192.168.0.167:8080/websocket");
                        ws.onopen = function() {
                        };
                        ws.onmessage = function (evt) {
                        alert(evt.data);
                        };


                        console.log("touchscreen is", VirtualJoystick.touchScreenAvailable() ? "available" : "not available");
        
                        var joystick    = new VirtualJoystick({
                                container       : document.getElementById('container'),
                                mouseSupport    : true,
                        });
                        joystick.addEventListener('touchStart', function(){
                                console.log('down')
                        })
                        joystick.addEventListener('touchEnd', function(){
                                console.log('up')
                        })

                        setInterval(function(){
                                var outputEl    = document.getElementById('result');
                                outputEl.innerHTML      = '<b>Result:</b> '
                                        + ' dx:'+joystick.deltaX()
                                        + ' dy:'+joystick.deltaY()
                                        + (joystick.right()     ? ' right'      : '')
                                        + (joystick.up()        ? ' up'         : '')
                                        + (joystick.left()      ? ' left'       : '')
                                        + (joystick.down()      ? ' down'       : '')   
                                
                                ws.send(joystick.deltaX() + " " + joystick.deltaY());
                        }, 100);
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
    start_http_server(5000)
    app = make_app()
    app.listen(8080)
    tornado.ioloop.IOLoop.current().start()
