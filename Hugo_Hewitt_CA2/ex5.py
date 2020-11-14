"""A module that interperets access logs"""
access_log = ["19.69.248.2 mmc2 [12/12/2018] `GET /m/' 200 4263",
"19.69.248.2 mmc2 [12/12/2018] `GET /m/index.php' 200 4494",
"46.72.177.4 gr4 [12/12/2018] `GET /video/v.php' 200 4263"]

def monthly_users(year):
    '''A function to calculate the number of users each month'''
    lst = [0,0,0,0,0,0,0,0,0,0,0,0]
    ips = []
    j = 0
    date = []
    while j < len(access_log):
        log = access_log[j]
        i = 0
        while i < len(log):
            if log[i] == '[':
                start = i
            elif log[i] == ']':
                end = i
            i += 1
        temp = ''
        i = 0
        while log[i] != ' ':
            temp += log[i]
            i+=1
        if temp not in ips:
            date.append(log[(start+1):end])
        j+=1
        ips.append(temp)
    month = []
    i = 0
    for i in date:
        if int(i[6:11]) == year:
            month.append(i[3:5])
    i = 0
    for i in month:
        lst[(int(i)-1)] += 1
    return lst

def annual_user_count(year):
    '''A function to calculate the number of users a year'''
    total = 0
    lst = monthly_users(year)
    for i in lst:
        total += i
    return total

def annual_user_download_average(year):
    '''A function to find out the average size of a download'''
    downloaded = []
    date = []
    j = 0
    while j < len(access_log):
        log = access_log[j]
        i = 0
        while i < len(log):
            if log[i] == '[':
                start = i
            elif log[i] == ']':
                end = i
            i += 1
        date.append(log[(start+1):end])
        j+=1
    j = 0
    for log in access_log:
        temp = ''
        i = len(log) - 1
        while log[i] != ' ':
            temp += log[i]
            i-=1
        temp = ''.join(reversed(temp))
        if int(date[j][6:11]) == year:
            downloaded.append(temp)
        j += 1
    total = 0
    for i in downloaded:
        total += int(i)
    total = int(total/(len(downloaded)))
    return total

print(monthly_users(2018))
print(annual_user_count(2018))
print(annual_user_download_average(2018))
