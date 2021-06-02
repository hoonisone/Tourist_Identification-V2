# Tourist-Identification
Tourist Identification from Public Transportation Passengers Considering the Types of Access to A Tourist City

# 1. How To Use
### 1.1 set data attribute name
  * you can modify attribute names on lib/config.py
  * if your data has USER_ID named "userId" you must change the content like USER_ID = "userId"

### 1.2 data range
  * you can ditermine data range modifying START_DATA and END_DATA value on lib/config.py
  * if you want 2020/1/1 ~ 2020/12/31 you can change like next:
  <pre>
  <code>
    START_DATE = datetime.datetime(2020, 1, 1)
    END_DATE = datetime.datetime(2020, 12, 31)
  </code>
  </pre>
