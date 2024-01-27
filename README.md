# Диплом

[![Automated tests](https://github.com/ElGansoDorado/Diplom/actions/workflows/build.yml/badge.svg)](https://github.com/ElGansoDorado/Diplom/actions/workflows/build.yml)
[![Automated tests](https://github.com/ElGansoDorado/Diplom/actions/workflows/pr-title-checker.yml/badge.svg)](https://github.com/ElGansoDorado/Diplom/actions/workflows/pr-title-checker.yml)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=ElGansoDorado_Diplom&metric=coverage)](https://sonarcloud.io/summary/new_code?id=ElGansoDorado_Diplom)
[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=ElGansoDorado_Diplom&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=ElGansoDorado_Diplom)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=ElGansoDorado_Diplom&metric=bugs)](https://sonarcloud.io/summary/new_code?id=ElGansoDorado_Diplom)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=ElGansoDorado_Diplom&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=ElGansoDorado_Diplom)

## Оглавление(ссылки)

- [Заметки](#заметки-по-проекту)
- [Команды проекта](#команды-проекта)
- [Ведение гита проекта](#гайд-по-ведению-гита-проекта)
    - [Как называть ветки](#гайд-по-названиям-веток)
    - [Как называть коммиты](#гайд-по-названиям-коммитов)
    - [Как называть PR](#гайд-по-названиям-pr)
- [Структура проекта](#гайд-по-структуре-проекта)
- [Окружение](#окружение)
- [Запуск](#запуск)
- [Работа с файлами](#работа-с-файлами)
- [Шаблонизатор](#шаблонитизатор)
- [Гайд по тестам](#тесты)
- [Docker](#docker)

---

## Данные для входа

| Приложение   | Локально    | Сайт          |                 |
|--------------|-------------|---------------|-----------------|
| логин        | karlik      | karlik_01     |                 |
| пароль       | terpenie    | terpenie_01   |                 |
| вход         | читать гайд | mrs.hopto.org | (если работает) |
|              |             | 94.139.242.71 |                 |
| админ-панель | admin       | terpenie      |                 |

---

## Заметки по проекту:

Вот таким образом можно делать заметки в коде(работает в pycharm точно)

/# TODO: task
(использовать без /)

После принятия и слияния PR, в которых вносились изменения в models, требуется принять
миграции.

```cmd
python manage.py migrate
```

Иначе могут быть проблемы.

## Команды проекта

#### Заполнение тестовых записей в базу данных

Добавлен функционал для заполнения базы тестовыми записями. Работает на _faker, чтобы вызвать и добавить нужно
использовать команду:

```cmd
python manage.py populate_data <кол-во>
```

Через аргумент передаём кол-во записей для создания. Минимум 1, максимум 100

пример

```cmd
python manage.py populate_data 40
```

_Будет создано 40 новых записей_

#### Пересброс token_id

Команда на случай если будет проблема с id token(проблемы мало вероятны, однако полезно при тесте)

_Переделает для всех записей в бд:_

```cmd
python manage.py regenerate_tokens --all
```

_Переделает для отправленных id(можно списком):_

```cmd
python manage.py regenerate_tokens <id>
```

---

## Гайд по ведению гита проекта

В main находится стабильная версия, которая будет работать на сервере. <br>
Чтобы что-то сделать, нужно создать ветку от main'a и назвать дать ей соответствующее название.<br>
Дальше работаем в ветке и делаем нормальные коммиты(гайд есть ниже).<br>
Далее, чтобы применить изменения, нужно сделать пулл-реквест в main.<br>
Далее требуется подтверждение от коллег и пройти тесты SonarCloud.<br>

### Гайд по названиям веток:

Создание новой ветки:

При создании новой ветки для работы с новой функциональностью, исправлением бага или задачей,
используйте префиксы, указанные в конфигурации.

feature/ для новых функциональностей <br>
bugfix/ для исправлений ошибок <br>
chore/ для задач, не связанных напрямую с функциональностью или исправлением бага, например, обновление зависимостей<br>

Например:

git checkout -b feature/new-feature<br>
git checkout -b bugfix/fix-bug<br>
git checkout -b chore/update-dependencies<br>

---

**Работа с веткой:**

Ваша работа внутри ветки должна быть логически связанной с тем, что указано в префиксе.
Например, если вы работаете в ветке feature/, то ваши изменения должны относиться к новой функциональности.

**Синхронизация с удаленным репозиторием:**

Перед пушем ваших изменений в удаленный репозиторий, убедитесь, что ветка именуется согласно соглашениям и префиксами.

**Пулл-реквест:**

При создании пулл-реквеста убедитесь, что ваша ветка называется согласно соглашениям.
Если есть проблемы с названием ветки, система выдаст соответствующее сообщение об ошибке.

---

### Гайд по названиям коммитов:

Обычно, при использовании Git и коммитов, каждый коммит стараются делать атомарным,
то есть в одном коммите фиксируются изменения, связанные с определенной логической единицей работы.
Это делает историю коммитов более читаемой и упрощает внесение изменений в будущем.

**Префиксы для коммитов:**

fix: Исправление ошибки в модуле X<br>
feat: Добавление функциональности Y<br>
docs: Обновление инструкций по установке<br>
refactor: Переименование переменных для улучшения читаемости<br>
style: Коррекция отступов и стиля кода<br>
test: Добавление модульных тестов для класса Z<br>
update: Обновление функционала<br>
docs: Добавление информации в документацию версии 1<br>

**Каждый коммит должен начинаться с одного из префиксов**, указанных в конфигурации. Например:

git commit -m "feat: добавлена новая функциональность"<br>
git commit -m "fix: исправлена ошибка в обработке данных"<br>
git commit -m "chore: обновление зависимостей"<br>

Логическая связь:

Внутри одного коммита должны быть внесены изменения, логически связанные с тем, что указано в префиксе.

**Обновление коммитов:**

Если вы заметили, что название коммита не соответствует соглашениям, вы можете внести исправления
и использовать git commit --amend для изменения последнего коммита.

---

### Гайд по названиям PR:

Правила и примеры использования префиксов в названиях Pull Request (PR)

fix: Используется для PR, в котором вносятся исправления ошибок.<br>
feat: добавление новой функциональности<br>
docs: обновление документации<br>
refactor: Используется для PR, связанного с переработкой кода без добавления новой функциональности или исправлений.<br>
style: форматирование кода в соответствии с Prettier<br>
test: Используется для PR, связанного с добавлением или обновлением тестов.<br>
update: обновление зависимостей или других внешних компонентов.<br>

---

## Гайд по структуре проекта

Проект состоит из двух приложений:

**web_hanlder**

Login<br>
Home<br>
Прочие информационные страницы, не связанные с обработкой

**clients**

clients_list<br>
clients_details

Тут все записи. Нейронка будет либо тут, либо еще одно приложение. Посмотрим.

## Окружение

---

Проект переведен на python3 12 версии. Подойдет версия начиная с 3.12.1

Узнать версию python:

```cmd
python --version
```

Скачать:
https://www.python.org/ftp/python/3.12.1/python-3.12.1-amd64.exe

Также нужно обновить и пакетный менеджер (PIP):

```cmd
python -m pip install --upgrade pip
```

Чтобы работать, нужно создать виртуальное окружение - это изолированное окружение среды
(в нашем случае это окружение Python), которое позволяет нам использовать определенные версии приложений.

в консоли -> Заходим в нужную папку -> пишем:

```cmd
python -m venv venv  
```

**ВАЖНО**<br>Нужно обязательно проверять включен venv или нет!

В консоли должна появиться приписка спереди, с названием окружения, если всё работает.

Установить все зависимости для проекта:

```cmd
pip install -r requirements.txt
```

Чтобы запустить:

переходим в venv\\Scripts
запускаем activate
на windows: ./activate
Всё работает, что бы выйди -> Deactivate

_Если что-то нужно еще, то устанавливаем и предупреждаем!
Гайд по зависимостям будет чуть позже.

---

## Запуск

Нужно быть в файле проекта. То есть не просто в папке Diplom, а в mrs_proj, где находится файл manage.py

```cmd
python manage.py runserver
```

Если всё нормально, то запуститься на localhost:8000, также можно передать аргументом нужный порт.

Закрыть проект:

```cmd
CTRL+C  в консоль
```

Работая локально, вы работаете через базу Sqlite, которая тягается с проектом.

---

## Работа с файлами

Есть соглашение, чтобы все статические(css, js, картинки и прочее)
лежали в папке *static* нужного приложения(допускаются вложения отдельных папок)

**стиль описания файлов:**

*приложение*_*страница_приложения*_тип

Пример:

clients_list_styles.css

Если есть два слова, типа web_handler. То можно использовать сокращение или одно слово. Главное чтобы
везде было одинаково.

---

## Шаблонизатор

**Шаблонизатор** — программное обеспечение, позволяющее использовать html-шаблоны для генерации конечных html-страниц.
Основная цель использования шаблонизатора — это отделение представления данных от исполняемого кода.

Подключения статических файлов:

```html
{% load static %}
```

```html
{% static "путь к файлу внутри папки static" %}
<link rel="stylesheet" href="{% static " css/styles.css" %}" />
```

Нередко шаблоны должны иметь одинаковую базовую структуру, одни и те же блоки, при этом определять для отдельных блоков
различное содержимое. Это позволяет сформировать единообразный стиль сайта, когда веб-страницы имеют одни и те же
структурные элементы - меню, хедер, футер, сайдбары и так далее.

В этом случае мы можем определять все шаблоны по отдельности. Однако если возникнет необходимость изменить какой-то
блок, например, добавить в общее меню еще один пункт, тогда придется менять все шаблоны, коих может быть довольно много.
И в этом случае оптимальнее повторно использовать один базовый шаблон, который определяет все основные блоки.

Например, определим шаблон, который назовем base.html:

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8"/>
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

С помощью элементов {% block название_блока %}{% endblock название_блока %} определяются отдельные блоки шаблонов. При
этом для каждого блока определяется открывающий элемент {% block название_блока %} и закрывающий элемент {% endblock
название_блока %}.

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

---

## Тесты

В приложении работают авто-тесты. Нужно обязательно смотреть за покрытием нового кода тестами.
Тесты дописываются в соответствующие файлы проекта. tests.py
Документация по тестам есть в документации Django.

Сейчас есть два варианта запустить тесты

(директория /mrs_proj)

```cmd
python manage.py test
```

Запуск тестов с покрытием

```cmd
tox
```

Будет выведена информация по покрытию (по файлам). tox создаст новое
виртуальное окружение в своей папке. Зависимости он подтянет сам.

При PR SonarCloud будет запускать тесты у себя. Так что если что-то будет не так, то
ошибки смотрим на Github.

---

## Docker

Сделал настройки для сбора приложения в докер-контейнер. Там сразу все настройки.
Nginx и Gunicorn. Версия приложения собирается последняя стабильная. Естественно нужен установленный docker в системе.

```cmd
docker build -t mrs_proj:latest .  #собрать контейнер
docker save -o mrs_proj_image.tar mrs_proj:latest # экспорт Docker-образа и перенос на другую машину
```

Перенесите файл mrs_proj_image.tar на другую машину.

```cmd
docker load -i mrs_proj_image.tar # импортируйте Docker-образ на другой машине
```
Запустить контейнер

```cmd
docker run -p 8000:8000 mrs_proj:latest gunicorn mrs_proj.wsgi:application
```
Замените 8000:8000 на необходимые вам порты, и убедитесь, что ваши Django-настройки (например, ALLOWED_HOSTS)<br>
и настройки Gunicorn соответствуют вашему окружению.<br>
Теперь ваш Django проект должен быть доступен на порту 8000 внутри контейнера.


---

![nonlin](img/im.jpg)