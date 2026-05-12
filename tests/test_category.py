from pathlib import Path

from shop.category import Category
from shop.json_loader import load_categories_from_json
from shop.product import Product


def test_category_initialization() -> None:
    p1 = Product("A", "da", 1.0, 1)
    p2 = Product("B", "db", 2.0, 2)
    category = Category(
        name="Электроника",
        description="Гаджеты",
        products=[p1, p2],
    )
    assert category.name == "Электроника"
    assert category.description == "Гаджеты"
    assert len(category.products) == 2
    assert category.products[0] is p1
    assert category.products[1] is p2


def test_category_count_increments() -> None:
    assert Category.category_count == 0
    Category("c1", "d1", [])
    assert Category.category_count == 1
    Category("c2", "d2", [])
    assert Category.category_count == 2


def test_product_count_sums_list_lengths() -> None:
    assert Category.product_count == 0
    Category("c1", "d1", [Product("x", "y", 1.0, 1)])
    assert Category.product_count == 1
    Category(
        "c2",
        "d2",
        [
            Product("a", "b", 1.0, 1),
            Product("c", "d", 2.0, 2),
        ],
    )
    assert Category.product_count == 3


def test_category_products_is_copied() -> None:
    shared: list[Product] = []
    category = Category("name", "desc", shared)
    shared.append(Product("p", "d", 1.0, 1))
    assert len(category.products) == 0


def test_load_categories_from_json() -> None:
    path = Path(__file__).resolve().parents[1] / "data" / "products.json"
    categories = load_categories_from_json(path)
    assert len(categories) == 2
    assert categories[0].name == "Смартфоны"
    assert len(categories[0].products) == 2
    assert categories[0].products[0].name == "Samsung Galaxy S23 Ultra"
    assert categories[1].name == "Ноутбуки"
    assert len(categories[1].products) == 1
