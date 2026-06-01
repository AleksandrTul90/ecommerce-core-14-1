from __future__ import annotations

from shop.base_product import BaseProduct
from shop.print_creation_mixin import PrintCreationMixin


class Product(PrintCreationMixin, BaseProduct):
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
        super().__init__()

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"{self.name!r}, {self.description!r}, "
            f"{self.price}, {self.quantity})"
        )

    def __str__(self) -> str:
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: object) -> float:
        if not isinstance(other, Product):
            return NotImplemented
        if type(self) is not type(other):
            raise TypeError("Можно складывать только продукты одного типа")
        return (self.price * self.quantity) + (other.price * other.quantity)

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

    def check_change_price(self, new_price: float) -> float | None:
        """Изменение цены с подтверждением пользователя."""
        if self.price == new_price:
            return self.price
        user_confirmed = input(
            "Вы уверены, что хотите изменить цену? (y/n):"
        )
        if user_confirmed.lower() == "y":
            self.price = new_price
            return self.price
        if user_confirmed.lower() == "n":
            return self.price
        return None

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


class Smartphone(Product):
    """Товар-смартфон."""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ) -> None:
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
        super().__init__(name, description, price, quantity)

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"{self.name!r}, {self.description!r}, {self.price}, "
            f"{self.quantity}, {self.efficiency}, {self.model!r}, "
            f"{self.memory}, {self.color!r})"
        )


class LawnGrass(Product):
    """Товар из категории газонной травы."""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ) -> None:
        self.country = country
        self.germination_period = germination_period
        self.color = color
        super().__init__(name, description, price, quantity)

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"{self.name!r}, {self.description!r}, {self.price}, "
            f"{self.quantity}, {self.country!r}, "
            f"{self.germination_period!r}, {self.color!r})"
        )
