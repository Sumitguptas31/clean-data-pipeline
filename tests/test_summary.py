import pandas as pd
from src.datasummary import data_summary


def test_summary_output():

    df = pd.DataFrame({
        "name": ["A", "B"],
        "age": [20, 30]
    })

    summary = data_summary(df)

    assert "rows" in summary
    assert "columns" in summary
    assert "missing_values" in summary