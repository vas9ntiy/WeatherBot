import pyowm
import telebot

owm = pyowm.OWM('a2670a32ff80866d9f793a529677bc8a')
bot=telebot.TeleBot("859881974:AAHpxo_KhHsRUerALVWKpOEpR8xWSNEGBOw")

@bot.message_handler(content_types=['text'])
def send_echo(message):
	observation = owm.weather_at_place( message.text )
	w = observation.get_weather()
	temp = w.get_temperature('celsius')['temp']

	answer = "In "+ message.text +" now " + w.get_detailed_status()+"\n"
	answer += "Temperature is around" + str(temp)+"\n\n"

	if temp <10:
		answer += "That is cold outside. Wear jacket"
	elif temp <20:
		answer += "The weather is pretty good"
	else :
		answer += "That is hot outside. Prepare..."
	bot.send_message(message.chat.id, answer)
	
bot.polling (none_stop =True)
