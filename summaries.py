import pybaseball as pyb
import pandas as pd

RIZZO = pyb.playerid_lookup("rizzo", "anthony")
RIZZO_ID = RIZZO["key_mlbam"].iloc[0]
STARTDATE = "2012-01-01"
ENDDATE = "2020-12-31"

rizzo_batting = pyb.statcast_batter(STARTDATE, ENDDATE, RIZZO_ID)
print(type(rizzo_batting))
# pd.rizzo_batting.to_csv(
#     "/Users/mason_cotter/Desktop/python_projects/baseball_ds",
# )
