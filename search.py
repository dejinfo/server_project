from urllib import request
from flask_cors import CORS,cross_origin
import psycopg2
# from addserverFORM import app
from flask import Flask, request, jsonify, make_response
import requests                                   #importing the packages/modules
import psycopg2
# import INSERT   #inserting the database file
from datetime import date
# import data as data
# import regex     #it is used to show all the matched characters which are related to the searched one
from connect2db import *

date_today = date.today()

app = Flask(__name__)
CORS(app)

@app.route('/search', methods=['POST'])
def search():
    conn = connectDB()              #called the connectDB file to connect with the database

    conn.autocommit = True         #if you commit a database, it saves all the changes till that particular point

    if request.method == 'POST':  # using POST method to request the data
        cursor = conn.cursor()
        _json = request.json
        ID = _json["ID"] 
        print("_json")
        Creator=_json['Creator']


        cursor.execute('select * from server_request where ID = %s',(ID,) ) 

        serverData = cursor.fetchone()  # here crusor fetch that data and assign it with serverData

        if serverData is None:                     #if condition if that obj is null ,then it will retun 'no record found'
            return jsonify("No record found")
        else:
            #otherwise it will print the data wich contains the array of data related to that bmc_ip
            serverlist=[]
            for server in serverData :
               data=  {"id": serverData[0],"Creator":serverData[1],"start_date": serverData[2],
                       "end_date": serverData[3], "manufacture": serverData[4], "number_of_servers": serverData[6],
                       "operating_system": serverData[7],"cpu_model":serverData[15],"cpu_sockets": serverData[8],
                       "dimm_size":serverData[9],"dimm_capacity": serverData[10],"storage_vendor":serverData[16],
                    "storage_controller":serverData[11],"storage_capacity":serverData[12],"network_type":serverData[13],"network_speed":serverData[14],
                         "number_of_network_ports":serverData[18],"special_switching_needs":serverData[19] ,
                     "infraadmin_comments":serverData[20],"user_comments":serverData[21],"request":serverData[22]}
            serverlist.append(data)
        # print(serverData[6],"location ")
            # cursor.close()
        return jsonify(serverlist)

if __name__ == '__main__':
    # app.app_context()
    app.run(host="0.0.0.0", port=5000, debug=True)
    # anything chnged in here, will updated and reflected in web browser


