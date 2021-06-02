# Tourist-Identification
**Tourist Identification from Public Transportation Passengers Considering the Types of Access to A Tourist City**

**관광도시 출입 유형을 고려한 대중교통 이용 관광객 식별 알고리즘 개선**

- Authors: 한명훈* (jrngl3527@jejunu.ac.kr) 김예찬* (yechankim@gm.gist.ac.kr) 김성백 (sbkim@jejunu.ac.kr)

## Novelty
- `암호화`된 대중교통 이용 데이터에서 `제주 관광객`을 더욱 정확하게 `식별`하기 위해, `관광도시 출입 유형`을 고려하여 종래에 제안한 [알고리즘](https://doi.org/10.5626/KTCP.2020.26.8.349)의 성능을 더욱 향상시켰습니다. 세부사항은 [논문]()을 참고하시기 바랍니다.


## Prerequisites
- Python 3.7.4
- Pandas 0.25.1
- Tqdm 4.48.2

## How to use
### 1. set a name of attribute on lib/config.py
  * if your data has USER_ID named "userId" you must change the content like following
  <pre><code>
    USER_ID = "userId"
  </code></pre>
  
### 2. set a value of data range on lib/config.py
  * if you want 2020/1/1 ~ 2020/12/31 you can change like following:
  <pre><code>
    START_DATE = datetime.datetime(2020, 1, 1)
    END_DATE = datetime.datetime(2020, 12, 31)
  </code></pre>

### 3. set the parameters on lib/config.py
  <pre><code>
  EXTRACT_PARAS = [{"case":"both",    "stay_period":(2, 10), "use_ratio":70, "tour_station_count": 1},
                   {"case":"first",   "stay_period":(2, 10), "use_ratio":70, "tour_station_count": 3},
                   {"case":"last",    "stay_period":(2, 10), "use_ratio":80, "tour_station_count": 3},
                   {"case":"neither", "stay_period":(2, 10), "use_ratio":90, "tour_station_count": 4}]
  </code></pre>

### 4. run following
  * main/1.1 Extract user and station

### 5. after running you can find following on data/analysys
  * station.csv
  * user.csv

## Data sample
|attribute|value|
|------|------|
|user_id|f6f372cf8c6732eafc2a82b4f9d7a08bb3b493213ea4efbd3f4bba1d058406a7|
|base_date|20190601|
|route_id|22610000|
|route_name|292-2(한림체육관~제주버스터미널(종점))|
|rout_no|292-2|
|geton_datetime|20190601150225|
|geton_station_id|988|
|geton_stataion_name|납읍리사무소|
|geton_station_longitude|126.32944|
|geton_station_latitude|33.43944|
|getoff_datetime|20190601151638|
|getoff_station_id|26|
|getoff_stataion_name|하귀초등학교|
|getoff_station_longitude|126.40212|
|getoff_station_latitude|33.48017|
|user_type|일반|
|user_count|1|
|input_date|20190603|

## Performance



## Cautions
- 이 알고리즘은 [제주 빅데이터 센터](https://bc.jejudatahub.net/main)에서 제공하는 제주 대중교통 버스 교통카드 빅데이터(tb_bus_user_usage, 버스 이용 데이터)에 최적화되어 있습니다.

## Notice
- 본 소스코드를 이용하여 수행한 연구 결과를 논문이나 보고서 등의 형태의 산출물로 게재할 경우, 그 산출물에 하단 레퍼런스를 반드시 인용해야 합니다.
- 인용 포맷은 게재하는 논문이나 보고서의 규정을 준수하시면 됩니다.

>[국문 예시]
한명훈, 김예찬, 김성백, "관광도시 출입 유형을 고려한 대중교통 이용 관광객 식별 알고리즘 개선," 정보과학회 컴퓨팅의 실제 논문지, Vol. --, No. -, pp. 000-000, 2021.
>[영문 예시]
Myunghun Han, Yechan Kim and Seong-Baeg Kim, "An Enhanced Algorithm for Tourist Identification from Public Transportation Passengers Considering the Types of Access to a Tourist City," KIISE Transactions on Computing Practices, Vol. --, No. -, pp. 000-000, 2021. (in Korean)
