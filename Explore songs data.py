%fs ls "/databricks-datasets/songs/data-001"

%fs head --maxBytes=10000 "/databricks-datasets/songs/README.md"

%fs ls "/databricks-datasets/songs/data-001"

%fs head --maxBytes=10000 "/databricks-datasets/songs/data-001/part-00000"

df = spark.read.format('csv').option("sep", "\t").load('dbfs:/databricks-datasets/songs/data-001/part-00000')
df.display()