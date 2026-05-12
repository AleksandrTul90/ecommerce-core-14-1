import pytest

from shop.category import Category


@pytest.fixture(autouse=True)
def reset_category_counters() -> None:
    """Изолировать тесты: счётчики класса Category сбрасываются перед каждым тестом."""
    Category.category_count = 0
    Category.product_count = 0
    yield
    Category.category_count = 0
    Category.product_count = 0
