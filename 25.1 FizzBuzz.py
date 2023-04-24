r_day, r_month, r_year = [int (i) for i in input().strip().split(' ')]
d_day, d_month, d_year = [int (i) for i in input().strip().split(' ')]

if r_year < d_year:
    print(0)
elif r_year == d_year:
    if r_month < d_month:
        print(0)
    elif r_month == d_month:
        if r_day <= d_day:
            print(0)
        else:
            print(15 * (r_day - d_day))
    else:
        print(500 * (r_day - d_day))
else:
    print(10000)
