# -*- coding: utf-8 -*-
"""
@author: Sumit
"""
import time
import requests
import json
url = "https://live-metal-prices.p.rapidapi.com/v1/latest/XAU,XAU_OPEN,XAU_CHANGE,XAU_CHANGEPERCENT,XAU_1K,XAU_2K,XAU_3K,XAU_4K,XAU_5K,XAU_6K,XAU_7K,XAU_8K,XAU_9K,XAU_10K,XAU_11K,XAU_12K,XAU_13K,XAU_14K,XAU_15K,XAU_16K,XAU_17K,XAU_18K,XAU_19K,XAU_20K,XAU_21K,XAU_22K,XAU_23K,XAU_24K,XAG,XAG_OPEN,XAG_CHANGE,XAG_CHANGEPERCENT,PA,PL/INR/GRAM"
headers = {
    'x-rapidapi-host': "live-metal-prices.p.rapidapi.com",
    'x-rapidapi-key': "bfdae54b56msh212bf101eecebc1p166afdjsna3072861f010"
    }
count = 1

# sleep delay in seconds 
sleepTime = 5


print("Starting posting data every " , sleepTime, " seconds")

#This loop will call api every sleepTime value. 
#Infinite loop indicates automatic trigger of api call.
while(True):
    # API Call
    print("API call number ", count)
    print("\n")
    response = requests.request("GET", url, headers=headers)
    response = json.loads(response.text)
    final_response = {"records": [{"key" : "recordKey" + str(count),"value": response}]}
    final_response = json.dumps(final_response)
    final_response = final_response.replace("\\","")
    headers = {
        'Content-Type': 'application/vnd.kafka.json.v2+json',
    }
    data = final_response
    #this statement is used to send data to the database.
    #We are port forwarding 8082 port from cluster to local machine.
    response = requests.post('http://localhost:8082/topics/rapid.data.api', headers=headers, data=data)
    count+=1
    time.sleep(sleepTime)