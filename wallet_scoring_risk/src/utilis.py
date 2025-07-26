def normalize_column(col):
    min_val = col.min()
    max_val = col.max()
    if max_val == min_val:
        return col.apply(lambda x: 0.0)
    return (col - min_val) / (max_val - min_val)
