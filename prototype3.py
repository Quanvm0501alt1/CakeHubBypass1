# Cake bypass Python scripts
# import requests
import urllib.request
import json
import base64
class Error(Exception):
	"""docstring for Error"""
	pass
class NoHWIDOrTokenKey(Error):
	pass

def is_developer(dev_key):
	owner_dev_key = "aGlwaG9wbmV2ZXJkaWU="
	conel_dev_key = "c3RpY2t4bmV2ZXJkaWU="
	api = 0
	is_developer = False
	dev_mode = 0
	dev_key = dev_key.lower()
	if dev_key == base64.b64decode(owner_dev_key).decode('utf-8'):
		is_developer = True
		print("You are a developer now!")
		dev_mode = 1
	elif dev_key == base64.b64decode(conel_dev_key).decode('utf-8'):
		is_developer = True
		print("You are a developer now!")
		dev_mode = 2
	return {"is_developer": is_developer, "dev_mode": dev_mode}

def str_return_mode(api):
	if api == 0:
		print("""
		1: Fluxus
		2: Adlink
		3: RelzHub
		0: Change API
		""")
	elif api == 1:
		print("""
		1: Fluxus
		2: Delta (fixing by dev) (can test)
		3: Hydrogen (fixing by dev) (can test)
		4: Linkvertise
		5: Arceus X
		6: CodeX
		7: Vega X
		0: Change API
		""")
	mode = int(input("Type mode: "))
	if mode == 0:
		return 0
	else:
		return mode


def change_apis(is_developer):
	print("""
	0: Duck API (DEFAULT) 
	1: StickX API
	2: Bypass.vip API (Dev)
	""")
	api = int(input("Type API: "))
	if api == 3:
		if is_developer == False:
			print("You are not a developer!")
		else:
			return api
	else:
		return api

def duck(mode, link):
	if mode == 1:
		url = f'https://duckcute-zeta.vercel.app/fluxus?link={link}'
		with urllib.request.urlopen(url) as response:
			html = response.read()
			# Decode bytes to string and remove the leading 'b' character
			dick = html.decode('utf-8').replace('b', '', 1)
			dictionary = json.loads(dick)
			print("Key:",dictionary['key'])
	elif mode == 2:
		url = f"https://duckcute-zeta.vercel.app/adlink?link={link}"
		with urllib.request.urlopen(url) as response:
			html = response.read()
			# Decode bytes to string and remove the leading 'b' character
			dick = html.decode('utf-8').replace('b', '', 1)
			print("Result:",dictionary['key'])
	elif mode == 3:
		url = f"https://duckcute-zeta.vercel.app/relzhub?link={link}"
		with urllib.request.urlopen(url) as response:
			html = response.read()
			# Decode bytes to string and remove the leading 'b' character
			dick = html.decode('utf-8').replace('b', '', 1)
			print("Key:",dictionary['key'])

def stickx(mode, link):
	if mode == 1:
		url = f'https://stickx.top/api-fluxus/?hwid={link}&api_key=E99l9NOctud3vmu6bPne'
		with urllib.request.urlopen(url) as response:
			html = response.read()
			# Decode bytes to string and remove the leading 'b' character
			dick = html.decode('utf-8').replace('b', '', 1)
			dictionary = json.loads(dick)
			print("Key:",dictionary['key'])
	elif mode == 2:
		url = f"https://stickx.top/api-delta/?hwid={link}&api_key=tUnAZj3sS74DJo9BUb8tshpVhpLJLA"
		with urllib.request.urlopen(url) as response:
			html = response.read()
			# Decode bytes to string and remove the leading 'b' character
			dick = html.decode('utf-8').replace('b', '', 1)
			print("Key:",dictionary['key'])
	elif mode == 3:
		url = f"https://stickx.top/api-hydrogen/?hwid={link}&api_key=E99l9NOctud3vmu6bPne"
		with urllib.request.urlopen(url) as response:
			html = response.read()
			# Decode bytes to string and remove the leading 'b' character
			dick = html.decode('utf-8').replace('b', '', 1)
			print("Key:",dictionary['key'])
	elif mode == 4:
		url = f"https://stickx.top/api-linkvertise/?link={link}&api_key=E99l9NOctud3vmu6bPne"
		with urllib.request.urlopen(url) as response:
			html = response.read()
			# Decode bytes to string and remove the leading 'b' character
			dick = html.decode('utf-8').replace('b', '', 1)
			print("Key:",dictionary['key'])
	elif mode == 5:
		url = f"https://stickx.top/api-arceusx/?hwid={link}&api_key=tUnAZj3sS74DJo9BUb8tshpVhpLJLA"
		with urllib.request.urlopen(url) as response:
			html = response.read()
			# Decode bytes to string and remove the leading 'b' character
			dick = html.decode('utf-8').replace('b', '', 1)
			print("Key:",dictionary['key'])
	elif mode == 6:
		url = f"https://stickx.top/api-codex/?token={link}&api_key=tUnAZj3sS74DJo9BUb8tshpVhpLJLA"
		with urllib.request.urlopen(url) as response:
			html = response.read()
			# Decode bytes to string and remove the leading 'b' character
			dick = html.decode('utf-8').replace('b', '', 1)
			print("Key:",dictionary['key'])
	elif mode == 7:
		url = f"https://stickx.top/api-vegax/?hwid={link}&api_key=tUnAZj3sS74DJo9BUb8tshpVhpLJLA"
		with urllib.request.urlopen(url) as response:
			html = response.read()
			# Decode bytes to string and remove the leading 'b' character
			dick = html.decode('utf-8').replace('b', '', 1)
			print("Key:",dictionary['key'])

def main():
	dev_dict = is_developer(input("Type your developer key: "))
	api = change_apis(dev_dict["is_developer"])
	while True:
		mode = str_return_mode(api)
		if mode == 0:
			api = change_apis(dev_dict["is_developer"])
		if mode != 0:
			break
	try:
		link = input("Type link: ")
		if len(link) == 0:
			raise NoHWIDOrTokenKey
	except NoHWIDOrTokenKey:
		print("You MUST input HWID or Token key!")
	except Exception as e:
		print(e)
	else:
		if api == 0:
			duck(mode, link)


	# finally:
		# pass
if __name__ == '__main__':
	main()