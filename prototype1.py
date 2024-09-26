# Cake bypass Python scripts
# import requests
import urllib.request
import json
class Error(Exception):
	"""docstring for Error"""
	pass
class NoHWIDOrTokenKey(Error):
	pass

def main():
	api = 1
	print("""
0: Mode ((Duck API < DEFAULT) / StickX API) (Testing)
1: Fluxus
2: Bypass Adlink""")
	try:
		mode = int(input("Type mode: "))
		key = input("Type key: ")
		if len(key) == 0:
			raise NoHWIDOrTokenKey
	except NoHWIDOrTokenKey:
		print("You MUST input HWID or Token key!")
	except Exception as e:
		print(e)
	else:
		if api == 1:
			if mode == 1:
				url = f'https://duckcute-zeta.vercel.app/fluxus?link={key}'
				with urllib.request.urlopen(url) as response:
					html = response.read()
					# Decode bytes to string and remove the leading 'b' character
					dick = html.decode('utf-8').replace('b', '', 1)
					dictionary = json.loads(dick)
					print("Key:",dictionary['key'])
			if mode == 2:
				url = f"https://duckcute-zeta.vercel.app/adlink?link={key}"
				with urllib.request.urlopen(url) as response:
					html = response.read()
					# Decode bytes to string and remove the leading 'b' character
					dick = html.decode('utf-8').replace('b', '', 1)
					print(dick)


	# finally:
		# pass
if __name__ == '__main__':
	main()