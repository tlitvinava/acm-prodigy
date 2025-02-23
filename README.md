# ACM Prodigy
---

## Содержание
0. [Описание](#описание-проекта)
1. [Установка](#установка)
2. [Настройка](#настройка)
3. [Запуск](#запуск)
4. [Лизцензия](#license)


## Описание проекта
Проект представляет собой веб-сайт, позволяющий проводить регистрацию и управление участниками олимпиад. Был разработан для проведения [BSUIR Open](https://acm.bsuir.by).


## Установка
TBD


## Настройка
После установки проекта, добавить в модель Settings следующие настройки:

```
    registration.team.available {true|false} -- Открытие регистрации
    mails.subject.quaterfinals {string} -- Тема письма для четвертьфинала
    mails.subject.semifinals {string} -- Тема письма для полуфинафинала
    mails.subject.finals {string} -- Тема письма для финала
    configuration.olymp.type {single|team} -- Для различных типов олимпиад
    configuration.registration.student_group {true|false} -- Валидация номера группы студента
    configuration.olympiad.credentials {false|true} -- Отображение логинов и паролей для пользователей
    configuration.team.prefix {string} -- Префикс логинов тестирующей системы
    configuration.team.scope {number} -- scope solve для которого будут создаваться пользователи
    configuration.solve.login {string} -- логин админки solve
    configuration.solve.password {string} -- пароль админки solve
    configuration.solve.url {string} -- ссылка на API Solve
```

## Запуск
TBD

## License

[ACM Prodigy](https://github.com/denvilk/acm-prodigy) © 2025 by [Velikovich Vladimir](https://github.com/denvilk) is licensed under [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International](LICENSE.txt)