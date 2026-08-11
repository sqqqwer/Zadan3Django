## Запуск проекта

- Клонируйте репозиторий
```shell
git clone https://github.com/sqqqwer/Zadan3Django.git
```
- Перейдите в проект
```shell
cd Zadan3Django/
```
- Подготовьте .env файл.
- Запустите docker

- Поднимите контейнеры
```shell
make docker-up
```
- Проект запущен

## Тест запросов через Postman
- Импортируйте файл [DogsAppTest.postman_collection](./book_store/scripts/test_query.py) в Postman

## Примеры запросов
### Добавление новой Породы
Запрос:
```
POST http://127.0.0.1:8000/api/breeds/
```
```json
{
    "name": "Овчарка",
    "size": "medium",
    "friendliness": 4,
    "trainability": 5,
    "shedding_amount": 2,
    "exercise_needs": 5
}
```
Ответ:

*Cоздаётся и возвращается новая Порода*
```json
{
    "id": 1,
    "name": "Овчарка",
    "size": "medium",
    "friendliness": 4,
    "trainability": 5,
    "shedding_amount": 2,
    "exercise_needs": 5
}
```
### Добавление новой Собаки
Запрос:
```
POST http://127.0.0.1:8000/api/dogs/
```
```json
{
    "name": "Шарик",
    "age": 5,
    "breed": 1,
    "gender": "М",
    "color": "Черно-коричневый",
    "favorite_food": "Кукуруза",
    "favorite_toy": "Кость"
}
```
Ответ:

*Cоздаётся и возвращается новая Собака*
```json
{
    "id": 1,
    "name": "Шарик",
    "age": 5,
    "breed": 1,
    "gender": "М",
    "color": "Черно-коричневый",
    "favorite_food": "Кукуруза",
    "favorite_toy": "Кость"
}
```
### Список всех собак
Запрос:
```
GET http://127.0.0.1:8000/api/dogs/
```
Ответ:

*Выдаётся список Собак с дополнительным полем "avg_breed_age"*
```json
[
    {
        "id": 1,
        "name": "Шарик",
        "age": 5,
        "breed": 1,
        "gender": "М",
        "color": "Черно-коричневый",
        "favorite_food": "Кукуруза",
        "favorite_toy": "Кость",
        "avg_breed_age": 5
    },
    {
        "id": 2,
        "name": "Круглик",
        "age": 2,
        "breed": 2,
        "gender": "Д",
        "color": "Белый",
        "favorite_food": "Курица",
        "favorite_toy": "Палка",
        "avg_breed_age": 2
    }
]
```