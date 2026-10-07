from pyspark.sql import SparkSession
from pyspark.sql.functions import lower,col,trim

spark=SparkSession.builder.appName("").getOrCreate()

donnee=spark.read.csv("donnees_rh_sale.csv",header=True)
donnee=donnee.withColumn("prenom_nom",lower(trim(col("prenom_nom"))))
donnee.show(100,False)