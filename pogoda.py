import pyowm

owm = pyowm.OWM('a2670a32ff80866d9f793a529677bc8a',language="en")

place=input("Enter city: ")

observation = owm.weather_at_place(place)
w = observation.get_weather()

temp = w.get_temperature('celsius')["temp"]

print("In "+place+" now " + w.get_detailed_status())
print("Temperature is around" + str(temp))

if temp<10:
	print("That is cold outside")
elif temp<20:
	print("That is pretty fine")
else :
	print("That's hot oudside")