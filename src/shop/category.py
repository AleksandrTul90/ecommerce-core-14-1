from __future__ import annotations

from shop.base_entity import BaseEntity
from shop.product import Product


class Category(BaseEntity):
    """Категория товаров."""

    category_count: int = 0
    product_count: int = 0

    def __init__(
        self,
        name: str,
        description: str,
        products: list[Product],
    ) -> None:
        self._name = name
        self.description = description
        self.__products: list[Product] = list(products)
        type(self).category_count += 1
        type(self).product_count += len(self.__products)

    @property
    def name(self) -> str:
        return self._name

    def add_product(self, product: Product) -> None:
        """Добавляет товар в приватный список категории."""
        if not isinstance(product, Product):
            raise TypeError(
                "Можно добавлять только объекты Product или его наследников"
            )
        self.__products.append(product)
        type(self).product_count += 1

    def __str__(self) -> str:
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    @property
    def products(self) -> str:
        """Возвращает строку со всеми товарами категории."""
        return "".join(f"{product}\n" for product in self.__products)

    def middle_price(self) -> float:
        """Возвращает среднюю цену товаров в категории."""
        try:
            return sum(product.price for product in self.__products) / len(
                self.__products
            )
        except ZeroDivisionError:
            return 0.0
