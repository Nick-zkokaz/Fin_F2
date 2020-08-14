# ДЗ E9_11


Для запуска проекта  необходимо:
1) Распаковать проект в папку DZ_E9_11 и через терминал зайти в директорию проекта
2) Создать виртуальное окружение:
   - python -m venv flask
3) Активировать виртуальное окружение:
   - flask\Scripts\activate.bat
4) Установить все необходимые пакеты:
   - pip install -r requirements.txt
5) Запустите локальный сервер:
   - python manage.py runserver

 --Сервер открывается по адресу  http://127.0.0.1:5000/ или http://0.0.0.0:5000/

6) Также можно воспользоваться следующими командами:
   - python manage.py db migrate --> создать миграции
   - python manage.py db upgrade --> применить миграции
   - python manage.py createsuperuser --> создать суперпользователя (администратора)

Для деплоя на heroku необходимо:
1) В терминале зайти в директорию проекта:
2) Выполнить следующие команды:
   - git init
   - git add .
   - git commit -m "initial commit"
   - heroku login
   - heroku create
   - heroku rename -a https://enigmatic-headland-63521.herokuapp.com/ https://shielded-plains-77689.herokuapp.com/ (переименовываем приложение, если необходимо)
   - heroku addons:create heroku-postgresql --as DATABASE
   - heroku config:set SECRET_KEY=Ваш_секретный_код
   - git push heroku master
   - heroku run python manage.py db migrate
   - heroku run python manage.py db upgrade
   - heroku run python manage.py createsuperuser

3) Запуск приложение:
   - heroku open

-- Данный проект находится на https://fatidique-livre-88037.herokuapp.com/
 --- Логин admin, пароль admin 

