# Cake bypass Python scripts
# import requests
import urllib.request
import json, os

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
	1st Built-in API ("Builtin1()"):
	0: StickX API
	1: Duck API
	2: Bypass.vip
	3: Demon
	4: Prince X
	5: TSS
	6: NrzXHaxRBLX
	Add more!
	""")
	api = int(input("Type API: "))
	if api == 13:
		print("You are not a developer!")
		return
	if api not in [0]:
		print("Opps! Invaild API!")
		return
	else:
		return api

class KobayashiBypass:
	""" Archived """
	def __init__(self, bypasslink=False, api=0 ,mode=0 ,link=""):
		pass
	def kobayashi_old(mode, link):
		"""
		CUURENTLY NOT WORKING, MOVED TO NEW API
		:developer~2:  Developer By Xynnnn 私
		:hatsunefireblue:  Free API :
		https://kobayashi-own.vercel.app/api/kobayashi?url=
		:hatsuneupdate:  Supported :

		Fluxus, Relzhub, Delta, Codex, Rekonise, Mboost, Socialwolvez, Nicuse, Lootlabs,
		Linkvertise ( all domain ), Linkvertise Dynamic, Work.ink, Paste-Drop, Mediafire

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
				
				dick = html.decode('utf-8').replace('b', '', 1)
				dictionary = json.loads(dick)
				return dictionary['key']

class Builtin1:
	"""
	1: StickX API
	2: Duck API
	3: Bypass.vip
	4: Demon
	5: Prince X
	6: TSS
	7: NrzXHaxRBLX
	"""
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
				dick = html.decode('utf-8').replace('b', '', 1)
				dictionary = json.loads(dick)
				return dictionary['key']
		elif mode == 2:
			url = f"https://stickx.top/api-delta/?hwid={link}&api_key=tUnAZj3sS74DJo9BUb8tshpVhpLJLA"
			with urllib.request.urlopen(url) as response:
				html = response.read()
				dick = html.decode('utf-8').replace('b', '', 1)
				dictionary = json.loads(dick)
				return dictionary['key']
		elif mode == 3:
			url = f"https://stickx.top/api-hydrogen/?hwid={link}&api_key=E99l9NOctud3vmu6bPne"
			with urllib.request.urlopen(url) as response:
				html = response.read()
				dick = html.decode('utf-8').replace('b', '', 1)
				dictionary = json.loads(dick)
				return dictionary['key']
		elif mode == 4:
			url = f"https://stickx.top/api-linkvertise/?link={link}&api_key=E99l9NOctud3vmu6bPne"
			with urllib.request.urlopen(url) as response:
				html = response.read()
				dick = html.decode('utf-8').replace('b', '', 1)
				dictionary = json.loads(dick)
				return dictionary['key']
		elif mode == 5:
			url = f"https://stickx.top/api-arceusx/?hwid={link}&api_key=tUnAZj3sS74DJo9BUb8tshpVhpLJLA"
			with urllib.request.urlopen(url) as response:
				html = response.read()
				dick = html.decode('utf-8').replace('b', '', 1)
				dictionary = json.loads(dick)
				return dictionary['key']
		elif mode == 6:
			url = f"https://stickx.top/api-codex/?token={link}&api_key=tUnAZj3sS74DJo9BUb8tshpVhpLJLA"
			with urllib.request.urlopen(url) as response:
				html = response.read()
				dick = html.decode('utf-8').replace('b', '', 1)
				dictionary = json.loads(dick)
				return dictionary['key']
		elif mode == 7:
			url = f"https://stickx.top/api-vegax/?hwid={link}&api_key=tUnAZj3sS74DJo9BUb8tshpVhpLJLA"
			with urllib.request.urlopen(url) as response:
				html = response.read()
				dick = html.decode('utf-8').replace('b', '', 1)
				dictionary = json.loads(dick)
				return dictionary['key']

	def duck(self, mode, link):
		"""
		1: Fluxus
		2: Adlink
		3: Relzhub (Not working)
		"""
		if mode == 0:
			return
		if mode == 1:
			url = f"https://ducktestflu.vercel.app/api/fluxus?url={link}"
			with urllib.request.urlopen(url) as response:
				html = response.read()
				dick = html.decode('utf-8').replace('b', '', 1)
				dictionary = json.loads(dick)
				return dictionary['key']
		elif mode == 2:
			url = f"https://duckcute-zeta.vercel.app/adlink?link={link}"
			with urllib.request.urlopen(url) as response:
				html = response.read()
				dick = html.decode('utf-8').replace('b', '', 1)
				dictionary = json.loads(dick)
				return dictionary['key']
		elif mode == 3:
			url = f"https://duckcute-zeta.vercel.app/relzhub?link={link}"
			with urllib.request.urlopen(url) as response:
				html = response.read()
				dick = html.decode('utf-8').replace('b', '', 1)
				dictionary = json.loads(dick)
				return dictionary['key']
	def bypassvip(self, mode, link):
		"""
		1: Bypass all links
		Currently support: Linkvertise, paster.so, Admaven, Lootlinks/Lootlabs,
		work.ink, boost.ink, mboost.me (bst.gg, booo.st), socialwolvez.com,
		sub2get.com, social-unlock.com, unlocknow.net, sub2unlock.com, sub2unlock.net,
		sub2unlock.io, sub4unlock.io, rekonise.com, adfoc.us, v.gd, bit.ly, tinyurl.com,
		is.gd, rebrand.ly, tinylink.onl, t.co, bit.do
		"""
		if mode == 0:
			return
		if mode == 1:
			url = f"https://api.bypass.vip/bypass?url={link}"
			with urllib.request.urlopen(url) as response:
				html = response.read()
				dick = html.decode('utf-8').replace('b', '', 1)
				dictionary = json.loads(dick)
				return dictionary['key']
	def demon(self, mode, link):
		"""
		1: Bypass all links
		Currently support: Fluxus, Rekonise, Codex, Relz, Cokka, Nicuse, Mboost.me,
		Delta, linkvertise dynamic, Sub2unlock, Boost.ink
		2: Fluxus
		"""
		if mode == 0:
			return
		if mode == 1:
			url = f"https://bypass-all.vercel.app/bypass?url={link}&apikey=DemonOnTop"
			with urllib.request.urlopen(url) as response:
				html = response.read()
				dick = html.decode('utf-8').replace('b', '', 1)
				dictionary = json.loads(dick)
				return dictionary['key']
		elif mode == 2:
			url = f"https://apifluxus.zaaproject.xyz/api/fluxus?url={link}"
			with urllib.request.urlopen(url) as response:
				html = response.read()
				dick = html.decode('utf-8').replace('b', '', 1)
				dictionary = json.loads(dick)
				return dictionary['key']
		elif mode == 3:
			url = f"https://apifluxus.zzaaproject.my.id/api/fluxus?url={link}"
			with urllib.request.urlopen(url) as response:
				html = response.read()
				dick = html.decode('utf-8').replace('b', '', 1)
				dictionary = json.loads(dick)
				return dictionary['key']
	def prince(self, mode, link):
		"""
		1: Bypass all links (Not working)
		Currently support: unknown
		"""
		if mode == 0:
			return
		if mode == 1:
			url = f"https://prince-x-api.vercel.app/bypass?url={link}"
			with urllib.request.urlopen(url) as response:
				html = response.read()
				dick = html.decode('utf-8').replace('b', '', 1)
				dictionary = json.loads(dick)
				return dictionary['key']
	def tss(self, mode, link):
		if mode == 0:
			return
		if mode == 1:
			url = f"https://prince-x-api.vercel.app/bypass?url={link}"
			with urllib.request.urlopen(url) as response:
				html = response.read()
				dick = html.decode('utf-8').replace('b', '', 1)
				dictionary = json.loads(dick)
				return dictionary['key']
	def NrzXHaxRBLX(self, mode, link):
		"""
		1: Linkvertise
		2: Mediafire
		"""
		if mode == 0:
			return
		if mode == 1:
			url = f"https://keybypass.vercel.app/api/linkvertise?url={link}"
			with urllib.request.urlopen(url) as response:
				html = response.read()
				dick = html.decode('utf-8').replace('b', '', 1)
				dictionary = json.loads(dick)
				return dictionary['key']
		elif mode == 2:
			url = f"https://keybypass.vercel.app/api/mediafire?url={link}"
			with urllib.request.urlopen(url) as response:
				html = response.read()
				dick = html.decode('utf-8').replace('b', '', 1)
				dictionary = json.loads(dick)
				return dictionary['key']
	def testhub(self, mode, link):
		"""
		1: Bypass all links
		Currently support: Delta, Cryptic, Fluxus, Codex(Bug),
		adlinks(linkvertise,lotlabs,sub2unlock,lotlinks,etc), trigon"""
		if mode == 0:
			return
		if mode == 1:
			url = f"https://fi4.bot-hosting.net:22869/executor?url={link}"
			with urllib.request.urlopen(url) as response:
				html = response.read()
				dick = html.decode('utf-8').replace('b', '', 1)
				dictionary = json.loads(dick)
				return dictionary['key']

	def astralx(self, mode, link):
		"""
		1: Bypass all links
		Currently support: Fluxus, Delta, Cryptic, LinkVetise, Trigon
		"""
		if mode == 0:
			return
		if mode == 1:
			url = f"http://145.223.81.79:2020/api/bypass?url={link}"
			with urllib.request.urlopen(url) as response:
				html = response.read()
				dick = html.decode('utf-8').replace('b', '', 1)
				dictionary = json.loads(dick)
				return dictionary['key']
	def ethos(self, mode, link):
		"""
		1: Bypass all links
		Currently Support: Linkvertise, AdMaven, LootLabs, Trigon KeySystem,
		Fluxus KeySystem, MBoost, Sub2Unlock (.com, .io, .net), Sub4Unlock (.io, .net),
		Boost.ink, SocialWolvez, AdFocus, MediaFire, PasteDrop (RAW), Pastebin (RAW),
		Paster.so, UnlockNow.net, Rekonise (rkns.link domain supported), Sub2Get.com,
		Esohasl (script site, gets script), SocialUnlock(.com)
		"""
		if mode == 0:
			return
		if mode == 1:
			url = f"https://ethos.kys.gay/api/free/bypass?url={link}"
			with urllib.request.urlopen(url) as response:
				html = response.read()
				dick = html.decode('utf-8').replace('b', '', 1)
				dictionary = json.loads(dick)
				return dictionary['key']
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
