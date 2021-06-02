# Tourist-Identification
Tourist Identification from Public Transportation Passengers Considering the Types of Access to A Tourist City

# 1. How To Use
### 1.1 setting lib/config.py
##### 1.1.1 set a name of attribute
  * if your data has USER_ID named "userId" you must change the content like following
  <pre><code>
    USER_ID = "userId"
  </code></pre>
  
#### 1.1.2 set a value of data range
  * if you want 2020/1/1 ~ 2020/12/31 you can change like following:
  <pre><code>
    START_DATE = datetime.datetime(2020, 1, 1)
    END_DATE = datetime.datetime(2020, 12, 31)
  </code></pre>
