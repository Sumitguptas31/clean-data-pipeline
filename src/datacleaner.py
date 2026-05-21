import logging
import pandas as pd

from src.utils import (
    trim_whitespace as trim_whitespace_func,
    remove_duplicates,
    drop_null_rows
)

logger = logging.getLogger(__name__)


def clean_data(
    df: pd.DataFrame,
    drop_nulls: bool = False,
    trim_whitespace: bool = False,
    duplicate_subset: list[str] | None = None
) -> pd.DataFrame:

    before_rows = len(df)

    logger.info(
        f"Rows before cleaning: {before_rows}"
    )

    if trim_whitespace:
        df = trim_whitespace_func(df)

    if drop_nulls:
        df = drop_null_rows(df)

    df = remove_duplicates(
        df,
        subset=duplicate_subset
    )

    after_rows = len(df)

    logger.info(
        f"Rows after cleaning: {after_rows}"
    )

    return df