# API для Yatube

REST API для социальной платформы Yatube.  
Проект позволяет работать с публикациями, группами, комментариями и подписками через HTTP-запросы.

## Что умеет API

- получать список и отдельные объекты `posts`, `groups`, `comments`, `follow`;
- создавать, редактировать и удалять посты и комментарии;
- подписываться на авторов и искать подписки по `username`;
- выдавать JWT-токены для аутентификации.

Доступы:

- неаутентифицированные пользователи: только чтение;
- аутентифицированные пользователи: создание контента;
- изменять и удалять можно только свой контент;
- эндпоинт подписок `/api/v1/follow/` доступен только авторизованным.

## Технологии

- Python 3.10+
- Django 3.2
- Django REST Framework
- Djoser + SimpleJWT
- SQLite (по умолчанию)

## Как запустить проект локально

1. Клонировать репозиторий и перейти в него:

```bash
git clone <url_репозитория>
cd api-final-yatube-ad
```

2. Создать и активировать виртуальное окружение:

Для Windows (PowerShell):

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

Для Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Установить зависимости:

```bash
pip install -r requirements.txt
```

4. Применить миграции:

```bash
cd yatube_api
python manage.py migrate
```

5. Запустить сервер:

```bash
python manage.py runserver
```

## Документация API

После запуска проекта документация Redoc доступна по адресу:

`http://127.0.0.1:8000/redoc/`

## Основные эндпоинты

- `GET /api/v1/posts/` - список постов
- `POST /api/v1/posts/` - создать пост
- `GET /api/v1/groups/` - список групп
- `GET /api/v1/posts/{post_id}/comments/` - комментарии поста
- `GET /api/v1/follow/` - список подписок текущего пользователя
- `POST /api/v1/follow/` - подписаться на автора
- `POST /api/v1/jwt/create/` - получить JWT-токен

## Примеры запросов

### Получить JWT-токен

```bash
curl -X POST http://127.0.0.1:8000/api/v1/jwt/create/ \
  -H "Content-Type: application/json" \
  -d "{\"username\":\"admin\",\"password\":\"admin\"}"
```

### Создать пост

```bash
curl -X POST http://127.0.0.1:8000/api/v1/posts/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <access_token>" \
  -d "{\"text\":\"Мой первый пост через API\"}"
```

### Подписаться на автора

```bash
curl -X POST http://127.0.0.1:8000/api/v1/follow/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <access_token>" \
  -d "{\"following\":\"some_author\"}"
```
