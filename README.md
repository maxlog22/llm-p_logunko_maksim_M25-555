# Построение защищённого API для работы с большой языковой моделью

## Цель работы
Разработка серверного приложения на FastAPI, предоставляющего защищённый API для взаимодействия с большой языковой моделью (LLM) через сервис OpenRouter. В рамках задания необходимо было реализовать аутентификацию и авторизацию пользователей с использованием JWT, хранение данных в базе SQLite, а также корректно разделить ответственность между слоями приложения (API, бизнес-логика, доступ к данным).
В рамках проекта были получены следующие практические навыки:
- работы с FastAPI и асинхронным backend,
- проектирования серверной архитектуры с разделением слоёв,
- использования JWT для аутентификации,
- интеграции внешних API (LLM),
- работы с базой данных через SQLAlchemy,
- управления зависимостями проекта через uv.

## Запуск проекта
uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

После запуска приложения по сслыке станет доступен интерфейс Swagger, в котором доступна документация всех реализованных эндпоинтов и возможность их тестирования.
Ссылка после запуска проекта: http://0.0.0.0:8000/docs

## Работа со Swagger
### 1. Регистрация
<img width="1911" height="852" alt="Регистрация" src="https://github.com/user-attachments/assets/0be848e4-bbe5-4d9d-8fd1-6ba0ee5e8170" />

### 2. Получение JWT-токена
<img width="981" height="958" alt="Логин и получение JWT" src="https://github.com/user-attachments/assets/d2a375c1-a723-4726-8db0-4794664e6882" />

### 3. Авторизация в Swagger
<img width="663" height="604" alt="Авторизация1" src="https://github.com/user-attachments/assets/9bdf2a59-6123-4662-bb09-4a5da7e13b72" />
<img width="661" height="458" alt="Авторизация2" src="https://github.com/user-attachments/assets/c1c3f969-763f-404c-a4f5-be3436e0e878" />
Стали доступны эндпоинты по JWT:
<img width="1428" height="817" alt="Эндопоинты по JWT" src="https://github.com/user-attachments/assets/d9ddd4f4-5e86-41bb-ae29-d510704f80dc" />

### 4. Вызов POST /chat
<img width="963" height="907" alt="1 запрос" src="https://github.com/user-attachments/assets/aeb830a3-e309-4d8d-ba57-64856fc13510" />

### 5. Получение истории GET
<img width="963" height="907" alt="Получение истории" src="https://github.com/user-attachments/assets/3aa2ef1e-649b-4899-ac4f-f011188cc44e" />

### 6. Удаление истории через DELETE
Удаление истории:
<img width="964" height="576" alt="Удаление истории" src="https://github.com/user-attachments/assets/94522ce5-5447-47b7-a873-9c68d2badcbb" />
Проверка удаления:
<img width="964" height="607" alt="Проверка_удаления" src="https://github.com/user-attachments/assets/9b1a7f55-7abb-4259-867c-8cbdd946acc3" />









