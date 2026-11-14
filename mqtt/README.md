# MQTT: your device's events into AIRlert LIVE

FP's broker takes MQTT over TLS on port 8883. Each device gets its own login from FP, linked to a virtual HUB in AIRlert LIVE. Once linked, changes of state (for example fall, in bed, out of bed) run through the same alert rules as a physical AIRlert HUB.

MQTT for third-party systems is being set up now: ask FP for a login before testing.

```bash
pip install paho-mqtt
export AIRLERT_MQTT_USER="your-device-login"
export AIRLERT_MQTT_PASS="your-device-password"
python publish_event.py
```

Use a topic that starts with your product name and the device's own ID (for example its MAC address), so AIRlert LIVE can tell your devices apart. FP will confirm the exact topic and message format for your device.
