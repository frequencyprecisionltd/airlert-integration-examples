"""Send one example event from your device to AIRlert LIVE over MQTT (TLS).

Placeholders only: FP issues the login, and confirms the topic and message format for your device.
"""
import json
import os
import ssl
import time

import paho.mqtt.client as mqtt

BROKER = "mqtt.airlert.co.uk"
PORT = 8883
DEVICE_ID = "AABBCCDDEEFF"            # your device's own ID, e.g. its MAC address
TOPIC = f"/YourProduct/{DEVICE_ID}/event"

client = mqtt.Client(client_id=f"yourproduct-{DEVICE_ID}")
client.username_pw_set(os.environ["AIRLERT_MQTT_USER"], os.environ["AIRLERT_MQTT_PASS"])
client.tls_set(cert_reqs=ssl.CERT_REQUIRED)
client.connect(BROKER, PORT, keepalive=60)
client.loop_start()

event = {"device": DEVICE_ID, "state": "out_of_bed", "time": int(time.time())}
info = client.publish(TOPIC, json.dumps(event), qos=1)
info.wait_for_publish()
print("sent", event)

client.loop_stop()
client.disconnect()
