store={'Весь склад':{}}
korzina=[]
while True:
    menu=input('Выберите действие: \n'
      '1-Добавить \n '
      '2-Изменить \n '
      '3-Удалить ')
    if menu=='1':
       new_product=input('Добавить товар: ')
       korzina.append(new_product)
       print(korzina)
    elif menu=='2':
       change=input('Введите новый товар: ')
       change2=input('Введите товар котрый хотите изменить ')
       index=korzina.index(change2)
       korzina[index]=change
       print(korzina)
    elif menu=='3':
       deleting=input('Удалить товар: ')
       korzina.remove(deleting)
       print(korzina)
    else:
       print('Неверное значение')

    menu=input('Что хотите делать? \n'
             '1-Добавить товар \n'
             '2-Удалить товар \n'
             '3-Посмотреть весь товар ')
    if menu=='1':
             product_name=input('Напишите название товара: ')
             product_count=input('Введите количество товара: ')
             store['Весь склад'][product_name]= product_count
    elif menu=='2':
      print(store)
      for k,v in store['Весь склад'].items():
             print(k,v)


