import requests

def ask_money():
	monnaie = input("Indiquez l'abréaviation de la crypto-monnaie dont vous désirez connaitre le prix.\nVotre réponse : ")
	show_money(monnaie)

def show_money(monnaie):
	r = requests.get('https://min-api.cryptocompare.com/data/price?fsym='+monnaie+'&tsyms=BTC,USD,EUR').json()
	valeur = str(r["EUR"])
	print("Votre monnaie vaut : "+valeur+" euros.")
	ask_money()

def main():
	try:
		r = requests.get('https://www.cryptocompare.com/api/data/coinlist/').json()["Data"]
		for value in r.values():
			print(value['FullName'])
		ask_money()	
	except Exception as e:
		print(e)
		print("Erreur lors de la récupération de la totalité des noms des crypto-monnaies")

main()