"""メインロジック"""

from pyspark.sql import DataFrame, SparkSession

from common.utils import greet


def load_table(spark: SparkSession, table_name: str, limit: int) -> DataFrame:
    """テーブルからデータを読み込む"""
    return spark.table(table_name).limit(limit)


def main(table_name: str, limit: int = 10) -> None:
    """メイン処理"""
    spark = SparkSession.builder.getOrCreate()
    print(greet("Databricks"))
    df = load_table(spark, table_name, limit)
    df.show()
