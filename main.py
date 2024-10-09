import requests
from dotenv import dotenv_values

dotenv = dotenv_values(".env")

api_key = dotenv["API_KEY"]

response = requests.get(f"https://api.aviationstack.com/v1/flights?access_key={api_key}")
data = response.json()["data"]

print("Active Flights:\n-------------------")
for x in data:
    if x["flight_status"] == "active":
        dep = x["departure"]["airport"]
        arr = x["arrival"]["airport"]
        name = x["airline"]["name"]
        print(f"Airline: {name}\nDeparture Airport: {dep}\nArrival Airport: {arr}\n-------------------")
