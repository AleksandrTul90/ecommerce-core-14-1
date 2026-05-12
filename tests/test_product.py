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
