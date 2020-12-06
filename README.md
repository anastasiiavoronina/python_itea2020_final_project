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