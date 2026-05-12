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

Рекомендуемый порядок перед сдачей:

1. Создать ветку `develop` от `main` (если её ещё нет в удалённом репозитории):  
   `git checkout -b develop` и запушить.
2. От `develop` создать feature-ветку, например `feature/14.1-oop-intro`.
3. После коммитов открыть **pull request** из feature-ветки в `develop` (или по инструкции наставника).

