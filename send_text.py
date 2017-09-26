import nexmo

client = nexmo.Client(key='#######', secret='#######')

def success_text(text):
	response = client.send_message({'from': 'YourWeather', 'to': '#your_number', 'text': text})

	response = response['messages'][0]

	if response['status'] == '0':
		print('Sent message', response['message-id'])
		print('Remaining balance is', response['remaining-balance'])
	else:
		print('Error:', response['error-text'])


def fail_text():
	response = client.send_message({'from': 'YourWeather', 'to': '#your_number', 'text': 'Your location is not currently supported.'})

	response = response['messages'][0]

	if response['status'] == '0':
		print('Sent message', response['message-id'])
		print('Remaining balance is', response['remaining-balance'])
	else:
		print('Error:', response['error-text'])
