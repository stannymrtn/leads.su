# Автоматизации тестирования LEADS.SU
<a target="_blank" href="https://leads.su/">Сайт проекта</a>

## Содержание
- [Стек](#стек)
- [Примеры UI тестов](#примеры-ui-тестов)
- [Примеры API тестов](#примеры-api-тестов)
- [Сборка](#сборка)
- [Allure отчет](#allure-отчет)
- [Отчет в Telegram](#отчет-в-telegram)
- [Видео прохождения тестов](#видео-прохождения-тестов)

## Стек
<p>
<a href="https://www.jetbrains.com/pycharm/"><img src="resources/images/PyCharm_Icon.svg" width="50" height="50"  alt="Pycharm" title="IntelliJ IDEA"/></a>
<a href="https://www.python.org/"><img src="resources/images/python.svg" width="50" height="50"  alt="Python" title="Python"/></a>
<a href="https://github.com/"><img src="resources/images/Github.svg" width="50" height="50"  alt="Github" title="GitHub"/></a>
<a href="https://www.selenium.dev/"><img src="resources/images/selenium.svg" width="50" height="50"  alt="Selenium" title="Selenium"/></a>
<a href="https://aerokube.com/selenoid/"><img src="resources/images/Selenoid.svg" width="50" height="50"  alt="Selenoid" title="Selenoid"/></a>
<a href="https://github.com/allure-framework/allure2"><img src="resources/images/Allure_Report.svg" width="50" height="50"  alt="Allure" title="Allure"/></a>
<a href="https://www.jenkins.io/"><img src="resources/images/Jenkins.svg" width="50" height="50"  alt="Jenkins" title="Jenkins"/></a>
<a href="https://github.com/yashaka/selene"><img src="resources/images/selene.png" width="50" height="50"  alt="Selene" title="Selene"/></a>
</p>

В проекте автотесты написаны на <code>Python</code> с использованием <code>Selenium</code>, <code>Selene</code> и <code>Pytest</code> для UI-тестов
>
> <code>Selenoid</code> Запускает браузеры в контейнерах <code>Docker</code>.
>
> <code>Allure Report</code> Формирует отчеты о запуске тестов.
>
> <code>Jenkins</code> Выполняет запуск самих тестов.
> После завершения прогона отправляются уведомления в <code>Telegram</code>.


## Примеры UI тестов
- Проверка входа в систему
- Проверка Создания отчёта в Checker
- Проверка добавления оффера в избранное
- Проверка генерации API-токена
- Проверка закреплённого оффера в каталоге


## Примеры API тестов
- API тесты были написаны на трекер trello.com:

- Проверка создания рабочей доски
- Проверка изменения рабочей доски
- Получение информации о рабочей доске
- Удаление рабочей доски

##  Сборка
>
> В сборке присутствуют настраиваемые параметры.
>
> Один из них - версия браузера. Сами тесты запускаются удаленно с помощью <code>Selenoid</code>
<p align="center">
<img title="Сборка в Jenkins с параметрами" src="resources/images/jenkins_parameters.png">
</p>
Ссылка на джобу в jenkins
https://jenkins.autotests.cloud/job/for%20leads.su,%20latypov/

## Allure отчет
>
> Allure формирует подробный отчет о прогоне тестов. Кастомные фильтры и листенеры делают отчет максимально понятным
>
> Например в отчет пишутся все селекторы и методы <code>Selene</code>, отчеты формируются по категориям, в конце приложен скриншот, видео запись прогона теста и логи.
Для API тестов полностью указаны данные запроса/ответа
<p align="center">
<img title="Allure отчет" src="resources/images/allure-report.png">
</p>
<p align="center">
<img title="Allure отчет" src="resources/images/allure-report_2.png">
</p>
<p align="center">
<img title="Allure отчет" src="resources/images/allure-report_3.png">
</p>

## Отчет в Telegram
>
> Далее в <code>Telegram</code>чат автоматически приходит уведомление с информацией о прогоне и ссылкой на <code>Allure</code>
>
<p>
<img title="Отчет в Telegram с помощью бота" src="resources/images/allure_tg.png">
</p>

## Видео прохождения тестов
>
> <code>Selenoid</code> пишет видео прогона каждого теста и видео прикладывается в отчет <code>Allure</code>
>
<p>
<img title="Selenoid Video" src="resources/images/auth.gif" alt="video">
</p>
