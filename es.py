import requests
import json
import sys

#Oxford API
#Roberto / soyroberto
#https://developer.oxforddictionaries.com/admin/applications
#Tue 30 Nov 2021 11:49:52 AEDT
#Copia del original, removí las llaves
app_id = ''
app_key = ''
language = 'es'
#25/03 https://tecadmin.net/python-command-line-arguments/
#word_id = La variable para la palabra a buscar
fields = 'definitions' 
#origword_id = str(sys.argv[1])
#https://stackoverflow.com/questions/2194163/python-empty-argument
if len(sys.argv) == 1:
	print ("Falta la palabra 😼🐮🙃\n")
else:
	word_id = str(sys.argv[1])
	onedesout= '/Users/roberto/OneDrive/Azure/palabras/noexistepal' #texto
	strictMatch = 'false'
	url = 'https://od-api.oxforddictionaries.com:443/api/v2/entries/' + language + '/' + word_id.lower() + '?fields=' + fields + '&strictMatch=' + strictMatch;

	r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})

	if (r.status_code) == 200:
		#original print("text \n" + r.text)
		#originalprint("\n" + r.text)
		print(r.text)
#json lee
		#https://stackoverflow.com/questions/4706499/how-do-you-append-to-a-file
		f = open ('/Users/roberto/t/es.json','a') 
		f.write(r.text)
		f.close
	elif (r.status_code) == 404:
		print("{} 😬🤨🤔 " .format(r.status_code) + word_id + "\n")
		#f = open ('/Users/roberto/t/noexistepal.json','a') 
		f = open (onedesout,'a') 
		f.write(word_id+"\n")
		f.close
		#Rprint("json \n" + json.dumps(r.json()))
