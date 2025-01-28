import random
from time import sleep
from mpire import WorkerPool
import fireducks.pandas as pandas
from django.db import transaction
from django.db.utils import OperationalError
from query_engine.models import ChromosomeRegion, VaraDB_TFChipSeq

df = pandas.read_feather("database/datasets/combined_TF_Chip_for_main_database.feather")


def bulk_insert(chunk):
    chunked_df = df.iloc[chunk[0] : chunk[1]]
    try:
        with transaction.atomic():
            chromosome_regions = [
                ChromosomeRegion(
                    chr=row["Chr"],
                    end=row["End"],
                    start=row["Start"],
                    type="VaraDB_TFChipSEQ",
                )
                for _, row in chunked_df.iterrows()
            ]
            sleep_time = random.uniform(1, 10)
            sleep(sleep_time)
            ChromosomeRegion.objects.bulk_create(chromosome_regions)
            return True
    except OperationalError as e:
        sleep_time = random.uniform(20, 30)
        sleep(sleep_time)
        return chunk


chunks = []
chunk_size = 10000
for i in range(0, len(df), chunk_size):
    chunks.append([[i, min(i + chunk_size, len(df))]])

with WorkerPool(n_jobs=40) as pool:
    results = pool.map(
        bulk_insert,
        chunks,
        progress_bar=True,
    )
