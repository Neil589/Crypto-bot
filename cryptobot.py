import requests
import time
bitcoin_api_url = 'https://api.coinmarketcap.com/v1/ticker/bitcoin/'
while 1 > 0:
	response = requests.get(bitcoin_api_url)
	response_json = response.json()
	if float(response_json[0]['price_usd']) > 8000:
		
		print('Bitcoin price has reached $8000!')
		break
	time.sleep(300)