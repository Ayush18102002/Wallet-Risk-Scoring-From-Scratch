# src/fetch_data.py

import requests
import time

COVALENT_API_KEY = "cqt_rQ7WrxCBBd84H7f9bMXbr4Jkt8h9"

def fetch_wallet_data(wallets):
    base_url = "https://api.covalenthq.com/v1/1/address/{}/balances_v2/"
    headers = {"accept": "application/json"}

    all_data = []

    for wallet in wallets:
        print(f"[*] Fetching data for wallet: {wallet}")
        url = base_url.format(wallet)
        params = {"key": COVALENT_API_KEY}

        try:
            res = requests.get(url, headers=headers, params=params)
            data = res.json()

            if data.get("error"):
                print(f"[!] Failed for wallet {wallet}: {data.get('error_message')}")
                continue

            wallet_info = {
                "wallet": wallet,
                "total_usd_value": 0.0,
                "eth_balance": 0.0,
                "has_cTokens": False,
                "num_tokens": 0
            }

            tokens = data["data"]["items"]
            wallet_info["num_tokens"] = len(tokens)

            for token in tokens:
                symbol = token.get("contract_ticker_symbol", "")
                quote = token.get("quote", 0.0)
                wallet_info["total_usd_value"] += quote

                if symbol.lower() == "eth":
                    wallet_info["eth_balance"] = quote

                if symbol.lower().startswith("c"):  # compound token (e.g., cUSDC)
                    wallet_info["has_cTokens"] = True

            all_data.append(wallet_info)

        except Exception as e:
            print(f"[!] Exception for wallet {wallet}: {str(e)}")

        time.sleep(0.2)  # avoid rate limits

    return all_data
