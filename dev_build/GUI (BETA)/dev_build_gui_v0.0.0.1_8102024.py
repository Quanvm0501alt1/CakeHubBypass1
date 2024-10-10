import dev_build_v00018102024 as bypasser
import customtkinter

ctk = customtkinter

customtkinter.set_default_color_theme("dark-blue")
customtkinter.set_appearance_mode("system")

# Make Window
window = ctk.CTk()
# Set geometry and Title
window.geometry("60x250")
window.title("CTk example")

# Main parts

# Make api list
class Main:
	"""docstring for Main"""
	def __init__(self, window):
		global ctk, bypasser
		self.ctk = ctk
		self.bypasser = bypasser
		self.window = window
		self.frame = customtkinter.CTkFrame(master=self.window, width=200, height=200)
		self.label1 = customtkinter.CTkLabel(self.frame, text="API:", fg_color="transparent")
		self.api()
		self.label2 = customtkinter.CTkLabel(self.frame, text="Mode:", fg_color="transparent")
		self.mode()
		self.link()
		self.button()
	def update(self):
		self.window.update()
		self.window.update_idletasks()
	def api(self):
		self.api_var = customtkinter.StringVar(value="Duck API")
		self.api_gui = customtkinter.CTkOptionMenu(self.frame,
			values=["Duck API", "StickX API", "Bypass.vip API", "Zaneru Bypass API", "Prince API", "Cryzo", "Nexus API", "Demon", "Triple Scripts Server", "XTR Bypass", "HaHa bypass (Coming Soon)"], 
			variable=self.api_var,
			command=self.update_mode)  # Add command to call update_mode on change
	def mode(self):
		self.api = self.api_gui.get()
		self.mode_var = customtkinter.StringVar(value="Fluxus")
		self.mode_values = self.get_mode_values(self.api)
		self.mode_gui = self.ctk.CTkOptionMenu(self.frame, values=self.mode_values, variable=self.mode_var)
	def get_mode_values(self, api):
		mode_values = []
		if api == "Duck API":
			mode_values = ["Fluxus", "Adlink", "RelzHub"]
		elif api == "StickX API":
			mode_values = ["Fluxus", "Delta", "Hydrogen", "Linkvertise", "Arceus X", "Code X", "Vega X"]
		elif api == "Bypass.vip API":
			mode_values = ["Adlink"]
		elif api == "Zaneru Bypass API":
			mode_values = ["Fluxus","RelzHub", "Delta"]
		elif api == "Prince API":
			mode_values = ["Fluxus", "Code X", "Delta", "Work.ink", "Rekonise", "MediaFire", "Arceus X", "Linkvertise"]
		return mode_values
	def link(self):
		self.link_gui = customtkinter.CTkEntry(self.frame, placeholder_text="Paste your link here")
		self.link = self.link_gui.get()
	def button(self):
		self.button = customtkinter.CTkButton(self.frame, text="Bypass!", command=self.button_event)
	def button_event(self):
		api_dict = {
			"Duck API": 0,
			"StickX API": 1,
			"Bypass.vip API": 2,
			"Zaneru Bypass API": 3,
			"Prince API": 4,
			"Cryzo": 5,
			"Nexus API": 6,
			"Demon": 7,
			"Triple Scripts Server": 8,
			"XTR Bypass": 9,
			"HaHa bypass (Coming Soon)": None  # Not implemented yet
		}
		mode_dict = {
			0: {"Fluxus": 1, "Adlink": 2, "RelzHub": 3},
			1: {"Fluxus": 1, "Delta": 2, "Hydrogen": 3, "Linkvertise": 4, "Arceus X": 5, "Code X": 6, "Vega X": 7},
			2: {"Adlink": 1},
			3: {"Fluxus": 1, "Relz Hub": 2, "Delta": 3},
			4: {"Fluxus": 1, "Code X": 2, "Delta": 3, "Work.ink": 4, "Rekonise": 5, "Mediafire": 6, "Arceus X": 7, "Linkvertise": 8},
			5: {"Bypass Link": 1},
			6: {"Bypass Roblox link": 1, "Adlink": 2},
			7: {"Fluxus": 1, "MBoost": 2, "PasteDrop": 3, "MediaFire": 4, "RelzHub": 5, "Delta": 6},
			8: {"Bypass all Links": 1, "ArceusX": 2},
			9: {"Fluxus": 1, "Delta": 2},
			10: {"Fluxus": 1, "CodeX": 2}
		}
		api = api_dict.get(self.api, None)
		mode = mode_dict[api].get(self.mode_var.get(), None)
		if self.api is not None:
			print(self.api, api)
			print(self.mode_var.get(), mode)
			self.key = self.bypasser.bypass(api, mode, self.link)
			print(self.key)
			self.label3 = self.ctk.CTkLabel(self.frame, text=self.key, fg_color="transparent")
			self.label3.pack()
			self.window.update()
	def update_mode(self, choice):
		self.api = choice
		self.mode_values = self.get_mode_values(self.api)
		self.mode_gui.configure(values=self.mode_values)
	def pack(self):
		self.frame.pack()
		self.label1.pack(padx=10, pady=0)
		self.api_gui.pack(padx=10, pady=0)
		self.label2.pack(padx=10, pady=0)
		self.mode_gui.pack(padx=10, pady=12.5)
		self.link_gui.pack(padx=10, pady=0)
		self.button.pack(padx=10, pady=0)

main = Main(window)
main.pack()
window.mainloop()
