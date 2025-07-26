# src/feature_engineering.py

import pandas as pd

def compute_features(wallet_data):
    print("[*] Engineering features...")

    records = []

    for entry in wallet_data:
        records.append({
            "wallet": entry["wallet"],
            "total_usd_value": entry["total_usd_value"],
            "eth_balance": entry["eth_balance"],
            "has_cTokens": int(entry["has_cTokens"]),  # convert bool to int
            "num_tokens": entry["num_tokens"]
        })

    return pd.DataFrame(records)
