import os
import fireducks.pandas as pandas
from query_engine.models import ChromosomeRegion


txt_files = [f for f in os.listdir() if f.endswith(".txt")]

for file in txt_files:
    df = pandas.read_csv(file, sep="\t")
    df["Type"] = "VaraDB_Disease_Enhancer"
    start_len = ChromosomeRegion.objects.latest("id").id
    df["id"] = list(range(start_len, start_len + len(df)))
    df[["id", "Chr", "Start", "End", "Type"]].to_csv(
        f"main_{file}", sep="\t", index=True, header=False
    )
    df.drop(columns=["Chr", "Start", "End", "Type"]).to_csv(
        f"sub_{file}", sep="\t", index=True, header=False
    )
