import pytest

from shop.product import Product


def test_product_initialization() -> None:
    product = Product(
        name="Книга",
        description="Учебник по Python",
        price=1500.0,
        quantity=10,
    )
    assert product.name == "Книга"
    assert product.description == "Учебник по Python"
    assert product.price == 1500.0
    assert product.quantity == 10


def test_new_product_from_dict() -> None:
    product = Product.new_product(
        {
            "name": "Наушники",
            "description": "Беспроводные",
            "price": 5000.0,
            "quantity": 4,
        }
    )
    assert product.name == "Наушники"
    assert product.description == "Беспроводные"
    assert product.price == 5000.0
    assert product.quantity == 4


def test_price_setter_rejects_zero_and_negative(
    capsys: pytest.CaptureFixture[str],
) -> None:
    product = Product("Товар", "Описание", 100.0, 1)
    product.price = 0
    captured = capsys.readouterr()
    assert product.price == 100.0
    assert "Цена не должна быть нулевая или отрицательная" in captured.out

    product.price = -50
    captured = capsys.readouterr()
    assert product.price == 100.0
    assert "Цена не должна быть нулевая или отрицательная" in captured.out


def test_price_setter_accepts_positive() -> None:
    product = Product("Товар", "Описание", 100.0, 1)
    product.price = 200.0
    assert product.price == 200.0


def test_price_setter_decrease_requires_confirmation(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    product = Product("Товар", "Описание", 1000.0, 1)
    monkeypatch.setattr("builtins.input", lambda _: "y")
    product.price = 500.0
    assert product.price == 500.0


def test_price_setter_decrease_cancelled(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    product = Product("Товар", "Описание", 1000.0, 1)
    monkeypatch.setattr("builtins.input", lambda _: "n")
    product.price = 500.0
    assert product.price == 1000.0


def test_new_product_merges_duplicate_by_name() -> None:
    existing = Product("Дубликат", "Старый", 100.0, 2)
    products_list = [existing]
    result = Product.new_product(
        {
            "name": "Дубликат",
            "description": "Новый",
            "price": 150.0,
            "quantity": 3,
        },
        existing_products=products_list,
    )
    assert result is existing
    assert existing.quantity == 5
    assert existing.price == 150.0


def test_new_product_merge_keeps_higher_price() -> None:
    existing = Product("Дубликат", "Старый", 200.0, 1)
    products_list = [existing]
    Product.new_product(
        {
            "name": "Дубликат",
            "description": "Новый",
            "price": 100.0,
            "quantity": 1,
        },
        existing_products=products_list,
    )
    assert existing.price == 200.0
    assert existing.quantity == 2
