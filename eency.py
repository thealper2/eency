import argparse
import os
import socket
import colorama
from colorama import Fore, Style, Back
from cryptography.fernet import Fernet

colorama.init(autoreset=True)

def encryption(file="", path="", is_file=False, is_dir=False):
	key = Fernet.generate_key()
	with open("key.txt", "wb") as f:
		f.write(key)
	print(f"{Fore.GREEN}[+] Anahtar :{Fore.RESET}", key)
	print(f"{Fore.RED}{Style.BRIGHT}[!] key.txt olusturuldu. Sakin silmeyin! Dosyanizi kaybedebilirsiniz.{Fore.RESET}{Style.RESET_ALL}")
	fernet = Fernet(key)
	file_path = ""

	if is_file == True:
		directory, filename = os.path.split(file)
		if os.access(directory, os.W_OK):
			with open(file, "rb") as f:
				data = f.read()
			encrypted_data = fernet.encrypt(data)

			with open(file + ".eency", "wb") as f:
				f.write(encrypted_data)
			print(f"{Fore.YELLOW}[-] Dosya: {file_path}" + file + f" sifrelendi.{Fore.RESET}")
			os.remove(file)
	elif is_dir == True:
		for root, dirs, files in os.walk(path):
			for f in files:
				file_path = os.path.join(root, f)
				directory, filename = os.path.split(file_path)
				if os.access(directory, os.W_OK):
					with open(file_path, "rb") as r:
						data = r.read()
					encrypted_data = fernet.encrypt(data)
					with open(file_path + ".eency", "wb") as w:
						w.write(encrypted_data)
					print(f"{Fore.YELLOW}[-] Dosya: " + file_path +  f" sifrelendi.{Fore.RESET}")
					os.remove(file_path)

def decryption(file="", path="", is_file=False, is_dir=False):
	with open("key.txt", "rb") as f:
		key = f.read()
	print(f"{Fore.GREEN}[+] Anahtar :{Fore.RESET}", key)
	fernet = Fernet(key)
	file_path = ""
	if is_file == True:
		directory, filename = os.path.split(file)
		if file.endswith(".eency"):
			with open(file, "rb") as f:
				encrypted_data = f.read()
			decrypted_data = fernet.decrypt(encrypted_data)
			file_name, extension = os.path.splitext(file)
			with open(file_name, "wb") as f:
				f.write(decrypted_data)
			print(f"{Fore.YELLOW}[-] Dosya: " + file + f" sifresi cozuldu.{Fore.RESET}")
			os.remove(file)
	elif is_dir == True:
		for root, dirs, files in os.walk(path):
			for f in files:
				if f.endswith(".eency"):
					file_path = os.path.join(root, f)
					with open(file_path, "rb") as r:
						encrypted_data = r.read()
					decrypted_data = fernet.decrypt(encrypted_data)
					filename, extension = os.path.splitext(file_path)
					with open(os.path.join(root, filename), "wb") as w:
						w.write(decrypted_data)
					print(f"{Fore.YELLOW}[-] Dosya: " + file_path + f" sifresi cozuldu.{Fore.RESET}")
					os.remove(file_path)

argument_parser = argparse.ArgumentParser(description="Fernet kutuphanesi ile dosya sifrelem uygulamasidir. Sakin key.txt dosyasini silmeyin. Dosyanizi geri donduruleyecek sekilde kaybedebilirsiniz. Olusabilecek tum hatalardan kullanici sorumludur.")
argument_parser.add_argument('--encryption', required=False, action='store_true', help="Sifrele")
argument_parser.add_argument('--decryption', required=False, action='store_true', help="Sifre coz")
argument_parser.add_argument('--file', type=str, required=False, help="Dosya sifrele/sifre coz")
argument_parser.add_argument('--dir', type=str, required=False, help="Dizin icindekileri sifrele/sifre coz")
arguments = argument_parser.parse_args()

# Ornek komutlar
# python3 eency.py --encryption --file /home/alper/dosya.txt
# python3 eency.py --encryption --dir /home/alper
# python3 eency.py --decryption --file /home/alperdosya.txt
# python3 eency.py --decryption --dir /home/alper

if (arguments.encryption and arguments.file != None):
	encryption(file=arguments.file, is_file=True)

elif (arguments.decryption and arguments.file != None):
	decryption(file=arguments.file, is_file=True)

elif (arguments.encryption and arguments.dir != None):
	encryption(path=arguments.dir, is_dir=True)

elif (arguments.decryption and arguments.dir != None):
	decryption(path=arguments.dir, is_dir=True)
