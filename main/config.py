import datetime


# data range
START_DATE = datetime.datetime(2019, 6, 1)
END_DATE = datetime.datetime(2019, 8, 29)

PROJECT_PATH = "./.."
DEFAULT_ENCODING = "cp949"
STATION_DF_PATH = "data/analysis/station_df.csv"
USER_DF_PATH = "data/analysis/user_df.csv"
TOUR_STATION_CANDIDATE_DF_PATH = "data/analysis/tour_station_candidate_df.csv"
USAGE_DF_PATH = "data/analysis/usage_df.csv"

# 공항과 항만에 대한 이름 후보(정류장 이름의 부분 문자열) 데이터
airport_candidate_list = ["제주국제공항"]
harbor_candidate_list = ["국제여객터미널", "제주연안여객터미널", "제4부두", "제6부두", "임항로", "제주해양경찰서"]