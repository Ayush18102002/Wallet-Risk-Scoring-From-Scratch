# main.py

import sys
import os
import pandas as pd

SRC_DIR = os.path.join(os.path.dirname(__file__), 'src')
sys.path.append(SRC_DIR)

from fetch_data import fetch_wallet_data
from feature_engineering import compute_features
from scoring import compute_risk_scores

def main():
    print("[*] Loading wallet addresses...")
    wallet_df = pd.read_csv("data/wallets.csv")
    wallets = wallet_df["wallet_id"].tolist()

    print(f"[*] Fetching data for {len(wallets)} wallets from Compound V2...")
    wallet_data = fetch_wallet_data(wallets)

    print("[*] Engineering features...")
    features_df = compute_features(wallet_data)
    features_df.to_csv("data/processed_features.csv", index=False)

    print("[*] Calculating risk scores...")
    scored_df = compute_risk_scores(features_df)
    scored_df.to_csv("data/wallet_risk_scores.csv", index=False)

    print("[✔] Risk scoring complete. Output saved to data/wallet_risk_scores.csv")

if __name__ == "__main__":
    main()
