cash = int(input('Сколько составляет прибыль Вашего ларька?  '))
costs = int(input('Сколько составляет расход на Ваш ларек? '))
kpd = cash - costs
if kpd > 0 :
    print('Ваш чистый доход состовляет ' + str(kpd),"р .Вы на верном пути!" )
elif kpd == 0 :
    print('Вы работаете в 0. Вам следует рассмотреть цены на услуги или сэкономить на расходах')
else:
    print('Вы работаете в минус. Долг составляет ' + str(kpd),"р. Вам следует рассмотреть цены на услуги или сэкономить на расходах")

