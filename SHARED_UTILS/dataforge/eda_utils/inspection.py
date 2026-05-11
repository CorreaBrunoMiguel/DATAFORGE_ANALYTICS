import pandas as pd


def dataset_overview(df: pd.DataFrame) -> None:
    """
    Exibe visão geral inicial de um DataFrame.
    """

    print("\n=== DATASET SHAPE ===")
    print(df.shape)

    print("\n=== COLUMN TYPES ===")
    print(df.dtypes)

    print("\n=== MISSING VALUES ===")
    print(df.isna().sum())

    print("\n=== DUPLICATED ROWS ===")
    print(df.duplicated().sum())
