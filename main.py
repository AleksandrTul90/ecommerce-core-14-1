from __future__ import annotations

import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parent
_SRC = _ROOT / "src"
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

from shop import Category, Product  # noqa: E402


def main() -> None:
    try:
        Product("Бракованный товар", "Неверное количество", 1000.0, 0)
    except ValueError:
        print(
            "Возникла ошибка ValueError прерывающая работу программы при "
            "попытке добавить продукт с нулевым количеством"
        )
    else:
        print(
            "Не возникла ошибка ValueError при попытке добавить продукт "
            "с нулевым количеством"
        )

    product1 = Product(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны",
        "Категория смартфонов",
        [product1, product2, product3],
    )
    print(category1.middle_price())

    category_empty = Category("Пустая категория", "Категория без продуктов", [])
    print(category_empty.middle_price())


if __name__ == "__main__":
    main()
