"""テスト"""

from unittest.mock import MagicMock

from common.utils import greet
from src.main import load_table


def test_greet():
    assert greet("World") == "Hello, World!"


def test_load_table():
    mock_spark = MagicMock()
    mock_df = MagicMock()
    mock_spark.table.return_value.limit.return_value = mock_df

    result = load_table(mock_spark, "test_table", 10)

    mock_spark.table.assert_called_once_with("test_table")
    mock_spark.table.return_value.limit.assert_called_once_with(10)
    assert result == mock_df
