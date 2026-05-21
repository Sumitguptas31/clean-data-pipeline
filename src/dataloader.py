import pandas as pd
from pandas.errors import EmptyDataError, ParserError


def load_csv(path: str) -> pd.DataFrame:
    """
    Load CSV file safely.

    Args:
        path: CSV file path

    Returns:
        pandas DataFrame
    """

    try:
        df = pd.read_csv(path)
        return df

    except FileNotFoundError:
        raise FileNotFoundError(
            f"ERROR: File not found -> {path}"
        )

    except EmptyDataError:
        raise ValueError(
            "ERROR: CSV file is empty"
        )

    except ParserError:
        raise ValueError(
            "ERROR: Invalid CSV format"
        )

    except Exception as e:
        raise Exception(
            f"Unexpected error while loading CSV: {str(e)}"
        )