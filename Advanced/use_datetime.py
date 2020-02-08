from datetime import datetime, timedelta, timezone

# Now
now = datetime.now()
print(now)

# create datetime object
dt1 = datetime(2019,1,1)
dt2 = datetime.strptime('2019-01-01 00:00:00','%Y-%m-%d %H:%M:%S')
print(dt1)
print(dt2)

# format datetime
nowf = now.strftime('%Y/%m/%d')
print(nowf)

# datetime ops, timedelta
td = timedelta(days=1, hours=12)
dt3 = dt2 + td
print(dt3)

df = now - dt3
print(df)
print(type(df))  # <class 'datetime.timedelta'>
no_of_days = df.days
print(no_of_days)

