import pytest

from shop import BaseEntity, BaseProduct, Order, PrintCreationMixin, Product
from shop.category import Category


def test_product_inherits_base_product() -> None:
    assert issubclass(Product, BaseProduct)


def test_print_creation_mixin_on_product_init(
    capsys: pytest.CaptureFixture[str],
) -> None:
    Product("Товар", "Описание", 1000.0, 5)
    captured = capsys.readouterr()
    assert "Создан объект класса Product" in captured.out
    assert "с параметрами:" in captured.out


def test_check_change_price_same_value() -> None:
    product = Product("Товар", "Описание", 1000.0, 5)
    assert product.check_change_price(1000.0) == 1000.0


def test_check_change_price_confirmed(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    product = Product("Товар", "Описание", 1000.0, 5)
    monkeypatch.setattr("builtins.input", lambda _: "y")
    assert product.check_change_price(800.0) == 800.0


def test_check_change_price_declined(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    product = Product("Товар", "Описание", 1000.0, 5)
    monkeypatch.setattr("builtins.input", lambda _: "n")
    assert product.check_change_price(800.0) == 1000.0


def test_order_creation() -> None:
    product = Product("Товар", "Описание", 1000.0, 5)
    order = Order(product, 2, 2000.0)
    assert order.product is product
    assert order.quantity == 2
    assert order.total_cost == 2000.0
    assert order.name == "Заказ: Товар"


def test_category_inherits_base_entity() -> None:
    assert issubclass(Category, BaseEntity)


def test_print_creation_mixin_in_mro() -> None:
    assert PrintCreationMixin in Product.__mro__
