"""Точка входа: проверка, что ядро магазина импортируется и выполняется без ошибок."""

from __future__ import annotations

import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parent
_SRC = _ROOT / "src"
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

from shop import Category, Product, load_categories_from_json  # noqa: E402


def main() -> None:
    sample = Product(
        name="Демо-товар",
        description="Пример для запуска main.py",
        price=99.5,
        quantity=1,
    )
    demo_category = Category(
        name="Демо-категория",
        description="Категория для проверки",
        products=[sample],
    )
    n = len(demo_category.products)
    print(f"Создано: {demo_category.name}, товаров в категории: {n}")

    json_path = Path(__file__).resolve().parent / "data" / "products.json"
    if json_path.is_file():
        loaded = load_categories_from_json(json_path)
        print(f"Из JSON загружено категорий: {len(loaded)}")


if __name__ == "__main__":
    main()
