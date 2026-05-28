from pathlib import Path

from shop.category import Category
from shop.json_loader import load_categories_from_json
from shop.product import Product
import pytest


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
    assert category.products == (
        "A, 1.0 руб. Остаток: 1 шт.\nB, 2.0 руб. Остаток: 2 шт.\n"
    )
    assert Category.product_count == 2


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
    assert category.products == ""


def test_add_product_appends_and_increments_counter() -> None:
    category = Category("Тест", "Описание", [])
    product = Product("Товар", "Описание товара", 100.0, 3)
    category.add_product(product)
    assert category.products == "Товар, 100.0 руб. Остаток: 3 шт.\n"
    assert Category.product_count == 1


def test_add_product_rejects_non_product() -> None:
    category = Category("Тест", "Описание", [])
    with pytest.raises(TypeError):
        category.add_product("not a product")


def test_products_property_format() -> None:
    product = Product("Книга", "Учебник", 1500.0, 10)
    category = Category("Книги", "Печатные издания", [product])
    assert category.products == "Книга, 1500.0 руб. Остаток: 10 шт.\n"


def test_category_str_shows_total_quantity() -> None:
    category = Category(
        "Смартфоны",
        "Телефоны",
        [
            Product("A", "da", 100.0, 5),
            Product("B", "db", 200.0, 7),
        ],
    )
    assert str(category) == "Смартфоны, количество продуктов: 12 шт."


def test_load_categories_from_json() -> None:
    path = Path(__file__).resolve().parents[1] / "data" / "products.json"
    categories = load_categories_from_json(path)
    assert len(categories) == 2
    assert categories[0].name == "Смартфоны"
    assert "Samsung Galaxy S23 Ultra" in categories[0].products
    assert categories[0].products.count("шт.") == 2
    assert categories[1].name == "Ноутбуки"
    assert categories[1].products.count("шт.") == 1
