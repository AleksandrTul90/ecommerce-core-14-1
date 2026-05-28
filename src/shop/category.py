from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from shop.product import Product


class Category:
    """Категория товаров."""

    category_count: int = 0
    product_count: int = 0

    def __init__(
        self,
        name: str,
        description: str,
        products: list[Product],
    ) -> None:
        self.name = name
        self.description = description
        self.__products: list[Product] = list(products)
        type(self).category_count += 1
        type(self).product_count += len(self.__products)

    def add_product(self, product: Product) -> None:
        """Добавляет товар в приватный список категории."""
        self.__products.append(product)
        type(self).product_count += 1

    def __str__(self) -> str:
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    @property
    def products(self) -> str:
        """Возвращает строку со всеми товарами категории."""
        return "".join(f"{product}\n" for product in self.__products)
