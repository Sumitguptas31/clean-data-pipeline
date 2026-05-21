import subprocess
import json
import pandas as pd
from pathlib import Path


def test_main_cli_success(tmp_path):
    """
    Test successful CLI execution.
    """

    # Create sample CSV
    sample_data = pd.DataFrame({
        "name": [" Sumit ", "Sumit"],
        "email": [
            "test@gmail.com",
            "test@gmail.com"
        ]
    })

    input_file = tmp_path / "input.csv"
    output_file = tmp_path / "output.csv"

    sample_data.to_csv(input_file, index=False)

    # Run CLI command
    result = subprocess.run(
        [
            "python",
            "main.py",
            "--input",
            str(input_file),
            "--output",
            str(output_file),
            "--trim"
        ],
        capture_output=True,
        text=True
    )

    # Ensure command succeeded
    assert result.returncode == 0

    # Ensure output file created
    assert output_file.exists()

    # Parse printed JSON summary
    summary = json.loads(result.stdout)

    # Validate summary keys
    assert "rows" in summary
    assert "columns" in summary
    assert "missing_values" in summary


def test_main_missing_file():
    """
    Test CLI with missing input file.
    """

    result = subprocess.run(
        [
            "python",
            "main.py",
            "--input",
            "missing.csv",
            "--output",
            "output.csv"
        ],
        capture_output=True,
        text=True
    )

    # Program should fail
    assert result.returncode != 0

    # Error message should appear
    assert "File not found" in (
        result.stderr + result.stdout
    )