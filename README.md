# AIRlert integration examples

Examples for integrators who want to use **AIRlert sensors** from [Frequency Precision Ltd](https://frequencyprecision.com) in their own systems: hospitals, care clinics, homes and bespoke projects.

AIRlert sensors are pneumatic mats designed and made in the UK. They sit under any mattress, including air mattresses, and detect bed exit, bed occupancy and tonic-clonic convulsions. Chair and floor sensors, call buttons and long-range POCSAG pagers complete the range. AIRlert is assistive technology, not a medical device.

This repository holds examples and documentation only. It contains no AIRlert portal code, keys, passwords or customer data: every value here is a placeholder.

## Three ways to connect

| Route | What you get | Folder |
| --- | --- | --- |
| **Transmitter Shield into your own system** | AIRlert sensors onto long-range POCSAG paging, received by your gateway or pager system. Shields for more protocols will follow. | [`transmitter-shield/`](transmitter-shield/) |
| **AIRlert HUB as your gateway** | Alerts to phones, pagers, IP call systems and alarm centres, over Wi-Fi and Bluetooth; works on a local network with no internet. | (ask FP for the HUB guide) |
| **AIRlert LIVE platform** | Your devices' events in, and AIRlert alerts out to your own system, through an API and a two-way API. MQTT for Zigbee and other systems is being set up now. | [`mqtt/`](mqtt/), [`webhook/`](webhook/), [`alerts-out/`](alerts-out/) |

Platform connections that need development are quoted and paid up front.

## Examples

- [`mqtt/publish_event.py`](mqtt/publish_event.py): send a device's events to AIRlert LIVE through FP's MQTT broker (TLS, a login per device issued by FP).
- [`webhook/send_event.sh`](webhook/send_event.sh): post an event from a device or gateway to a virtual HUB.
- [`alerts-out/receive_alerts.py`](alerts-out/receive_alerts.py): receive AIRlert alerts in your own system.
- [`home-assistant/automations.yaml`](home-assistant/automations.yaml): react to AIRlert bed exit and convulsion alerts in Home Assistant.

## Getting started

1. Email **contact@frequencyprecision.com** with your project: the site, the sensors you need, and how you want to connect.
2. FP issues your credentials (a virtual HUB, an MQTT login or a webhook address) and trade prices.
3. Try the examples with your own values in place of the placeholders.

Frequency Precision Ltd, The Old Cider Works, Abbotskerswell, Newton Abbot, Devon, TQ12 5NF, United Kingdom. ISO 9001:2015.

## Licence

The example code in this repository is released under the MIT licence (see [LICENSE](LICENSE)). AIRlert and Frequency Precision are trade marks of Frequency Precision Ltd; AIRlert sensors are patented.
