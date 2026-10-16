"""CFPB Consumer Complaint Database ingestion.

Pulls incremental complaint records from the CFPB public API and saves them
as raw files for loading into the Bronze layer.
"""


def fetch_complaints(date_received_min, date_received_max, size):
    """Fetch complaints received between two dates from the CFPB API.

    Args:
        date_received_min: Start of the date range (inclusive).
        date_received_max: End of the date range (inclusive).
        size: Maximum number of records to return.

    Returns:
        A pandas DataFrame of raw complaint records.
    """
    pass


def save_raw(df, path):
    """Save a raw complaints DataFrame to disk.

    Args:
        df: DataFrame of raw complaint records.
        path: Destination file path (e.g. under data/raw/).
    """
    pass
