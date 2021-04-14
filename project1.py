#!/usr/bin/env python3

import os
import requests
from typing import Optional
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException

app = FastAPI()

#Welcome page
@app.get("/")  # zone apex
def read_root():
    return_string = "Welcome!"
    return return_string

#converts temperature from Celsius to Fahrenheit
@app.get("/convert_c_to_f/{celsius}")
def convert_temp(celsius: int,):
    if (type(celsius) != int): #makes sure the user entered a number
        raise HTTPException(status_code=400, detail="Please enter a number")
    return {celsius*9/5 +32}

#converts the distance from km to miles
@app.get("/convert_km_to_miles/{km}")
def km_to_miles(km: int):
    if (type(km) != int): #makes sure the user entered a number
        raise HTTPException(status_code=400, detail="Please enter a number") #makes sure the user entered a number
    return { km/1.609344 }

#return the city name associated with this zipcode
@app.get("/city/{zipcode}")
def return_city(zipcode: str):
    if( len(zipcode) != 5 ):
        raise HTTPException(status_code=400, detail="Please enter a 5 zipcode")
    url = "https://www.zipcodeapi.com/rest/klUv7wJSEB0aiLsyPFPBlxyBjWG1txs2dLapNSlY1YJBFXFcaqMWoEqPutAX2dcF/info.json/" + zipcode + "/degrees"
    response = requests.get(url)
    city = response.json()["city"]
    return city

#return the distance between two zipcodes
@app.get("/distance/{zipcode1}/{zipcode2}")
def return_distance(zipcode1: str, zipcode2: str):
    if( (len(zipcode1) != 5) or (len(zipcode2) != 5) ):
        raise HTTPException(status_code=400, detail="Please enter a 5 zipcode")
    url = "https://www.zipcodeapi.com/rest/klUv7wJSEB0aiLsyPFPBlxyBjWG1txs2dLapNSlY1YJBFXFcaqMWoEqPutAX2dcF/distance.json/" + zipcode1 + "/" + zipcode2 + "/mile"
    response = requests.get(url)
    distance = response.json()["distance"]
    return distance

#return the the area codes of this zipcode
@app.get("/areacodes/{zipcode}")
def return_areacodes(zipcode: str):
    if( len(zipcode) != 5 ):
        raise HTTPException(status_code=400, detail="Please enter a 5 zipcode")
    url = "https://www.zipcodeapi.com/rest/klUv7wJSEB0aiLsyPFPBlxyBjWG1txs2dLapNSlY1YJBFXFcaqMWoEqPutAX2dcF/info.json/" + zipcode + "/degrees"
    response = requests.get(url)
    areacodes = response.json()["area_codes"]
    return areacodes
