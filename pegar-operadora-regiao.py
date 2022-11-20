import phonenumbers
from phonenumbers import geocoder, carrier

phoneNumber = phonenumbers.parse("+5511963062767")

Carrier = carrier.name_for_number(phoneNumber, "pt-br")

Region = geocoder.description_for_number(phoneNumber, "pt-br")

print("A operadora e: "+ Carrier)
print("O estado e: " + Region)