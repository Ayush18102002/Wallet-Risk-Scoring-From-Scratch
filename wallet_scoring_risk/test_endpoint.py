import requests

wallet = "0xfe5a05c0f8b24fca15a7306f6a4ebb7dcf2186ac"
chain_id = "1"  
api_key = "ckey_docs"  
api_key = "cqt_rQ7WrxCBBd84H7f9bMXbr4Jkt8h9"
url = f"https://api.covalenthq.com/v1/{chain_id}/address/{wallet}/balances_v2/?key={api_key}"

res = requests.get(url)
print(res.json())
