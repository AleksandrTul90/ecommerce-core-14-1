from __future__ import annotations


class PrintCreationMixin:
    """Миксин: при создании объекта выводит класс и параметры."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        super().__init__(*args, **kwargs)
        print(
            f"Создан объект класса {self.__class__.__name__} "
            f"с параметрами: {self!r}"
        )
