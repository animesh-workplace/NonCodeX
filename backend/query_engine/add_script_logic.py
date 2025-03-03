# import os

# from query_engine.models import ChromosomeRegion


# df = pandas.read_csv(file, sep="\t")
# df["Type"] = "VaraDB_Disease_Enhancer"
# start_len = ChromosomeRegion.objects.latest("id").id
# df["id"] = list(range(start_len + 1, start_len + len(df) + 1))
# df[["id", "Chr", "Start", "End", "Type"]].to_csv(
#     f"main_{file}", sep=",", index=False, header=False
# )
# df.drop(columns=["Chr", "Start", "End", "Type"]).to_csv(
#     f"sub_{file}", sep=",", index=True, header=False
# )

# # Run subprocess on the following command
# # sqlite3 db.sqlite3 ".mode csv" ".import <sub_file> <sub_db>"
# # sqlite3 db.sqlite3 ".mode csv" ".import <main_file> query_engine_chromosomeregion"

import subprocess, argparse, os
import fireducks.pandas as pandas
from query_engine.models import ChromosomeRegion


def process_and_upload(file_name: str, file_type: str, sub_db_name: str):
    # Read the input file
    df = pandas.read_csv(file_name, sep="\t")
    df["Type"] = file_type

    # Generate unique IDs
    start_len = ChromosomeRegion.objects.latest("id").id
    df["id"] = list(range(start_len + 1, start_len + len(df) + 1))

    # Generate output filenames
    main_file = f"datasets/main_{file_name}.csv"
    sub_file = f"datasets/sub_{file_name}.csv"

    # Save main file (subset of columns)
    df[["id", "Chr", "Start", "End", "Type"]].to_csv(
        main_file, sep=",", index=False, header=False
    )

    # Save sub file (dropping some columns)
    df.drop(columns=["Chr", "Start", "End", "Type"]).to_csv(
        sub_file, sep=",", index=True, header=False
    )

    # Run SQLite import commands
    db_name = "db.sqlite3"  # Change this if using a different DB file
    subprocess.run(
        [
            "sqlite3",
            db_name,
            ".mode csv",
            f".import {main_file} query_engine_chromosomeregion",
        ]
    )
    subprocess.run(
        ["sqlite3", db_name, ".mode csv", f".import {sub_file} {sub_db_name}"]
    )

    print("Data successfully uploaded!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Upload a file into SQLite DB")
    parser.add_argument("file_name", type=str, help="File to be uploaded")
    parser.add_argument("sub_db_name", type=str, help="Sub-table name in SQLite DB")
    parser.add_argument(
        "file_type", type=str, help="Provide the type for database entry"
    )

    args = parser.parse_args()
    process_and_upload(args.file_name, args.file_type, args.sub_db_name)
