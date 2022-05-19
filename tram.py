import pandas as pd

df = pd.read_csv("stop_times.csv")

df = df.drop(df.columns[[1, 2,5,6,7,8,9]], axis=1)

trip_1_only = df.set_index("trip_id").filter(like="_trip_1_service_1", axis=0)

trip_1_only.to_csv("out.txt")
