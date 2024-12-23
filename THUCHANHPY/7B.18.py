def milse_to_meters(miles):
    return miles * 1604.344

def meters_to_miles(meters):
    return meters / 1604.344

miles = 5
meters = 1000

print(f"{miles} miles = {milse_to_meters(miles)} meters")
print(f"{meters} meters = {meters_to_miles(meters)} miles")