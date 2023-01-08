import base64
import cv2 as cv
import numpy as np
import paho.mqtt.client as mqtt

MQTT_BROKER = "192.168.0.101"
MQTT_RECEIVE = "home/server"



# # The callback for when the client receives a CONNACK response from the server.
# def on_connect(client, userdata, flags, rc):
#     print("Connected with result code "+str(rc))

#     # Subscribing in on_connect() means that if we lose the connection and
#     # reconnect then subscriptions will be renewed.
#     client.subscribe(MQTT_RECEIVE)


# # The callback for when a PUBLISH message is received from the server.
# def on_message(client, userdata, msg):
#     global frame
#     # Decoding the message
#     img = base64.b64decode(msg.payload)
#     # converting into numpy array from buffer
#     npimg = np.frombuffer(img, dtype=np.uint8)
#     # Decode to Original Frame
#     frame = cv.imdecode(npimg, 1)

def on_connect(client, userdata, flags, rc):  # The callback for when 
    print("Connected with result code {0}".format(str(rc)))  
    # Print result of connection attempt client.subscribe("digitest/test1")  
    # Subscribe to the topic “digitest/test1”, receive any messages published on it


def on_message(client, userdata, msg):  # The callback for when a PUBLISH message is received from the server. 
    print("Message received-> " + msg.topic + " " + str(msg.payload))  # Print a received msg

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_BROKER)
client.loop_forever()
# Starting thread which will receive the frames
# client.loop_start()

# while True:
#     cv.imshow("Stream", frame)
#     if cv.waitKey(1) & 0xFF == ord('q'):
#         break

# Stop the Thread
# client.loop_stop()