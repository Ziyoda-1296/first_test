store={'Весь склад':{}}
while True:
    menu=input('Что хотите делать? \n'
             '1-Добавить товар \n'
             '2-Удалить товар \n'
             '3-Посмотреть весь товар ')
    if menu=='1':
             product_name=input('Напишите название товара: ')
             product_count=input('Введите количество товара: ')
             store['Весь склад'][product_name]= product_count
    elif menu=='2':
        product_delete=input('Напишите что бы хотели удалить: ')
        product_delete=('Напишите количество: ')
        for d,v in product_name.remove(),product_count.remove():
            print(d,v)
    elif menu=='3':
      print(store)
      for k,v in store['Весь склад'].items():
          print(k,v)


