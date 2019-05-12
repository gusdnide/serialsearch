import requests
import AdvancedHTMLParser
import sys

from colorama import Fore


strLink = 'https://www.serials.ws/?chto='
strKey = 'https://www.serials.ws/d.php?n='
strPrograma = ''
parserHTML = AdvancedHTMLParser.AdvancedHTMLParser()


def DownString(url, param):
    return requests.get(url + param.replace(" ", "+")).text


asci = """
  /$$$$$$                   /$$         /$$
 /$$__  $$                 |__/        | $$
| $$  \__/ /$$$$$$  /$$$$$$ /$$ /$$$$$$| $$
|  $$$$$$ /$$__  $$/$$__  $| $$|____  $| $$
 \____  $| $$$$$$$| $$  \__| $$ /$$$$$$| $$
 /$$  \ $| $$_____| $$     | $$/$$__  $| $$
|  $$$$$$|  $$$$$$| $$     | $|  $$$$$$| $$
 \______/ \_______|__/     |__/\_______|__/
                                           
                           Search                 	                         
                                           
"""
print(asci)
print(Fore.YELLOW +" 		Developer: gusdnide")

if len(sys.argv) >= 2:
	strPrograma = sys.argv[1]
else:
	strPrograma = input(Fore.RED + "[*] " + Fore.WHITE + " Escreva o nome do software:\n")


parserHTML.parseStr(DownString(strLink, strPrograma))
count = 0
links = parserHTML.getElementsByTagName("a")


seriais = []

for link in links:
	nome = link.innerText
	url = str(link.href)
	if "javascript" not in url or "AddFavorite" in url or strPrograma not in nome: 
		continue
	url = url.replace("javascript:d(", "").replace(")", "")
	print( Fore.RED + "[" + str(count) +  "] " + Fore.WHITE + nome )
	count = count + 1
	seriais.append([nome, url])

if len(seriais) < 1:
	print(Fore.RED + "[*] " + Fore.WHITE +"Nenhum serial foi encontrado.")
	exit()

idValido = False
resp = -1

while (not idValido):	
	resp = int(input(Fore.WHITE + "\n   Digite um ID  entre " +  Fore.GREEN +"0-"  +  (str(len(seriais))) + ": "))
	if not (resp >= 0 and resp < len(seriais)):
		print("Voce digitou um ID invalido.")		
	else:
		idValido = True

serial = seriais[resp]

print(asci)
print()
print( Fore.RED + "[*]" + Fore.WHITE + " Baixando o serial " + Fore.RED +  serial[0])
print()
parserHTML.parseStr(DownString(strKey,serial[1]))
textarea = parserHTML.getElementsByTagName("textarea")[0].innerText
print(textarea)
print( Fore.RED + "\n\n[*] " + Fore.WHITE +" Concluido com sucesso.")










