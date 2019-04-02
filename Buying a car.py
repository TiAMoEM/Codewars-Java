def nbMonths(startPriceOld, startPriceNew, savingperMonth, percentLossByMonth):
    """
    codewars练习题: Buying a car
    :param startPriceOld:       旧车价钱
    :param startPriceNew:       新车价钱
    :param savingperMonth:      每月存的钱
    :param percentLossByMonth:  每月降价的数值
    :return:
    """
    if startPriceOld >= startPriceNew:
        return [0, startPriceOld - startPriceNew]
    gapMoney = startPriceNew - startPriceOld
    New = startPriceNew
    Old = startPriceOld
    month = 1
    while savingperMonth * (month - 1) < gapMoney:
        if month % 2 == 0:
            percentLossByMonth += 0.5
        New = New * ((1 - percentLossByMonth / 100))
        Old = Old * ((1 - percentLossByMonth / 100))
        gapMoney = New - Old
        month += 1

    remain = round(savingperMonth * (month - 1) - gapMoney)
    return [month - 1, remain]