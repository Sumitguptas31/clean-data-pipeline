import pytest
from src.dataloader import load_csv


def test_load_csv_success():
    df = load_csv("tests/sample.csv")

    assert len(df) > 0


def test_load_csv_missing_file():

    with pytest.raises(FileNotFoundError):
        load_csv("missing.csv")