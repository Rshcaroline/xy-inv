from api import Bihang

client = Bihang.api_secret(api_key="40034b0985b3481abb6e73aeec5e21b6", api_secret="7387464f624344ab98085b13c2ed0d38")

r = client.buttonsButton({'name':"python button",'price':2,'price_currency':'BTC'})

print(r.button)
