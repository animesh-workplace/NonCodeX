import random
from time import sleep
from mpire import WorkerPool
import fireducks.pandas as pandas
from django.db import transaction
from django.db.utils import OperationalError
from query_engine.models import ChromosomeRegion, VaraDB_TFChipSeq

df = pandas.read_feather("database/datasets/combined_TF_Chip_for_database.feather")


def bulk_insert(chunk):
    chunked_df = df.iloc[chunk[0] : chunk[1]]
    try:
        with transaction.atomic():
            # Create ChromosomeRegion objects
            chromosome_regions = []
            tf_chipseq_objects = []

            for _, row in chunked_df.iterrows():
                chr_region = ChromosomeRegion(
                    chr=row["Chr"],
                    end=row["End"],
                    start=row["Start"],
                    type="VaraDB_TFChipSEQ",
                )
                chromosome_regions.append(chr_region)

            # Insert chromosome regions and get their IDs
            sleep_time = random.uniform(1, 10)
            sleep(sleep_time)
            ChromosomeRegion.objects.bulk_create(chromosome_regions)

            # Create VaraDB_TFChipSeq objects with references to chromosome regions
            for chr_region, (_, row) in zip(chromosome_regions, chunked_df.iterrows()):
                tf_chipseq = VaraDB_TFChipSeq(
                    tf=row["TF"],
                    source=row["Source"],
                    tf_class=row["TF_Class"],
                    chromosome_region=chr_region,
                    biosample_type=row["Biosample_Type"],
                    biosample_name=row["Biosample_Name"],
                )
                tf_chipseq_objects.append(tf_chipseq)

            # Bulk create TF ChIP-seq objects
            sleep_time = random.uniform(1, 10)
            sleep(sleep_time)
            VaraDB_TFChipSeq.objects.bulk_create(tf_chipseq_objects)
            return True
    except OperationalError as e:
        sleep_time = random.uniform(20, 30)
        sleep(sleep_time)
        return chunk


chunks = []
chunk_size = 10000
for i in range(0, len(df), chunk_size):
    chunks.append([[i, min(i + chunk_size, len(df))]])

with WorkerPool(n_jobs=50) as pool:
    results = pool.map(bulk_insert, chunks, progress_bar=True)
