def date_nb_days(a0, a, p):
    day = math.ceil(math.log(a / a0, (1 + p / 36000)))
    return str(datetime.date(2016, 1, 1) + datetime.timedelta(day))