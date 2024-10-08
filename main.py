# step 1: import requests
import requests

# step 2: call api with given endpoint and key
response = requests.get("https://api.aviationstack.com/v1/flights?access_key=9b6a85505fed243b921626af0eb662bb")

# step 3: convert to dictionary and grab only the "data" value
data = response.json()["data"]

# step 4: loop through the flights and check which flights are active
print("Active Flights:\n-------------------")
for x in data:
    if x["flight_status"] == "active":
        dep = x["departure"]["airport"]
        arr = x["arrival"]["airport"]
        name = x["airline"]["name"]
        print(f"Airline: {name}\nDeparture Airport: {dep}\nArrival Airport: {arr}\n-------------------")


# step 5: if active, print the airline, date, departure airport and arrival airport