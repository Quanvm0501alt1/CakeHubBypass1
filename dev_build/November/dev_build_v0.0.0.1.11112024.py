# Cake bypass Python scripts
# import requests
import urllib.request
import json, base64, os

class Error(Exception):
	"""docstring for Error"""
	pass
class NoHWIDOrTokenKey(Error):
	pass

def str_return_mode(api):
	
	mode = int(input("Type mode: "))
	wrong_mode = False
	if mode == 0:
		return 0
	else:
		pass

		if wrong_mode == True:
			print("Opps! Invaild Mode!")
		else:
			return mode


def change_apis():
	print("""
	Building api based on https://apif.simdif.com/
	0: StickX (Disabled by dev)
	1: KYS.GAY
	""")
	api = int(input("Type API: "))
	if api == 13:
		print("You are not a developer!")
		return
	if api not in [0,1,2,3,4,5,6,7,8,9,10]:
		print("Opps! Invaild API!")
		return
	else:
		return api

class KobayashiBypass:
	""" Work In Progress (WIP)"""
	def __init__(self, bypasslink=False, api=0 ,mode=0 ,link=""):
		pass
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
		# Work In Progress
		print("WIP")

	# old api
	def kobayashi(mode,link):
		if mode == 1:
			url = f"https://kobayashi-heart-attack.vercel.app/api/kobayashi?url={link}&kobayashi=NoHome"
			with urllib.request.urlopen(url) as response:
				html = response.read()
				# Decode bytes to string and remove the leading 'b' character
				dick = html.decode('utf-8').replace('b', '', 1)
				dictionary = json.loads(dick)
				return dictionary['key']

class BypassUrlsFromApifsimdif:
	"""
1: StickX API
2: Kys.gay
3: Bypass.lat"""
	def __init__(self, bypasslink=False, api=0 ,mode=0 ,link=""):
		if bypasslink == True:
			if api == 0:
				return stickx(mode, link)
			elif api == 1:
				return kysgay(mode, link)
	def stickx(self, mode, link):
		"""
1: Fluxus
2: Delta (Fixing)
3: Hydrogen
4: Linkvertise
5: Arceus X
6: Codex
7: Vega X
"""
		if mode == 0:
			return
		if mode == 1:
			url = f"https://stickx.top/api-fluxus/?hwid={link}&api_key=E99l9NOctud3vmu6bPne"
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
				dictionary = json.loads(dick)
				return dictionary['key']
		elif mode == 3:
			url = f"https://stickx.top/api-hydrogen/?hwid={link}&api_key=E99l9NOctud3vmu6bPne"
			with urllib.request.urlopen(url) as response:
				html = response.read()
				# Decode bytes to string and remove the leading 'b' character
				dick = html.decode('utf-8').replace('b', '', 1)
				dictionary = json.loads(dick)
				return dictionary['key']
		elif mode == 4:
			url = f"https://stickx.top/api-linkvertise/?link={link}&api_key=E99l9NOctud3vmu6bPne"
			with urllib.request.urlopen(url) as response:
				html = response.read()
				# Decode bytes to string and remove the leading 'b' character
				dick = html.decode('utf-8').replace('b', '', 1)
				dictionary = json.loads(dick)
				return dictionary['key']
		elif mode == 5:
			url = f"https://stickx.top/api-arceusx/?hwid={link}&api_key=tUnAZj3sS74DJo9BUb8tshpVhpLJLA"
			with urllib.request.urlopen(url) as response:
				html = response.read()
				# Decode bytes to string and remove the leading 'b' character
				dick = html.decode('utf-8').replace('b', '', 1)
				dictionary = json.loads(dick)
				return dictionary['key']
		elif mode == 6:
			url = f"https://stickx.top/api-codex/?token={link}&api_key=tUnAZj3sS74DJo9BUb8tshpVhpLJLA"
			with urllib.request.urlopen(url) as response:
				html = response.read()
				# Decode bytes to string and remove the leading 'b' character
				dick = html.decode('utf-8').replace('b', '', 1)
				dictionary = json.loads(dick)
				return dictionary['key']
		elif mode == 7:
			url = f"https://stickx.top/api-vegax/?hwid={link}&api_key=tUnAZj3sS74DJo9BUb8tshpVhpLJLA"
			with urllib.request.urlopen(url) as response:
				html = response.read()
				# Decode bytes to string and remove the leading 'b' character
				dick = html.decode('utf-8').replace('b', '', 1)
				dictionary = json.loads(dick)
				return dictionary['key']

	def kysgay(self, mode, link):
		"""
1: Bypass links
2: Delta"""
		if mode == 0:
			return
		if mode == 1:
			url = f"https://dlr.kys.gay/api/free/bypass?url={link}"
			with urllib.request.urlopen(url) as response:
				html = response.read()
				# Decode bytes to string and remove the leading 'b' character
				dick = html.decode('utf-8').replace('b', '', 1)
				dictionary = json.loads(dick)
				return dictionary['key']
		elif mode == 2:
			url = f"https://dlr.kys.gay/api/free/delta?url={link}"
			with urllib.request.urlopen(url) as response:
				html = response.read()
				# Decode bytes to string and remove the leading 'b' character
				dick = html.decode('utf-8').replace('b', '', 1)
				dictionary = json.loads(dick)
				return dictionary['key']
	def bypasslat(mode, link):
		"""
1: Bypass links (Vega X, Linkvertise, Work.ink, Paster.so, AdMaven, Lootlabs)
2: Another bypass (DLR_DonaldTrump apikey)"""
		if mode == 0:
			return
		if mode == 1:
			url = f"https://bypass.lat/api/free/bypass?url={link}"
			with urllib.request.urlopen(url) as response:
				html = response.read()
				# Decode bytes to string and remove the leading 'b' character
				dick = html.decode('utf-8').replace('b', '', 1)
				dictionary = json.loads(dick)
				return dictionary['key']
		elif mode == 2:
			url = f"https://bypass.lat/api/bypass?apikey=DLR_DONALDTRUMP&url={link}"
			with urllib.request.urlopen(url) as response:
				html = response.read()
				# Decode bytes to string and remove the leading 'b' character
				dick = html.decode('utf-8').replace('b', '', 1)
				dictionary = json.loads(dick)
				return dictionary['key']
	def ethosbypass
def bypass(api, mode, link):
	key = None
	

def built_in_bypass():
	with open("ascii_art.txt", "r") as f:
		print(f.read())
	api = change_apis()
	while True:
		mode = str_return_mode(api)
		if mode == 0:
			api = change_apis()
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
