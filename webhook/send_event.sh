#!/bin/sh
# Post one example event to your virtual HUB in AIRlert LIVE.
# FP gives you the webhook address and token for your virtual HUB; these are placeholders.
WEBHOOK_URL="https://example.invalid/your-virtual-hub-webhook"
TOKEN="your-token"

curl -sS -X POST "$WEBHOOK_URL" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"device":"AABBCCDDEEFF","state":"button_pressed","time":"2026-11-14T10:00:00Z"}'
