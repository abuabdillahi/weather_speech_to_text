# weather_speech_to_text
Speak to my laptop, get an sms with the weather back.

This project allows the user to speak to their computer asking for the weather in a particular town or city in England
and it will be sent to their phone via sms.

cities.py contains a list of all the towns and cities in England which I got from this website https://simple.wikipedia.org/wiki/List_of_cities_and_towns_in_England

record_audio.py is a script that prompts the user to record a message which lasts 5 seconds. This is where the request for 
the weather is given to the computer.

The .wav file is then sent to speech_to_text.py which uses the Google Cloud Speech api to transcribe it.

After the audio file has been transcribed, the name of the city or town in question is picked out and sent to a function
within weather.py which calls the Apixu weather api and gets the weather for the specified city.

The relevant weather information is then put into a string and passed through to the send_text.py script which uses the
Nexmo api to send a text to your phone.
