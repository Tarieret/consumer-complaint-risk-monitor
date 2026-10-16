"""FDIC bank institution data ingestion.

Pulls institution-level data (including total assets) from the FDIC API for
peer-group benchmarking, and saves it as raw files for the Bronze layer.
"""


def fetch_institutions():
    """Fetch FDIC institution records, including bank asset data.

    Returns:
        A pandas DataFrame of raw institution records.
    """
    pass


def save_raw(df, path):
    """Save a raw institutions DataFrame to disk.

    Args:
        df: DataFrame of raw institution records.
        path: Destination file path (e.g. under data/raw/).
    """
    pass
