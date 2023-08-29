import requests
import time

def query_loki_api():
    # Loki 在不指定 start参数和 end参数情况下 ，起始时间为1h 结束时间为当前时间。
    PROTOCOL = "http://"
    LOKI_API = "172.16.10.140:3100/loki/api/v1/query_range?"
    LOG_QL = 'limit=1000&query={job="varlogs"}'

    try:
        response = requests.get(PROTOCOL + LOKI_API + LOG_QL)
        data = response.json() # 将信息以 json 读取，赋值到 DATA
        print(data) # 打印 DATA
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e) # 捕获requests库中的RequestException异常并打印

while True:
    query_loki_api()
    time.sleep(3600)  # Delay for 1 hour