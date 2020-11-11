import datetime as dt


now = dt.datetime.now()
print(now)
print('Date is:', now.year, '-', now.month, '-', now.day)
print('ShortForm date is:', now.strftime('%y'), now.strftime(
    '%b'), now.day, now.strftime('%a'),
    now.strftime('%H'), ':', now.strftime('%M'), ':', now.strftime('%S'))
print('FullForm date is:', now.strftime('%Y'), now.strftime(
    '%B'), now.day, now.strftime('%A'),
    now.strftime('%I'), ':', now.strftime('%M'), ':', now.strftime('%S'),
    now.strftime('%p'), now.strftime('%Z'), now.strftime('%z'),
    'Day of the year is:', now.strftime('%j'))


print('Local Date Time:\n', now.strftime('%c'),
      now.strftime('%X'), now.strftime('%x'))
