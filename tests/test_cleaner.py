import pandas as pd
from src.datacleaner import clean_data


def test_duplicate_removal():

    data = {
        "name": ["A", "A"],
        "email": ["x@gmail.com", "x@gmail.com"]
    }

    df = pd.DataFrame(data)

    cleaned = clean_data(df)

    assert len(cleaned) == 1