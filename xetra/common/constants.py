"""
File to store constants
"""
from enum import Enum


class S3FileTypes(Enum):
    """
    Supported file types for S3BucketConnector
    """
    CSV = 'csv'
    PARQUET = 'parquet'


class MetaProcessFormat(Enum):
    """
    formation for MetaProcess class
    """

    DATE_FORMAT = '%Y-%m-%d'
    DATE_FORMAT_LONG = '%Y-%m-%d %H:%M:%S'
    SOURCE_DATE_COL = 'source_date'
    PROCESS_COL = 'processing_timestamp'
    FILE_FORMAT = 'csv'
