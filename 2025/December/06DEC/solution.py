def format_date(date_string):
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    x = date_string.split(' ')
    year = x[2]
    month = (months.index(x[0]))+1
    if len(str(month)) == 1:month = f"0{month}"
    day = x[1][:-1]
    if len(day) == 1:day = f"0{day}"
    answer = f'{year}-{month}-{day}'
    print(answer)
    return answer
