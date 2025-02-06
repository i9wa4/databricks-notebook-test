# Databricks notebook source
# MAGIC %md
# MAGIC # Databricks ノートブック管理テスト
# MAGIC
# MAGIC - 通常は Databricks 上のノートブックは .ipynb 形式で保存される
# MAGIC - "File -> Notebook format -> Source" でノートブックの保存形式を変更すると特殊な .py 形式で保存できるようになり Output はコミットされない状態となる！

# COMMAND ----------

print('Hello, World!')

# COMMAND ----------

import os

os.path.basename(os.getcwd())
