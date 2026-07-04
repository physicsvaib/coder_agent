import os
import requests
import json

response = requests.post(
  "http://localhost:1234/api/v1/chat",
  headers={
    "Content-Type": "application/json"
  },
  json={
    "model": "essentialai/rnj-1",
    "input": "Write a short haiku about sunrise."
  }
)

data = response.json()

return data["output"][0]["content"]

