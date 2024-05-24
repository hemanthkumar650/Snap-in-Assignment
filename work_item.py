import requests

api_token = "eyJhbGciOiJSUzI1NiIsImlzcyI6Imh0dHBzOi8vYXV0aC10b2tlbi5kZXZyZXYuYWkvIiwia2lkIjoic3RzX2tpZF9yc2EiLCJ0eXAiOiJKV1QifQ.eyJhdWQiOlsiamFudXMiXSwiYXpwIjoiZG9uOmlkZW50aXR5OmR2cnYtdXMtMTpkZXZvLzFMRFdnRU5MNDQ6ZGV2dS8xIiwiZXhwIjoxODEwNDAwNTc0LCJodHRwOi8vZGV2cmV2LmFpL2F1dGgwX3VpZCI6ImRvbjppZGVudGl0eTpkdnJ2LXVzLTE6ZGV2by9zdXBlcjphdXRoMF91c2VyL2xpbmtlZGlufFNiTG1TM0ZYTXEiLCJodHRwOi8vZGV2cmV2LmFpL2F1dGgwX3VzZXJfaWQiOiJsaW5rZWRpbnxTYkxtUzNGWE1xIiwiaHR0cDovL2RldnJldi5haS9kZXZvX2RvbiI6ImRvbjppZGVudGl0eTpkdnJ2LXVzLTE6ZGV2by8xTERXZ0VOTDQ0IiwiaHR0cDovL2RldnJldi5haS9kZXZvaWQiOiJERVYtMUxEV2dFTkw0NCIsImh0dHA6Ly9kZXZyZXYuYWkvZGV2dWlkIjoiREVWVS0xIiwiaHR0cDovL2RldnJldi5haS9kaXNwbGF5bmFtZSI6ImhlbWFudGhrdW1hcnZzMjciLCJodHRwOi8vZGV2cmV2LmFpL2VtYWlsIjoiaGVtYW50aGt1bWFydnMyN0BnbWFpbC5jb20iLCJodHRwOi8vZGV2cmV2LmFpL2Z1bGxuYW1lIjoiSGVtYW50aCBLIiwiaHR0cDovL2RldnJldi5haS9pc192ZXJpZmllZCI6dHJ1ZSwiaHR0cDovL2RldnJldi5haS90b2tlbnR5cGUiOiJ1cm46ZGV2cmV2OnBhcmFtczpvYXV0aDp0b2tlbi10eXBlOnBhdCIsImlhdCI6MTcxNTc5MjU3NCwiaXNzIjoiaHR0cHM6Ly9hdXRoLXRva2VuLmRldnJldi5haS8iLCJqdGkiOiJkb246aWRlbnRpdHk6ZHZydi11cy0xOmRldm8vMUxEV2dFTkw0NDp0b2tlbi9iODcwcG1tNSIsIm9yZ19pZCI6Im9yZ19xOGF6R2R3SVhTN3NvOUh1Iiwic3ViIjoiZG9uOmlkZW50aXR5OmR2cnYtdXMtMTpkZXZvLzFMRFdnRU5MNDQ6ZGV2dS8xIn0.tZ2oc3w45btetmdaDnFzJo8AYajKnBeSLOSTzbX9MccwMs5qQ5QkpkbuRtTsQmkb9dMvi9P3MRbAbZ7Eu231vViR4LELRvBiWnDsJyx4wtWyXnVPqXAam-bkU9YIZa00sb7yGOdLl_Itf1dG-evuzpwCIUqApvjsXdOjXO6zavYT2K7aNnXlIGn1p_QSysEcyUWiajo8Yuwt9FcJlRpOZ1uCKZim_5LtIyGTU7OB5c8Ge4BxdKiavH7h1_NSzvHMRWZ664-YVYpECtAiJz4KBbDK03Z_Bz2oAFEB9_4IZsn7z5FYge8fmJ7BMSCHzdRifUZpCb_1Q48oUcfd3A0-dw"

applies_to_part = "product"

owned_by = ["Hemanthkumarvs27"]

title = "NEW PROJECT"

url = "https://api.devrev.ai/works.get"

artifact_data = {
    "type": "issue",
    "applies_to_part": applies_to_part,
    "owned_by": [
        {
        "type": "dev_user",
        "id": "Hemanth",
        "display_id": "Hemanthkumarvs27",
        "display_name": "Hemanthkumarvs27",
        "email": "hemanthkumarvs27@gmail.com",
        "full_name": "Hemanth K",
        "state": "active"   
        }
    ],
    "title": title
}

headers = {
    "Authorization": f"Bearer {api_token}",
    "Content-Type": "application/json"
}

response = requests.post(url,json=artifact_data, headers=headers)

if response.status_code == 200:
    data = response.json()
    artifact_id = data["id"]
    print(f"Artifact ID: {artifact_id}")
else:
    print(f"Failed to create artifact: {response.status_code}")
    print(response.text)
