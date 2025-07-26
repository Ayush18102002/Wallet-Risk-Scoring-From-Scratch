# src/scoring.py

import pandas as pd
from src.utilis import normalize_column

def compute_risk_scores(df):
    print("[*] Calculating risk scores...")

    # Normalize the selected columns
    df['norm_usd'] = normalize_column(df['total_usd_value'])
    df['norm_eth'] = normalize_column(df['eth_balance'])
    df['norm_tokens'] = normalize_column(df['num_tokens'])

    # Simple scoring logic: higher balance = lower risk
    df['risk_score'] = 1 - (0.4 * df['norm_usd'] + 0.3 * df['norm_eth'] + 0.2 * df['norm_tokens'] - 0.1 * df['has_cTokens'])

    # Ensure scores stay between 0 and 1
    df['risk_score'] = df['risk_score'].clip(0, 1)

    return df[['wallet', 'risk_score']]
