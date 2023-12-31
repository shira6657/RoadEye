import requests
from pprint import pprint
#258dc07d366deaf974103c79726b3803f83c2ce2
#ee39ff412322e1c2a298caf2327b71e10cf50ad0
def detect_Num(img):
    regions = ['mx', 'us-ca'] # Change to your country
    with open(img, 'rb') as fp:
        try:
            response =   requests.post(
                'https://api.platerecognizer.com/v1/plate-reader/',
                data=dict(regions=regions, mmc=True),  # Optional
                files=dict(upload=fp),
                headers={'Authorization': 'Token 30e0ef5cf7b8fdeec83993550f95fc5970ccbc50'})
        except :
            print("err")
            return []
        
    my_object =  response.json()
    pprint(my_object)
    cars = []
    for result in my_object['results']:
        car = {
            'pixels': result['vehicle']['box'],
            'plate': result['plate'],
            'vehicle':vehicle_type(result['vehicle']['type'])
        }
        cars.append(car)
    return cars


def vehicle_type(typ):
    vehic = {'Big Truck':"משאית", 'Bus':"אוטובוס", 'Motorcycle':"אופנוע", 'Pickup Truck':"טנדר", 'Sedan':"רכב", 'SUV':"רכב שטח", 'Van':"ואן",'Unknown':"לא ידוע"}
    if not typ:
        return "לא ידוע"
    return vehic[typ]



#c Truck, Bus, Motorcycle, Pickup Truck, Sedan, SUV, Van, Unknown