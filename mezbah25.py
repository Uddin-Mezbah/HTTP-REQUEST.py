import requests
#r = requests.get("https://financialmodelingprep.com/api/company/price/AAPL")
#print(r.status_code)

url = "https://www.linkedin.com/feed/"
data = {
    "p1":4,
    "p2":8
}

r2 = requests.post(url = url, data = data)
print(r2)