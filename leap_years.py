def isLeap(year):
    out = False
    if (year%4 == 0):
        out = True
        if (year%100 == 0):
            out = False
            if (year%400 == 0):
                out = True
    return out

count = 0
years = 2019
while (1):
    if isLeap(years) == True:
        print(years)
        count += 1
    years += 1
    if count == 20:
        break