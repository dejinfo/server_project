import pytest
import requests
import json


def test_update_server():
    url = "http://127.0.0.1:5000/update_asset"

    payload = json.dumps({
    
    "asset_id" : "1",
    "bmc_password" : "user1234",
    "asset_location" : "bangalore",
    "purpose" : "shell scripting"
    })
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("PUT", url, headers=headers, data=payload)
    print("respose",str(response.text))
    assert response.status_code == 200
    expected_data = {
    "message": "Asset updated successfully !!",
    "status": "200 OK"
}
    
    assert json.loads(response.text) == expected_data
    expected_message = "Asset updated successfully !!"
    actual_message = json.loads(response.text)["message"]
    assert expected_message == actual_message
    

test_update_server()