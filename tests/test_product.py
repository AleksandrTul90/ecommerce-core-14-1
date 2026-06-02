import pytest

from shop.product import LawnGrass, Product, Smartphone


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


def test_product_initialization_raises_on_zero_quantity() -> None:
    with pytest.raises(ValueError) as exc_info:
        Product(
            name="Некорректный товар",
            description="Нельзя создать",
            price=100.0,
            quantity=0,
        )
    assert str(exc_info.value) == "Товар с нулевым количеством не может быть добавлен"


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


def test_product_str_representation() -> None:
    product = Product("Книга", "Учебник по Python", 1500.0, 10)
    assert str(product) == "Книга, 1500.0 руб. Остаток: 10 шт."


def test_product_add_returns_total_stock_value() -> None:
    product_a = Product("Товар A", "Описание A", 100.0, 10)
    product_b = Product("Товар B", "Описание B", 200.0, 2)
    assert product_a + product_b == 1400.0


def test_product_add_non_product_raises_type_error() -> None:
    product = Product("Товар", "Описание", 100.0, 1)
    with pytest.raises(TypeError):
        _ = product + 10


def test_smartphone_initialization() -> None:
    smartphone = Smartphone(
        name="Iphone 15",
        description="512GB, Gray space",
        price=210000.0,
        quantity=8,
        efficiency=98.2,
        model="15",
        memory=512,
        color="Gray space",
    )
    assert smartphone.name == "Iphone 15"
    assert smartphone.description == "512GB, Gray space"
    assert smartphone.price == 210000.0
    assert smartphone.quantity == 8
    assert smartphone.efficiency == 98.2
    assert smartphone.model == "15"
    assert smartphone.memory == 512
    assert smartphone.color == "Gray space"


def test_lawn_grass_initialization() -> None:
    grass = LawnGrass(
        name="Газонная трава",
        description="Элитная трава для газона",
        price=500.0,
        quantity=20,
        country="Россия",
        germination_period="7 дней",
        color="Зеленый",
    )
    assert grass.name == "Газонная трава"
    assert grass.description == "Элитная трава для газона"
    assert grass.price == 500.0
    assert grass.quantity == 20
    assert grass.country == "Россия"
    assert grass.germination_period == "7 дней"
    assert grass.color == "Зеленый"


def test_add_different_product_classes_raises_type_error() -> None:
    smartphone = Smartphone(
        name="Iphone 15",
        description="512GB, Gray space",
        price=210000.0,
        quantity=8,
        efficiency=98.2,
        model="15",
        memory=512,
        color="Gray space",
    )
    grass = LawnGrass(
        name="Газонная трава",
        description="Элитная трава для газона",
        price=500.0,
        quantity=20,
        country="Россия",
        germination_period="7 дней",
        color="Зеленый",
    )
    with pytest.raises(TypeError):
        _ = smartphone + grass
