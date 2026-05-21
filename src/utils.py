import pandas as pd


def trim_whitespace(df: pd.DataFrame) -> pd.DataFrame:
    """
    Trim leading and trailing spaces
    from string columns.

    Args:
        df: Input dataframe

    Returns:
        Cleaned dataframe
    """

    object_columns = df.select_dtypes(
        include=["object"]
    ).columns

    for col in object_columns:
        df[col] = df[col].str.strip()

    return df


def remove_duplicates(
    df: pd.DataFrame,
    subset: list[str] | None = None
) -> pd.DataFrame:
    """
    Remove duplicate rows.

    Args:
        df: Input dataframe
        subset: Columns used for duplicate detection

    Returns:
        Dataframe without duplicates
    """

    return df.drop_duplicates(subset=subset)


def drop_null_rows(
    df: pd.DataFrame
) -> pd.DataFrame:
    """
    Remove rows containing null values.

    Args:
        df: Input dataframe

    Returns:
        Cleaned dataframe
    """

    return df.dropna()