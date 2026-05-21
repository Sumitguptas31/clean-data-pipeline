import argparse
import json
from dataloader import load_csv
from datacleaner import clean_data
from datasummary import data_summary
import src.loggerfile

def main():
    parser = argparse.ArgumentParser(description="Clean CSV data")

    parser.add_argument("--input", required=True, help="Input CSV path")
    parser.add_argument("--output", required=True, help="Output CSV path")

    parser.add_argument(
        "--drop-null",
        action="store_true",
        help="Drop rows containing null values"
    )

    parser.add_argument(
        "--trim",
        action="store_true",
        help="Trim whitespace from string columns"
    )

    parser.add_argument(
        "--subset",
        type=str,
        help="Columns for duplicate removal separated by commas"
    )

    args = parser.parse_args()

    subset_columns = (
        args.subset.split(",") if args.subset else None
    )

    df = load_csv(args.input)

    cleaned_df = clean_data(
        df,
        drop_nulls=args.drop_null,
        trim_whitespace=args.trim,
        duplicate_subset=subset_columns
    )

    cleaned_df.to_csv(args.output, index=False)

    summary = data_summary(cleaned_df)

    print(json.dumps(summary, indent=4))


if __name__ == "__main__":
    main()