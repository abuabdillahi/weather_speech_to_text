from apixu.client import ApixuClient, ApixuException
api_key = '#######'
client = ApixuClient(api_key)


def get_weather(city):
	current = client.getCurrentWeather(q=city)

	temp = current['current']['temp_c']
	feel_temp = current['current']['feelslike_c']
	condition = current['current']['condition']['text']

	output = "The current condition in {} is {} with a temperature of {} degrees C and a real feel of {} degrees C.".format(city, condition.lower(), temp, feel_temp)
	print(output)
	return output