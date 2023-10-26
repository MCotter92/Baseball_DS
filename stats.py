import math
import pandas as pd


def BA(hits, ABs):
    return hits / ABs


def AtBats(data):
    df = pd.DataFrame(data)
    return df.shape[0]
