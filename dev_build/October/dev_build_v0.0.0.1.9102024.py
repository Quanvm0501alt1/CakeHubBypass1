# Cake bypass Python scripts
# import requests
import urllib.request
import json, base64, os

class Error(Exception):
	"""docstring for Error"""
	pass
class NoHWIDOrTokenKey(Error):
	pass

def is_developer(dev_key):
	owner_dev_key = "aGlwaG9wbmV2ZXJkaWU="
	conel_dev_key = "c3RpY2t4bmV2ZXJkaWU="
	bypassvip_dev_key = "YnlwYXNzLnZpcG5ldmVyZGll"
	zaneru_dev_key = "emFuZXJ1b2ZmaWNpYWxuZXZlcmRpZQ=="
	prince_api_key = "cHJpbmNlYXBpbmV2ZXJkaWU="
	cryzo_api_key = "Y3J5em9uZXZlcmRpZQ=="
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
	elif dev_key == base64.b64decode(bypassvip_dev_key).decode('utf-8'):
		is_developer = True
		print("You are a developer now!")
		dev_mode = 3
	elif dev_key == base64.b64decode(zaneru_dev_key).decode('utf-8'):
		is_developer = True
		print("You are a developer now!")
		dev_mode = 4
	elif dev_key == base64.b64decode(prince_api_key).decode('utf-8'):
		is_developer = True
		print("You are a developer now!")
		dev_mode = 5
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
	elif api == 2:
		print("""
		1: Adlink
		0: Change API""")
	elif api == 3:
		print("""
		1: Fluxus
		2: Relz Hub
		3: Delta
		0: Change API""")
	elif api == 4:
		print("""
		1: Fluxus
		2: CodeX
		3: Delta
		4: Work.ink
		5: Rekonise
		6: Mediafire
		7: Arceus X
		8: Linkvertise
		0: Change API""")
	elif api == 5:
		print("""
		1: Bypass Link
		0: Change API""")
	elif api == 6:
		print("""
		1: Bypass Roblox link
		2: Adlink
		0: Change API""")
	elif api == 7:
		print("""
		1: Fluxus
		2: MBoost
		3: PasteDrop
		4: MediaFire
		5: RelzHub
		6: Delta
		0: Change API""")
	elif api == 8:
		print("""
		1: Bypass all Links (Except ArceusX)
		2: ArceusX
		0: Change API""")
	elif api == 9:
		print("""
		1: Fluxus
		2: Delta
		0: Change API""")
	elif api == 10:
		print("""
		1: Fluxus
		2: CodeX
		0: Change API""")
	elif api == 11:
		print("""
		1: All links
		0: Change API""")
	mode = int(input("Type mode: "))
	wrong_mode = False
	if mode == 0:
		return 0
	else:
		if (api == 0 and mode not in [1,2,3]):
			wrong_mode = True
		elif (api == 1 and mode not in [1,2,3,4,5,6,7]):
			wrong_mode = True
		elif (api == 2 and mode not in [1]):
			wrong_mode = True
		elif (api == 3 and mode not in [1,2,3]):
			wrong_mode = True
		elif (api == 4 and mode not in [1,2,3,4,5,6,7]):
			wrong_mode = True
		elif (api == 5 and mode not in [1,2,3,4,5,6,7]):
			wrong_mode = True
		elif (api == 6 and mode not in [1,2]):
			wrong_mode = True
		elif (api == 7 and mode not in [1,2,3,4,5,6]):
			wrong_mode = True
		elif (api == 8 and mode not in [1,2]):
			wrong_mode = True
		elif (api == 9 and mode not in [1,2]):
			wrong_mode = True
		elif (api == 10 and api not in [1,2]):
			wrong_mode = True


		if wrong_mode == True:
			print("Opps! Invaild Mode!")
		else:
			return mode


def change_apis(is_developer):
	print("""
	0: Duck API (Recommmend!) 
	1: StickX API (Dev Fixing)
	2: Bypass.vip API
	3: Zaneru Bypass API
	4: Prince API
	5: Cryzo
	6: Nexus API (NEW)
	7: Demon
	8: Triple Scripts Server (TSS)
	9: XTR Bypass
	10: HaHa bypass (Comming Soon)
	11: Kobayashi Bypass
	""")
	api = int(input("Type API: "))
	if api == 10 and is_developer == False:
		print("You are not a developer!")
		return
	if api not in [0,1,2,3,4,5,6,7,8,9,10]:
		print("Opps! Invaild API!")
		return
	else:
		return api

def duck(mode, link):
	if mode == 1:
		url = f"https://ducktestflu.vercel.app/api/fluxus?url={link}"
		with urllib.request.urlopen(url) as response:
			html = response.read()
			# Decode bytes to string and remove the leading 'b' character
			dick = html.decode('utf-8').replace('b', '', 1)
			dictionary = json.loads(dick)
			return dictionary['key']
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
			return dictionary['key']

def stickx(mode, link):
	if mode == 1:
		url = f'https://stickx.top/api-fluxus/?hwid={link}&api_key=E99l9NOctud3vmu6bPne'
		with urllib.request.urlopen(url) as response:
			html = response.read()
			# Decode bytes to string and remove the leading 'b' character
			dick = html.decode('utf-8').replace('b', '', 1)
			dictionary = json.loads(dick)
			return dictionary['key']
	elif mode == 2:
		url = f"https://stickx.top/api-delta/?hwid={link}&api_key=tUnAZj3sS74DJo9BUb8tshpVhpLJLA"
		with urllib.request.urlopen(url) as response:
			html = response.read()
			# Decode bytes to string and remove the leading 'b' character
			dick = html.decode('utf-8').replace('b', '', 1)
			return dictionary['key']
	elif mode == 3:
		url = f"https://stickx.top/api-hydrogen/?hwid={link}&api_key=E99l9NOctud3vmu6bPne"
		with urllib.request.urlopen(url) as response:
			html = response.read()
			# Decode bytes to string and remove the leading 'b' character
			dick = html.decode('utf-8').replace('b', '', 1)
			return dictionary['key']
	elif mode == 4:
		url = f"https://stickx.top/api-linkvertise/?link={link}&api_key=E99l9NOctud3vmu6bPne"
		with urllib.request.urlopen(url) as response:
			html = response.read()
			# Decode bytes to string and remove the leading 'b' character
			dick = html.decode('utf-8').replace('b', '', 1)
			return dictionary['key']
	elif mode == 5:
		url = f"https://stickx.top/api-arceusx/?hwid={link}&api_key=tUnAZj3sS74DJo9BUb8tshpVhpLJLA"
		with urllib.request.urlopen(url) as response:
			html = response.read()
			# Decode bytes to string and remove the leading 'b' character
			dick = html.decode('utf-8').replace('b', '', 1)
			return dictionary['key']
	elif mode == 6:
		url = f"https://stickx.top/api-codex/?token={link}&api_key=tUnAZj3sS74DJo9BUb8tshpVhpLJLA"
		with urllib.request.urlopen(url) as response:
			html = response.read()
			# Decode bytes to string and remove the leading 'b' character
			dick = html.decode('utf-8').replace('b', '', 1)
			return dictionary['key']
	elif mode == 7:
		url = f"https://stickx.top/api-vegax/?hwid={link}&api_key=tUnAZj3sS74DJo9BUb8tshpVhpLJLA"
		with urllib.request.urlopen(url) as response:
			html = response.read()
			# Decode bytes to string and remove the leading 'b' character
			dick = html.decode('utf-8').replace('b', '', 1)
			return dictionary['key']

def bypassvip(mode, link):
	if mode == 1:
		url = f"https://api.bypass.vip/bypass?url={link}"
		with urllib.request.urlopen(url) as response:
			html = response.read()
			# Decode bytes to string and remove the leading 'b' character
			dick = html.decode('utf-8').replace('b', '', 1)
			return dictionary['key']


def zaneru(mode, link):
	if mode == 1:
		url = f"https://zaneru-official.vercel.app/api/bypass/fluxus?link={link}&api_key=zaneru-official"
		with urllib.request.urlopen(url) as response:
			html = response.read()
			# Decode bytes to string and remove the leading 'b' character
			dick = html.decode('utf-8').replace('b', '', 1)
			dictionary = json.loads(dick)
			return dictionary['key']
	elif mode == 2:
		url = f"https://zaneru-official.vercel.app/api/bypass/relzhub?link={link}&api_key=zaneru-official"
		with urllib.request.urlopen(url) as response:
			html = response.read()
			# Decode bytes to string and remove the leading 'b' character
			dick = html.decode('utf-8').replace('b', '', 1)
			dictionary = json.loads(dick)
			return dictionary['key']
	elif mode == 3:
		url = f"https://zaneru-official.vercel.app/api/bypass/delta?link={link}&api_key=zaneru-official"
		with urllib.request.urlopen(url) as response:
			html = response.read()
			# Decode bytes to string and remove the leading 'b' character
			dick = html.decode('utf-8').replace('b', '', 1)
			dictionary = json.loads(dick)
			return dictionary['key']

def prince(api,mode,link):
	if mode == 1:
		url = f"https://prince-mysticmoth-api.vercel.app/api/fluxus?link={link}&apikey=Triple_0H9BP72"
		with urllib.request.urlopen(url) as response:
			html = response.read()
			# Decode bytes to string and remove the leading 'b' character
			dick = html.decode('utf-8').replace('b', '', 1)
			dictionary = json.loads(dick)
			return dictionary['key']
	elif mode == 2:
		url = f"https://prince-mysticmoth-api.vercel.app/api/codex?link={link}&apikey=Triple_0H9BP72"
		with urllib.request.urlopen(url) as response:
			html = response.read()
			# Decode bytes to string and remove the leading 'b' character
			dick = html.decode('utf-8').replace('b', '', 1)
			dictionary = json.loads(dick)
			return dictionary['key']
	elif mode == 3:
		url = f"https://prince-mysticmoth-api.vercel.app/api/delta?link={link}&apikey=Triple_0H9BP72"
		with urllib.request.urlopen(url) as response:
			html = response.read()
			# Decode bytes to string and remove the leading 'b' character
			dick = html.decode('utf-8').replace('b', '', 1)
			dictionary = json.loads(dick)
			return dictionary['key']
	elif mode == 4:
		url = f"https://prince-mysticmoth-api.vercel.app/api/workink?link={link}&apikey=Triple_0H9BP72"
		with urllib.request.urlopen(url) as response:
			html = response.read()
			# Decode bytes to string and remove the leading 'b' character
			dick = html.decode('utf-8').replace('b', '', 1)
			dictionary = json.loads(dick)
			return dictionary['key']
	elif mode == 5:
		url = f"https://prince-mysticmoth-api.vercel.app/api/rekonise?link={link}&apikey=Triple_0H9BP72"
		with urllib.request.urlopen(url) as response:
			html = response.read()
			# Decode bytes to string and remove the leading 'b' character
			dick = html.decode('utf-8').replace('b', '', 1)
			dictionary = json.loads(dick)
			return dictionary['key']
	elif mode == 6:
		url = f"https://prince-mysticmoth-api.vercel.app/api/mediafire?link={link}&apikey=Triple_0H9BP72"
		with urllib.request.urlopen(url) as response:
			html = response.read()
			# Decode bytes to string and remove the leading 'b' character
			dick = html.decode('utf-8').replace('b', '', 1)
			dictionary = json.loads(dick)
			return dictionary['key']
	elif mode == 7:
		url = f"https://prince-mysticmoth-api.vercel.app/api/arceusx?link={link}&apikey=Triple_0H9BP72"
		with urllib.request.urlopen(url) as response:
			html = response.read()
			# Decode bytes to string and remove the leading 'b' character
			dick = html.decode('utf-8').replace('b', '', 1)
			dictionary = json.loads(dick)
			return dictionary['key']
	elif mode == 8:
		url = f"https://prince-mysticmoth-api.vercel.app/api/linkvertise?link={link}&apikey=Triple_0H9BP72"
		with urllib.request.urlopen(url) as response:
			html = response.read()
			# Decode bytes to string and remove the leading 'b' character
			dick = html.decode('utf-8').replace('b', '', 1)
			dictionary = json.loads(dick)
			return dictionary['key']

def cryzo(mode ,link):
	if mode == 1:
		url = f"http://37.114.41.51:6126/v2/bypass/?link={link}"
		with urllib.request.urlopen(url) as response:
			html = response.read()
			# Decode bytes to string and remove the leading 'b' character
			dick = html.decode('utf-8').replace('b', '', 1)
			dictionary = json.loads(dick)
			return dictionary['key']

def nexus(apikey, mode, link):
	if mode == 1:
		url = f"https://nexusapi-qg8a.onrender.com/api/bypass?link={link}&apikey={apikey}"
		with urllib.request.urlopen(url) as response:
			html = response.read()
			# Decode bytes to string and remove the leading 'b' character
			dick = html.decode('utf-8').replace('b', '', 1)
			dictionary = json.loads(dick)
			return dictionary['key']
	elif mode == 2:
		url = f"https://nexusapi-qg8a.onrender.com/api/adlinks?link={link}&apikey={apikey}"
		with urllib.request.urlopen(url) as response:
			html = response.read()
			# Decode bytes to string and remove the leading 'b' character
			dick = html.decode('utf-8').replace('b', '', 1)
			dictionary = json.loads(dick)
			return dictionary['key']
	# Error: Cannot bypass: returned 

def demon(mode, link):
	if mode == 1:
		url = f"https://keybypass.vercel.app/api/fluxus?url={link}"
		with urllib.request.urlopen(url) as response:
			html = response.read()
			# Decode bytes to string and remove the leading 'b' character
			dick = html.decode('utf-8').replace('b', '', 1)
			dictionary = json.loads(dick)
			return dictionary['key']
	elif mode == 2:
		url = f"https://keybypass.vercel.app/api/mboost?url={link}"
		with urllib.request.urlopen(url) as response:
			html = response.read()
			# Decode bytes to string and remove the leading 'b' character
			dick = html.decode('utf-8').replace('b', '', 1)
			dictionary = json.loads(dick)
			return dictionary['key']
	elif mode == 3:
		url = f"https://keybypass.vercel.app/api/paste_drop?url={link}"
		with urllib.request.urlopen(url) as response:
			html = response.read()
			# Decode bytes to string and remove the leading 'b' character
			dick = html.decode('utf-8').replace('b', '', 1)
			dictionary = json.loads(dick)
			return dictionary['key']
	elif mode == 4:
		url = f"https://keybypass.vercel.app/api/mediafire?url={link}"
		with urllib.request.urlopen(url) as response:
			html = response.read()
			# Decode bytes to string and remove the leading 'b' character
			dick = html.decode('utf-8').replace('b', '', 1)
			dictionary = json.loads(dick)
			return dictionary['key']
	elif mode == 5:
		url = f"https://keybypass.vercel.app/api/relzhub?url={link}"
		with urllib.request.urlopen(url) as response:
			html = response.read()
			# Decode bytes to string and remove the leading 'b' character
			dick = html.decode('utf-8').replace('b', '', 1)
			dictionary = json.loads(dick)
			return dictionary['key']
	elif mode == 6:
		url = f"https://keybypass.vercel.app/api/delta?url={link}"
		with urllib.request.urlopen(url) as response:
			html = response.read()
			# Decode bytes to string and remove the leading 'b' character
			dick = html.decode('utf-8').replace('b', '', 1)
			dictionary = json.loads(dick)
			return dictionary['key']
def tss(mode, link):
	if mode == 1:
		url = f"https://kazi-api.vercel.app/api/bypass?link={link}"
		with urllib.request.urlopen(url) as response:
			html = response.read()
			# Decode bytes to string and remove the leading 'b' character
			dick = html.decode('utf-8').replace('b', '', 1)
			dictionary = json.loads(dick)
			return dictionary['key']
	elif mode == 2:
		url = f"https://kazi-api.vercel.app/api/arceusx?link=&apikey=Kagi_0H9BP72"
		with urllib.request.urlopen(url) as response:
			html = response.read()
			# Decode bytes to string and remove the leading 'b' character
			dick = html.decode('utf-8').replace('b', '', 1)
			dictionary = json.loads(dick)
			return dictionary['key']

def xtr(mode, link):
	if mode == 1:
		url = f"https://fluxusbypassxyz.vercel.app/api/fluxus?link={link}"
		with urllib.request.urlopen(url) as response:
			html = response.read()
			# Decode bytes to string and remove the leading 'b' character
			dick = html.decode('utf-8').replace('b', '', 1)
			dictionary = json.loads(dick)
			return dictionary['key']
	elif mode == 2:
		url = f"https://fluxusbypassxyz.vercel.app/api/delta?link={link}"
		with urllib.request.urlopen(url) as response:
			html = response.read()
			# Decode bytes to string and remove the leading 'b' character
			dick = html.decode('utf-8').replace('b', '', 1)
			dictionary = json.loads(dick)
			return dictionary['key']

def hahabypass(mode, link):
	if mode == 1:
		url = f"https://fluxus-bypass-orcin.vercel.app/api/fluxus?link={link}"
		with urllib.request.urlopen(url) as response:
			html = response.read()
			# Decode bytes to string and remove the leading 'b' character
			dick = html.decode('utf-8').replace('b', '', 1)
			dictionary = json.loads(dick)
			return dictionary['key']
	elif mode == 2:
		url = f"https://codex-lemon-nu.vercel.app/api/codex?link={link}"
		with urllib.request.urlopen(url) as response:
			html = response.read()
			# Decode bytes to string and remove the leading 'b' character
			dick = html.decode('utf-8').replace('b', '', 1)
			dictionary = json.loads(dick)
			return dictionary['key']

def kobayashi_old(mode, link):
	"""
	CUURENTLY NOT WORKING, MOVED TO NEW API
	:developer~2:  Developer By Xynnnn 私
:hatsunefireblue:  Free API :
https://kobayashi-own.vercel.app/api/kobayashi?url=
:hatsuneupdate:  Supported :

Fluxus, Relzhub, Delta, Codex, Rekonise, Mboost, Socialwolvez, Nicuse, Lootlabs, Linkvertise ( all domain ), Linkvertise Dynamic, Work.ink, Paste-Drop, Mediafire

:hatsunefireblue: Fluxus :
https://hatsuneee-fluxus.vercel.app/api/fluxus?url=
:hatsunefireblue: Relzhub :
https://hatsuneee-relzhub-ebon.vercel.app/relz?url=
:hatsunefireblue: Delta :
https://hatsuneee-delta.vercel.app/api/delta?url=
:hatsunefireblue: Rekonise:
https://hatsuneee-rekonise.vercel.app/rekonise?url=
:hatsunefireblue: Mboost :
https://hatsuneee-mboost.vercel.app/mboost?url=
:hatsunefireblue: Paste Drop :
https://hatsuneee-pastedrop.vercel.app/api/paste?url=
:hatsunefireblue: MediaFire :
https://hatsuneee-mediafire.vercel.app/api/mediafire?url=
:hatsunefireblue: SocialWolvez :
https://hatsuneee-socialwolvez.vercel.app/socialwolvez?url=
	"""
	pass

def kobayashi(mode,link):
	if mode == 1:
		url = f"https://kobayashi-heart-attack.vercel.app/api/kobayashi?url={link}&kobayashi=NoHome"
		with urllib.request.urlopen(url) as response:
			html = response.read()
			# Decode bytes to string and remove the leading 'b' character
			dick = html.decode('utf-8').replace('b', '', 1)
			dictionary = json.loads(dick)
			return dictionary['key']

def bypass(api, mode, link, apikey=""):
	key = None
	if api == 0:
		key = duck(mode, link)
	elif api == 1:
		key = stickx(mode, link)
	elif api == 2:
		key = bypassvip(mode, link)
	elif api == 3:
		key = zaneru(mode, link)
	elif api == 4:
		key = prince(mode,link)
	elif api == 5:
		key = cryzo(mode, link)
	elif api == 6:
		key = nexus(apikey,mode,link)
	elif api == 7:
		key = demon(mode, link)
	elif api == 8:
		key = tss(mode, link)
	elif api == 9:
		key = xtr(mode, link)
	return key

def built_in_bypass():
	with open("ascii_art.txt", "r") as f:
		print(f.read())
	dev_dict = is_developer(input("Type your developer key: "))
	api = change_apis(dev_dict["is_developer"])
	while True:
		mode = str_return_mode(api)
		if mode == 0:
			api = change_apis(dev_dict["is_developer"])
		if mode != 0:
			break
	apikey = ""
	if api == 6:
		apikey = input("Type Nexus API Key (https://discord.gg/TPgZgYpNAS): ")
		if apikey == "":
			print("You MUST input API key!")
	try:
		link = input("Type link: ")
		if len(link) == 0:
			raise NoHWIDOrTokenKey
	except NoHWIDOrTokenKey:
		print("You MUST input HWID or Token key!")
	except Exception as e:
		print(e)
	else:
		print("Please wait...")
		print("Key:", bypass(api, mode, link, apikey))
	print("Press Enter to continue or Ctrl(Cmd) + C to stop", end=" ")
	input()
	return
def main():
	exit_parm = "N"
	while True:
		try:
			built_in_bypass()
		except KeyboardInterrupt:
			exit_parm = input("Do you want to exit? (y/N)")
			if exit_parm.lower() == "y":
				print("Good bye!")
				os.system("pause")
				break
			else:
				print("Continue now")
				os.system("pause")
if __name__ == '__main__':
	main()
