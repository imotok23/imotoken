#datetimeのインポート
import datetime

#うるう年や月の日数を考慮して、日付を進める関数
def add_days(date, days):
    # うるう年の判定
    if date.year % 4 == 0 and date.year % 100 != 0 or date.year % 400 == 0:
        leap_year = True
    else:
        leap_year = False

    # 月の日数
    if date.month in {1, 3, 5, 7, 8, 10, 12}:
        month_days = 31
    elif date.month == 2:
        if leap_year:
            month_days = 29
        else:
            month_days = 28
    else:
        month_days = 30

    # 日付の進め方
    # 複数の月をまたいでも進めるようにループ
    new_day = date.day + days
    if new_day <= month_days:
        new_date = date.replace(day=new_day)
    else:
        new_month = date.month + 1
        if new_month <= 12:
            new_date = date.replace(month=new_month, day=new_day - month_days)
        else:
            new_date = date.replace(year=date.year + 1, month=1, day=new_day - month_days)

    return new_date

#うるう年や月の日数を考慮して、二つの日付の間の日数を計算する関数
def days_diff(date1, date2):
    # 二つの日付の大小を入れ替える
    if date1 > date2:
        date1, date2 = date2, date1

    # うるう年の判定
    if date1.year % 4 == 0 and date1.year % 100 != 0 or date1.year % 400 == 0:
        leap_year = True
    else:
        leap_year = False

    # 月の日数
    if date1.month in {1, 3, 5, 7, 8, 10, 12}:
        month_days = 31
    elif date1.month == 2:
        if leap_year:
            month_days = 29
        else:
            month_days = 28
    else:
        month_days = 30

    # 二つの日付の差を計算
    days = 0
    while date1 < date2:
        days += 1
        date1 = add_days(date1, 1)

    return days


#上の関数add_daysをテストする関数
def test_add_days():
    # うるう年のテスト
    assert add_days(datetime.datetime(2020, 2, 28), 1) == datetime.datetime(2020, 2, 29)
    assert add_days(datetime.datetime(2020, 2, 28), 2) == datetime.datetime(2020, 3, 1)

    # 月末のテスト
    assert add_days(datetime.datetime(2020, 1, 31), 1) == datetime.datetime(2020, 2, 1)
    assert add_days(datetime.datetime(2020, 2, 29), 1) == datetime.datetime(2020, 3, 1)
    assert add_days(datetime.datetime(2020, 12, 31), 1) == datetime.datetime(2021, 1, 1)

    # 通常のテスト
    assert add_days(datetime.datetime(2020, 1, 1), 1) == datetime.datetime(2020, 1, 2)
    assert add_days(datetime.datetime(2020, 1, 1), 365) == datetime.datetime(2020, 12, 31)
    assert add_days(datetime.datetime(2020, 1, 1), 366) == datetime.datetime(2021, 1, 1)

    print("All tests passed.")
    
#上の関数days_diffをテストする関数
def test_days_diff():
    # うるう年のテスト
    assert days_diff(datetime.datetime(2020, 2, 28), datetime.datetime(2020, 2, 29)) == 1
    assert days_diff(datetime.datetime(2020, 2, 28), datetime.datetime(2020, 3, 1)) == 2

    # 月末のテスト
    assert days_diff(datetime.datetime(2020, 1, 31), datetime.datetime(2020, 2, 1)) == 1
    assert days_diff(datetime.datetime(2020, 2, 29), datetime.datetime(2020, 3, 1)) == 1
    assert days_diff(datetime.datetime(2020, 12, 31), datetime.datetime(2021, 1, 1)) == 1

    # 通常のテスト
    assert days_diff(datetime.datetime(2020, 1, 1), datetime.datetime(2020, 1, 2)) == 1
    assert days_diff(datetime.datetime(2020, 1, 1), datetime.datetime(2020, 12, 31)) == 365
    assert days_diff(datetime.datetime(2020, 1, 1), datetime.datetime(2021, 1, 1)) == 366

    print("All tests passed.")

test_add_days()
##test_days_diff()
