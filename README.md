"# python_itea2020_final_project" 

**Technological stack**
1) Python3
2) MondoDB
3) Mongoengine
4) Flask
5) Flask restrul
6) Telebot
7) Google cloud
8) Nginx
9) Gunicorn
10) Marshmallow

**DB entities**
1) Product
   1. Name
   2. Description
   3. {Category}
   4. Price
   5. Availability (true/false)
   6. Picture
   7. Discount in %
2) Category
   1. Name
   2. Description
   3. {Parent category}
   4. [{Sub-categories}]
3) User:
   1. Telegram id (pk)
   2. Phone number
   3. Nickname
4) Shopping cart
5) Order
6) News
   1. Title
   2. Body
   3. Publish date
   
   
#Lesson12
1) создать абстрактную коллекцию. Она должна содержать 2 поля created и modified и хранить в них время 
создания/последнего обновления. Логику со временем размещаем в методе save.
2) Проинициализировать бот. Описать хендлер старт. При старте приветствовать пользователя. Создать модуль texts, 
в котором будут храниться константами тексты приветствий, импортировать его и поприветствовать константой.

#lesson13
1) описать хендлер, который будет отрабатывать при клике на кнопку новости. Выводить последние 5 новостей отдельными
сообщениями.
2) Коллекция новостей должна наследовать абстрактную коллекцию с датами (created_at, modified_at).
3) Описать хендлер для клика на кнопку определенной категории. Выводить названия всех продуктов, относящихся к 
категории, на которую кликнули, отдельными сообщениями. 

#lesson14
1) Описать метод форматирования описания продукта (цена, название, описание, характеристики) (если путсто, то не выводить None).
Отправлять эту информацию под картинкой продукта
2) Описать хендлер для обработки кликов на категории.
--Сделано - проверить, работают ли клики на суб-катергории - выводят ли соответствующие продукты
3) Описать коллекцию корзины и заказа

#lesson15
1) Реализовать логику для изменения данных профиля (добавить в модель поле адрес, сделать возможность изменения 
имени, номера телефона, имеила, адреса).
по нажатию на сеттинги - инфа, дальше кнопки - изенить адрес, изменить телефон, изменить имеил, изменить имя.
можно сделать обычными кнопками или инлайн кнопками.

#lesson16
0) Описать метод форматирования описания продукта (цена, название, описание, характеристики) (если путсто, то не выводить None).
Отправлять эту информацию под картинкой продукта 
-> цена с учетом скидки. проперти сделали на занятии

1) создать эккаунт в гугл клауде, создать виртуальную машину (1 вцп, 1.7 гб оперативной памяти, диск 40 гб)
2) Рассылка сообщений (сделали на занятии)
3) Вывод содержимого корзины при клике на кнопку Корзина пользователю должно выводиться все содержимое с возможностью увеличить либо уменьшить количество
кнопки плюс/минус?
сделать возможность добавлять несколько штук одного продукта, на усмотрение, как. можно из корзины
4) Оформление заказа. В момент формирования корзины добавить кнопку Завершить заказ.
После нажатия на кнопку завершить заказ, выводить пользователю все, что есть в корзине. Плюс запросить у него данные - почта, телефон, адрес
можно по-своему. можно завершать заказ из корзины
--реализовать добавление в корзину продуктов
5) после создания новости в бд отправлять ее содержимое всем пользователям бота

#NOT DONE:
3) Вывод содержимого корзины при клике на кнопку Корзина пользователю должно выводиться все содержимое с возможностью увеличить либо уменьшить количество
кнопки плюс/минус?
сделать возможность добавлять несколько штук одного продукта, на усмотрение, как. можно из корзины
4) Оформление заказа. В момент формирования корзины добавить кнопку Завершить заказ.
После нажатия на кнопку завершить заказ, выводить пользователю все, что есть в корзине. Плюс запросить у него данные - почта, телефон, адрес
можно по-своему. можно завершать заказ из корзины
--реализовать добавление в корзину продуктов

-??создание новостей через рест

#todo
- Скрипт для заполнения базы значениями. 
  Или при описании рест
  
  
