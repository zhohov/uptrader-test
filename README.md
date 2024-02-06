# Тестовое задание для UpTrader

**Проект реализован с использованием фреймворка Django, базы данных SQLite, а так же инструмента управления зависимостями Poetry. 
Кроме того, в проект включен Docker для контейнеризации приложения, а так же Nginx в качестве обратного прокси для локальной разработки**

## Инструкция по установке

1. **Установка Docker:**
   - [Docker](https://docs.docker.com/get-docker/)
2. **Клонирование репозитория**
	```bash
	git clone https://github.com/zhohov/uptrader-test.git
	```
3. **Настройка проекта**
   - Переименовать `env` в `.env`
   - Заполнить данные в `.env`
     ```
     SECRET_KEY = ...
     ```
5. **Запуск проекта** 
    ```bash
    docker-compose up --build
    ```
6. Проект доступен по адресу `http://localhost`

## Примечания

- **Django Admin**
    - Чтобы войти в админ-панель Django требуется создать суперпользователя
        ```bash
        docker-compose exec web python src/manage.py createsuperuser
        ```
        После этого можно перейти на `http://localhost/admin/` и войти в аккаунт с учетными данными созданного суперпользователя