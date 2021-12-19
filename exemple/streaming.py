# 스파크 스트리밍 간단한 예제
# 소켓으로 스트리밍을 받아 단어를 카운트 해주는 간단한 프로그램
# 아웃풋 스트림으로 콘솔로 내보낸다.

# 라이브러리
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

# 스파크 인스턴스 생성
spark = SparkSession.builder.appName("stream-word-count").getOrCreate()

# 리드 스트림 명시
# 소켓으로부터 읽어온다.
# 옵션으로 호스트와 포트 명시
lines_df = spark.readStream.format("socket").option("host", "localhost").option("port", "9999").load()

# 일반적인 df처럼 사용
# expr: sql문을 select안에서 사용할 수 있게 해주는 함수
# 공백 기준으로 스플릿을 한 후 explode하라는 뜻이다.
words_df = lines_df.select(expr("explode(split(value, ' ')) as word"))

# 쪼갠 워드를 카운트한다.
counts_df = words_df.groupBy("word").count()

# 콘솔로 내보내준다.
word_count_query = counts_df.writeStream.format("console")\
                            .outputMode("complete")\
                            .option("checkpointLocation", ".checkpoint")\
                            .start()
word_count_query.awaitTermination()