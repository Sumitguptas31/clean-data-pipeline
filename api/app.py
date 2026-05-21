from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

import pandas as pd

from io import StringIO
import os

from src.datacleaner import clean_data
from src.datasummary import data_summary

app = FastAPI(
    title="Clean Data Pipeline API",
    description="API for cleaning CSV files and generating summaries",
    version="1.0.0"
)

# -----------------------------
# CORS Configuration
# -----------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# Create Required Folders
# -----------------------------

os.makedirs("data/raw", exist_ok=True)
os.makedirs("data/cleaned", exist_ok=True)

# -----------------------------
# Home Route
# -----------------------------

@app.get("/")
def home():
    return {
        "message": "Clean Data Pipeline API Running"
    }

# -----------------------------
# CSV Upload + Cleaning Endpoint
# -----------------------------

@app.post("/summary")
async def upload_csv(
    file: UploadFile = File(...)
):

    try:

        # Validate file type
        if not file.filename.endswith(".csv"):
            return {
                "error": "Only CSV files are allowed"
            }

        # Read uploaded content
        content = await file.read()

        # -----------------------------
        # Save Original File
        # -----------------------------

        raw_file_path = (
            f"data/raw/{file.filename}"
        )

        with open(raw_file_path, "wb") as f:
            f.write(content)

        # -----------------------------
        # Convert to DataFrame
        # -----------------------------

        decoded_content = content.decode("utf-8")

        df = pd.read_csv(
            StringIO(decoded_content)
        )

        # -----------------------------
        # Clean Data
        # -----------------------------

        before_rows = len(df)

        cleaned_df = clean_data(
            df,
            drop_nulls=True,
            trim_whitespace=True
        )

        after_rows = len(cleaned_df)

        # -----------------------------
        # Save Cleaned File
        # -----------------------------

        cleaned_file_path = (
            f"data/cleaned/cleaned_{file.filename}"
        )

        cleaned_df.to_csv(
            cleaned_file_path,
            index=False
        )

        # -----------------------------
        # Generate Summary
        # -----------------------------

        summary = data_summary(
            cleaned_df
        )

        # -----------------------------
        # Final API Response
        # -----------------------------

        return {

            "message": (
                "File cleaned successfully"
            ),

            "raw_file": raw_file_path,

            "cleaned_file": (
                cleaned_file_path
            ),

            "cleaning_report": {

                "rows_before_cleaning": (
                    before_rows
                ),

                "rows_after_cleaning": (
                    after_rows
                ),

                "rows_removed": (
                    before_rows - after_rows
                )
            },

            "summary": summary
        }

    except pd.errors.EmptyDataError:

        return {
            "error": "CSV file is empty"
        }

    except FileNotFoundError:

        return {
            "error": "File not found"
        }

    except Exception as e:

        return {
            "error": str(e)
        }