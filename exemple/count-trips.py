from pyspark import SparkConf, SparkContext
import pandas as pd

# Spark 설정
# SparkConf를 이용해 Master/Local 설정을 하고, 앱 이름을 정해준다.
conf = SparkConf().setMaster("local").setAppName("uber-date-trips")
# conf라는 객체를 SparkContext를 초기화 하는 데 사용한다.
sc = SparkContext(conf=conf)
 
# 데이터 파싱
lines = sc.textFile("/Users/6mini/spark/fhvhv_tripdata_2020-03.csv")
header = lines.first()
filtered_lines = lines.filter(lambda row:row != header) 

# 필요한 부분만 골라내서 세는 부분
# countByValue로 같은 날짜가 등장하는 부분을 센다.
dates = filtered_lines.map(lambda x: x.split(",")[2].split(" ")[0])
result = dates.countByValue()

# Spark코드가 아닌 일반적인 파이썬 코드
# CSV로 결과값 저장 
pd.Series(result, name="trips").to_csv("trips-date.csv")