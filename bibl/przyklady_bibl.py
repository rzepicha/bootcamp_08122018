import datetime
import json

print(datetime.date.today())

poczatek_urlopu=datetime.date(2019,7,1)
print(poczatek_urlopu-datetime.date.today())

poczatek_urlopu.weekday()

teraz=datetime.datetime.today() #do sekund
print(teraz+datetime.timedelta(days=2, hours=7))
print(datetime.timedelta(days=2)/datetime.timedelta(hours=1))




import decimal

print(decimal.Decimal(1100000000000000001.00))
print(decimal.Decimal('1100000000000000001.00'))

duzo=decimal.Decimal('1100000000000000001.00')
print(duzo*2)


s='{"kwota":1.56}'
json.loads(s)
print(json.loads(s, parse_float=decimal.Decimal))





import urllib.parse
#biblioteka rozkładająca na czesci adres url
urllib.parse.urlparse("adres")

