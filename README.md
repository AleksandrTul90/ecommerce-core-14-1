# E-commerce core (ДЗ 14.1)

Проект на **Poetry**: виртуальное окружение, линтер **flake8**, форматер **black**, тесты **pytest** с отчётом покрытия (**pytest-cov**).

## Реализованный функционал (задание 14.1)

- Класс **`Product`**: поля `name`, `description`, `price`, `quantity`; инициализация через конструктор.
- Класс **`Category`**: поля `name`, `description`, `products` (список товаров); инициализация через конструктор.
- У **`Category`** два **атрибута класса** — `category_count` и `product_count`: при создании каждой категории увеличиваются автоматически (количество категорий и суммарное число товаров по длине списка `products`).
- Дополнительно: функция **`load_categories_from_json`** читает `data/products.json` и строит объекты `Category` с вложенными `Product`.

## Запуск

```bash
poetry install
poetry run python main.py
poetry run pytest
poetry run flake8 src tests main.py
```

Отчёт о покрытии: каталог `htmlcov/` (откройте `index.html` в браузере).

## GitFlow

Работа ведётся в feature-ветке от `develop`, сдача — ссылкой на **pull request** в основную ветку согласно требованиям курса.
