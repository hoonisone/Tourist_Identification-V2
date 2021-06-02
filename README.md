# Tourist-Identification
Tourist Identification from Public Transportation Passengers Considering the Types of Access to A Tourist City

# 1. How To Use
### 1.1 set a name of attribute on lib/config.py
  * if your data has USER_ID named "userId" you must change the content like following
  <pre><code>
    USER_ID = "userId"
  </code></pre>
  
### 1.2 set a value of data range on lib/config.py
  * if you want 2020/1/1 ~ 2020/12/31 you can change like following:
  <pre><code>
    START_DATE = datetime.datetime(2020, 1, 1)
    END_DATE = datetime.datetime(2020, 12, 31)
  </code></pre>

### 1.3 set the parameters on lib/config.py
  <pre><code>
  EXTRACT_PARAS = [{"case":"both",    "stay_period":(2, 10), "use_ratio":70, "tour_station_count": 1},
                   {"case":"first",   "stay_period":(2, 10), "use_ratio":70, "tour_station_count": 3},
                   {"case":"last",    "stay_period":(2, 10), "use_ratio":80, "tour_station_count": 3},
                   {"case":"neither", "stay_period":(2, 10), "use_ratio":90, "tour_station_count": 4}]
  </code></pre>

### 1.4 run all of "1.1 Extract user and station"
