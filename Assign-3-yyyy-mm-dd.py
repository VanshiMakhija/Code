def dates(d1, q):
    dict_dates = {}
    present_year = d1[0:4]
    present_month = d1[4:]
    if present_month=='01':
        previous_month = '12'
        present_year = str(int(present_year)-1)
    else:
        previous_month = str(int(present_month)-1)
        if len(previous_month)==1:
            previous_month = '0' + previous_month
    dict_dates['prev_month'] = present_year + previous_month

    present_year = d1[0:4]
    qtr = q
    dict_dates['current_qtr'] = qtr + '_' + present_year

    if qtr=='Q1':
        qtr_1 = 'Q4'
        year = str(int(present_year)-1)
    else:
        qtr_1 = 'Q' + str(int(qtr[1])-1)
        year = present_year
    dict_dates['previous_qtr'] = qtr_1 + '_'+year

    present_year = d1[0:4]
    next_year = str(int(present_year) + 1)
    present_month = d1 [4:]
    next_month = str((int(present_month)+11)%12)
    if len(next_month)==1:
        next_month = '0' + next_month

    dict_dates['future_month'] = next_year + next_month
    print('Dates are as follows')

    return dict_dates


print(dates('202209', 'Q2'))

