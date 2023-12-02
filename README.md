# Diplom

Репозиторий для работы над дипломом

==терпим==

|          |               |               |
|----------|---------------|---------------|
| Сайт:    | 94.139.242.71 | mrs.hopto.org |
| Онлайн   | karlik_01     | terpenie_01   |
| Локально | karlik        | terpenie      |


## Гайд по структуре

Проект состоит из двух приложений:

**web-hanlder**

Login<br>
Home<br>
Прочие информационные страницы, не связанные с обработкой

**clients**

clients_list<br>
clients_details

Тут всё о карликах. Нейронка либо тут, либо еще одно приложение. Посмотрим.

## Окружение

Для проекта нужна версия питона 3.11.(~)
Лучше всего 3.11.6.
(не 12 версия)

Узнать версию питона:

```cmd
python --version
```
Питончик скачать.
https://www.python.org/ftp/python/3.11.6/python-3.11.6-embed-amd64.zip

Также нужно обновить и пакетный менеджер (PIP):
```cmd
python -m pip install --upgrade pip
```

Чтобы работать, нужно создать виртуальное окружение - это изолированное окружение среды (в нашем случае это окружение Python), которое позволяет нам использовать определенные версии приложений.

в консоли  -> Заходим в нужную папку  -> пишем :
```cmd
python -m venv venv  
```

В консоли должна появиться приписка спереди, с названием окружения, если всё работает.

Установить все зависимости для проекта:
```cmd
pip install -r requirements.txt
```

Чтобы запустить:

переходим в venv\\Scripts
запускаем activate 
на шинде: ./activate
Всё работает, что бы выйди -> Deactivate

Устанавливаем что надо, если надо

## Запуск

Нужно быть в файле проекта. То есть не просто папка Diplom с гита, а mrs_proj, где лежит manage.py


```cmd
python manage.py runserver
```

Если всё нормально, то запуститься на localhost:8000 можно передать аргументом нужный порт
, если не устраивает.

Закрыть проект:
```cmd
CTRL+C  в консоль
```

Работая локально, вы работаете через базу Sqlite, которая тягается с проектом. Там есть логин+пароль
karlik    terpenie

## Работа с файлами

Есть соглашение, чтобы все статические(css, js, картинки и прочее)

лежали в папке *static* нужного приложения(допускаются вложения отедельных папок)

стиль описания файлов:

*приложение*_*страница_приложения*_тип

Пример:

clients_list_styles.css

Если есть два слова, типа web_handler. То можно использовать сокращение или одно слово. Главное чтобы
везде было одинаково.


## Шаблонитизатор

Подключения статических файлов
```html
{% load static %}
```


```html
{% static "путь к файлу внутри папки static" %}
<link rel="stylesheet" href="{% static "css/styles.css" %}" />
```

Нередко шаблоны должны иметь одинаковую базовую структуру, одни и те же блоки, при этом определять для отдельных блоков различное содержимое. Это позволяет сформировать единообразный стиль сайта, когда веб-страницы имеют одни и те же структурные элементы - меню, хедер, футер, сайдбары и так далее.

В этом случае мы можем определять все шаблоны по отдельности. Однако если возникнет необходимость изменить какой-то блок, например, добавить в общее меню еще один пункт, тогда придется менять все шаблоны, коих может быть довольно много. И в этом случае оптимальнее повторно использовать один базовый шаблон, который определяет все основные блоки.

Например, определим шаблон, который назовем base.html:

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <title>{% block title %}Default title{% endblock title %}</title>
</head>
<body>
    <div><a href="/">Главная</a> | <a href="/contacts">Контакты</a></div>
    <h1>{% block header %}{% endblock header %}</h1>
    <div>{% block content%}{% endblock content %}</div>
    <div>MyCorp. 2022. All rights reserved.</div>
</body>
</html>
```

С помощью элементов {% block название_блока %}{% endblock название_блока %} определяются отдельные блоки шаблонов. При этом для каждого блока определяется открывающий элемент {% block название_блока %} и закрывающий элемент {% endblock название_блока %}.


Теперь применим этот базовый шаблон. Например, создадим новый шаблон index.html:

```html
{% extends "base.html" %}
{% block title %}Index{% endblock title %}
{% block header %}Главная{% endblock header %}
```
Также создадим шаблон contacts.html:

```html
{% extends "base.html" %}
{% block title %}Контакты{% endblock title %}
{% block header %}Контакты{% endblock header %}
  
{% block content %}
<p>Телефон: +12345677890</p>
<p>Email: admin@admin.com</p>
{% endblock content %}
```

![nonlin](img/im.jpg)