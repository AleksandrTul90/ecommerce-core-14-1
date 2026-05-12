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
        self.products = list(products)
        type(self).category_count += 1
        type(self).product_count += len(self.products)
