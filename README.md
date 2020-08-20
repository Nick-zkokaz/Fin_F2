


#SF Final 
 final project

# Для развертывания пректа в Docker.

 - скопировать репозиторий
 - docker-compose build собрать контейнеры web_1 и db_1 
 - docker-compose up запустить контейнеры
 - Cntr+C  остановить контейнеры для 
 - docker-compose run web python manage.py makemigrations  cоздания миграции 
 - docker-compose run web python manage.py migrate         проведения миграции db_1
 - docker-compose run web python manage.py createsuperuser создания суперюзера

 - docker-compose run web python manage.py loaddata db.json загрузить имеющиеся фикстуры
	- Выгрузить свою базу данных docker-compose run web python manage.py dumpdata > db.json
 - docker-compose up запуск докеров с базой

 - Сайт работает по адресу 127.0.0.1:8000 
 - В базе данных предустановлены пользователи: admin, пароль admin (суперпользователь)
 - есть еще два пользователя с обычными привилегиями: user1 - user1,
							31  - 31,
							user2 - user2
	

 - user2 может пройти  все тесты, новый юзер тоже может пройти все тесты 

 - Управление через Джанго Админку
	- сначала создаются вопросы  с ответами
	- затем назначаются блоки
	- затем можно создать результаты или ответить на вопросы в web 
	- у юзеров admin,user1 и 31 все тесты пройдены - не будет возможности пройти тест ещё раз  
	- user2 может пройти все тесты , также все тесты может пройти вновь зарегистрированный пользователь
	- результаты тестирования сохраняются в Django админке.

Сообщение для Николая Афанасьева - я не дождался ответа в Slack и решил задачу обозначенную там, через
таблицу соответствий (положил эту таблицу в файл Соответствия.xlsx). Проблемма , как я её понимаю, у меня
следующая - я не смог создать\разобраться в рекрусивных связях в полях многие к одному.
А именно, например, 3 ответа на один из вопросов. Решил задачу через ID вопроса и ID ответов на этот вопрос.
Понимаю как решить этот вопрос через Python , но тут разрешено не прорабатывать до конца, я и не стал.
Oбработку нового теста , поэтому нужно дописывать в results.html


Для деплоя на heroku необходимо:
1) В терминале зайти в директорию проекта:
2) Выполнить следующие команды:
   - git init
   - git add .
   - git commit -m "initial commit"
   - heroku login
   - heroku create
   - heroku addons:create heroku-postgresql --as DATABASE
   - heroku config:set SECRET_KEY=Ваш_секретный_код
   - git push heroku master
   - heroku run python manage.py  migrate
   - heroku run python manage.py  upgrade
   - heroku run python manage.py createsuperuser

3) Запуск приложение:
   - heroku open

-- Данный проект находится на https://shielded-plains-77689.herokuapp.com/
 --- Логин admin, пароль admin 

"# Fin_F2" 
