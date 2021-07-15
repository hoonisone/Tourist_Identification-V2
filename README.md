# Tourist Identification

**An Enhanced Algorithm for Tourist Identification from Public Transportation Passengers Considering the Types of Access to A Tourist City**

**관광도시 출입 유형을 고려한 대중교통 이용 관광객 식별 알고리즘 개선**

- Authors:
  - [MyungHun Han*](https://sites.google.com/view/hoonisone)    
  - [Yechan Kim*](https://sites.google.com/view/yechankim)    
  - [Seong Baeg Kim](https://education.jejunu.ac.kr/education/department/educom.htm)

## Novelty
- This repository includes enhanced algorithm for `Jeju tourist identification` from `encrpyted` public transportation dataset considering the `types of access to Jeju`. Kindly read the [paper](https://doi.org/10.5626/KTCP.2021.27.7.314) for details.
- 본 GitHub 레퍼지토리는`암호화`된 대중교통 이용 데이터에서 `제주 관광객`을 더욱 정확하게 `식별`하기 위해, `관광도시 (제주) 출입 유형`을 고려하여 종래에 제안한 [알고리즘](https://doi.org/10.5626/KTCP.2020.26.8.349)을 개선한 알고리즘의 소스코드를 제공합니다. 세부사항은 [논문](https://doi.org/10.5626/KTCP.2021.27.7.314)을 참고하시기 바랍니다.

## Prerequisites
- Python
- Pandas 
- Tqdm

## How to use
### 1. Set each name of attributes in `lib/config.py` as follows:
  <pre><code>
    USER_ID = "userId" # check header of your CSV file!
  </code></pre>
  
### 2. Set a date range on `lib/config.py` as follows:
  <pre><code>
    # If you want to extract tourists from Jan 1, 2020 to December 31, 2020
    START_DATE = datetime.datetime(2020, 1, 1)
    END_DATE = datetime.datetime(2020, 12, 31)
  </code></pre>

### 3. Set the hyper-parameters on `lib/config.py` as follows:
  <pre><code>
  # Our paper contains the explanation of each hyperparameter. Try to check it!
  EXTRACT_PARAS = [
    {"case":"both",    "stay_period":(2, 10), "use_ratio":70, "tour_station_count": 1},
    {"case":"first",   "stay_period":(2, 10), "use_ratio":70, "tour_station_count": 3},
    {"case":"last",    "stay_period":(2, 10), "use_ratio":80, "tour_station_count": 3},
    {"case":"neither", "stay_period":(2, 10), "use_ratio":90, "tour_station_count": 4}
  ]
  </code></pre>

### 4. Run `main/1.1 Extract user and station.ipynb` through jupyter notebook.

### 5. After 4, you can obtain the following results in 'data/analysis':
  * station.csv
  * user.csv

## Example of dataset
### This algorithm works only in the dataset as follows:
|attribute|value|
|------|------|
|user_id|f6f372cf8c6732eafc2a82b4f9d7a08bb3b493213ea4efbd3f4bba1d058406a7|
|base_date|20190601|
|route_id|22610000|
|route_name|292-2(한림체육관~제주버스터미널(종점))|
|route_no|292-2|
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

- Visit [Jeju Big-data center](https://bc.jejudatahub.net/main) to get `tb_bus_user_usage` dataset for further experiments.

## Cite this paper:

>[In Korean]
한명훈, 김예찬, 김성백, "관광도시 출입 유형을 고려한 대중교통 이용 관광객 식별 알고리즘 개선," 정보과학회 컴퓨팅의 실제 논문지, Vol. 27, No. 7, pp. 314-324, 2021.

>[In English]
Myunghun Han, Yechan Kim and Seong-Baeg Kim, "An Enhanced Algorithm for Tourist Identification from Public Transportation Passengers Considering the Types of Access to a Tourist City," KIISE Transactions on Computing Practices, Vol. 27, No. 7, pp. 314-324, 2021.
