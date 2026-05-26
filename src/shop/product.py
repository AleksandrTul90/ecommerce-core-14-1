from __future__ import annotations


class Product:
    """Товар интернет-магазина."""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
    ) -> None:
        self.name = name
        self.description = description
        self.quantity = quantity
        self.__price = price

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        if value < self.__price:
            answer = input(
                "Цена понижается. Подтвердите изменение (y — да, n — нет): "
            )
            if answer.strip().lower() != "y":
                return
        self.__price = value

    @classmethod
    def new_product(
        cls,
        product_data: dict,
        existing_products: list[Product] | None = None,
    ) -> Product:
        """Создаёт товар из словаря; при дубликате по имени объединяет остаток."""
        name = product_data["name"]
        description = product_data["description"]
        price = product_data["price"]
        quantity = product_data["quantity"]

        if existing_products is not None:
            for product in existing_products:
                if product.name == name:
                    product.quantity += quantity
                    if price > product.price:
                        product.price = price
                    return product

        return cls(
            name=name,
            description=description,
            price=price,
            quantity=quantity,
        )
