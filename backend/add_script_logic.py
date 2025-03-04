import fireducks.pandas as pandas
import subprocess, argparse, django, os

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "noncodex_backend.settings")
django.setup()

from query_engine.models import ChromosomeRegion


def process_and_upload(file_name: str, file_type: str, sub_db_name: str):
    # Read the input file
    df = pandas.read_csv(file_name, sep="\t")
    df["Type"] = file_type

    # Generate unique IDs
    start_len = ChromosomeRegion.objects.latest("id").id
    df["id"] = list(range(start_len + 1, start_len + len(df) + 1))

    # Generate output filenames
    main_file = f"database/datasets/main_{os.path.basename(file_name)}"
    sub_file = f"database/datasets/sub_{os.path.basename(file_name)}"

    # Save main file (subset of columns)
    df[["id", "Chr", "Start", "End", "Type"]].to_csv(
        main_file, sep=",", index=False, header=False
    )

    # Save sub file (dropping some columns)
    df.drop(columns=["Chr", "Start", "End", "Type"]).to_csv(
        sub_file, sep=",", index=True, header=False
    )

    # Run SQLite import commands
    db_name = "database/db.sqlite3"
    subprocess.run(
        [
            "sqlite3",
            db_name,
            "PRAGMA synchronous = OFF;",
            "PRAGMA journal_mode = MEMORY;",
            "PRAGMA cache_size = 1000000;",
            "PRAGMA temp_store = MEMORY;",
            ".mode csv",
            f".import {main_file} query_engine_chromosomeregion",
        ]
    )
    subprocess.run(
        [
            "sqlite3",
            db_name,
            "PRAGMA synchronous = OFF;",
            "PRAGMA journal_mode = MEMORY;",
            "PRAGMA cache_size = 1000000;",
            "PRAGMA temp_store = MEMORY;",
            ".mode csv",
            f".import {sub_file} {sub_db_name}",
        ]
    )

    print("Data successfully uploaded!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Upload a file into SQLite DB")
    parser.add_argument("--file_name", type=str, help="File to be uploaded")
    parser.add_argument("--sub_db_name", type=str, help="Sub-table name in SQLite DB")
    parser.add_argument(
        "--file_type", type=str, help="Provide the type for database entry"
    )

    args = parser.parse_args()
    process_and_upload(args.file_name, args.file_type, args.sub_db_name)
