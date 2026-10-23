# Databricks notebook source
from pyspark.sql.functions import *
from pyspark.sql.types import *

# COMMAND ----------

# COMMAND ----------

# MAGIC %md
# MAGIC ### Data loading

# COMMAND ----------

df_calender = spark.read.format("csv")\
    .option("header",True)\
    .option("inferSchema",True)\
    .load('abfss://bronze@adventureorksdatalake.dfs.core.windows.net/AdventureWorks_Calendar')

# COMMAND ----------

df_cust = spark.read.format("csv")\
    .option("header",True)\
    .option("inferSchema",True)\
    .load('abfss://bronze@adventureorksdatalake.dfs.core.windows.net/AdventureWorks_Customers')

# COMMAND ----------

df_prodcat = spark.read.format("csv")\
    .option("header",True)\
    .option("inferSchema",True)\
    .load('abfss://bronze@adventureorksdatalake.dfs.core.windows.net/AdventureWorks_Product_Categories')

# COMMAND ----------

df_prodreturn = spark.read.format("csv")\
    .option("header",True)\
    .option("inferSchema",True)\
    .load('abfss://bronze@adventureorksdatalake.dfs.core.windows.net/AdventureWorks_Product_Returns')

# COMMAND ----------

df_prodsubcat = spark.read.format("csv")\
    .option("header",True)\
    .option("inferSchema",True)\
    .load('abfss://bronze@adventureorksdatalake.dfs.core.windows.net/AdventureWorks_Product_Subcategories')

# COMMAND ----------

df_prod = spark.read.format("csv")\
    .option("header",True)\
    .option("inferSchema",True)\
    .load('abfss://bronze@adventureorksdatalake.dfs.core.windows.net/AdventureWorks_Products')

# COMMAND ----------

df_sales = spark.read.format("csv")\
    .option("header",True)\
    .option("inferSchema",True)\
    .load('abfss://bronze@adventureorksdatalake.dfs.core.windows.net/AdventureWorks_Sales*')

# COMMAND ----------

df_Territ = spark.read.format("csv")\
    .option("header",True)\
    .option("inferSchema",True)\
    .load('abfss://bronze@adventureorksdatalake.dfs.core.windows.net/AdventureWorks_Territories')

# COMMAND ----------

# MAGIC %md
# MAGIC ### Silver transformations

# COMMAND ----------

df_calender = df_calender.withColumn('month',month(col('Date')))

# COMMAND ----------

df_calender = df_calender.withColumn('year',year(col('Date')))

# COMMAND ----------

df_calender.write.format('parquet').mode('append').option("path","abfss://silver@adventureorksdatalake.dfs.core.windows.net/AdventureWorks_Calendar").save()

# COMMAND ----------

df_cust = df_cust.withColumn("full_name",concat(col('Prefix'),lit(" "),col('FirstName'),lit(" "),col('LastName')))

# COMMAND ----------

df_cust.write.mode("append").format("parquet").option("path", "abfss://silver@adventureorksdatalake.dfs.core.windows.net/AdventureWorks_Customers").save()

# COMMAND ----------

df_prodsubcat.write.mode("append").format("parquet").option("path", "abfss://silver@adventureorksdatalake.dfs.core.windows.net/AdventureWorks_Product_Subcategories").save()

# COMMAND ----------

df_prod = df_prod.withColumn("ProductSKU",split(col("ProductSKU"),"-")[0])\
    .withColumn("ProductName",split(col("ProductName"),",")[0])

# COMMAND ----------

df_prod.write.mode("append").format("parquet").option("path", "abfss://silver@adventureorksdatalake.dfs.core.windows.net/AdventureWorks_Products").save()

# COMMAND ----------

df_prodreturn.write.mode("append").format("parquet").option("path", "abfss://silver@adventureorksdatalake.dfs.core.windows.net/AdventureWorks_Product_Returns").save()

# COMMAND ----------

df_Territ.write.mode("append").format("parquet").option("path", "abfss://silver@adventureorksdatalake.dfs.core.windows.net/AdventureWorks_Territories").save()

# COMMAND ----------

df_sales.write.mode("append").format("parquet").option("path", "abfss://silver@adventureorksdatalake.dfs.core.windows.net/AdventureWorks_Sales").save()

# COMMAND ----------

df_prodcat.write.mode("append").format("parquet").option("path", "abfss://silver@adventureorksdatalake.dfs.core.windows.net/AdventureWorks_Product_Categories").save()