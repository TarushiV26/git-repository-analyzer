import pandas as pd

def branch_stats(branches):
    return pd.DataFrame(branches, columns=["Name", "Commit"])
