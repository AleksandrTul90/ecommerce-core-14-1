from __future__ import annotations

import json
from pathlib import Path

from shop.category import Category
from shop.product import Product


def load_categories_from_json(file_path: str | Path) -> list[Category]:
    """Читает JSON с категориями и товарами и возвращает список объектов Category."""
    path = Path(file_path)
    raw = path.read_text(encoding="utf-8")
    data = json.loads(raw)
    categories: list[Category] = []
    for item in data:
        products = [
            Product(
                name=p["name"],
                description=p["description"],
                price=p["price"],
                quantity=p["quantity"],
            )
            for p in item["products"]
        ]
        categories.append(
            Category(
                name=item["name"],
                description=item["description"],
                products=products,
            )
        )
    return categories
