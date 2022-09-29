import pytest
import requests
import json


def test_server_request():
    url = "http://127.0.0.1:5000/server_request"

    payload = json.dumps({
    "ID": "1",
    "Creator": "vibha",
    "Start_Date": "2022-07-01 5:00:00",
    "End_Date": "2022-08-01 00:00:00",
    "Manufacturer": "hp",
    "Number_Of_Servers": 6,
    "Cpu_model": "Intel(R)Core(TM)i7-4790CPU@3.60GHz",
    "CPU_Sockets": 2,
    "DIMM_Size": "64GB",
    "DIMM_Quantity": 4,
    "OS_Vendor": "samsung",
    "OS_Controller": "SAS",
    "OS_Capacity": "1.5TB",
    "Disk_Vendor": "sandisk",
    "Disk_Controller": "SATA",
    "Disk_Capacity": "1.5TB",
    "Network_Type": True,
    "Network_speed": "1GB",
    "Network_ports": 2,
    "Special_Switching_Needs": "no",
    "Infraadmin_Comments": "new server added",
    "User_Comments": "add server",
    })
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("PUT", url, headers=headers, data=payload)
    print("respose",str(response.text))
    assert response.status_code == 200
    expected_data = {
    "message": "Server Request updated successfully !!",
    "status": "200 OK"
    }
    
    assert json.loads(response.text) == expected_data
    expected_message = "Server Request updated successfully !!"
    actual_message = json.loads(response.text)["message"]
    assert expected_message == actual_message
    

test_server_request()