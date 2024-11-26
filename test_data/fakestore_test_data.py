from .models import Product

class FakeStoreTestData:
    EXPECTED_PRODUCT_1 = Product(
        id=1,
        title='Fjallraven - Foldsack No. 1 Backpack, Fits 15 Laptops',
        price=109.95,
        description='Your perfect pack for everyday use...',
        category="men's clothing",
        image='https://fakestoreapi.com/img/81fPKd-2AYL._AC_SL1500_.jpg',
        rating={'rate': 3.9, 'count': 120}
    )

    CATEGORIES = [
        "men's clothing",
        "women's clothing",
        "electronics",
        "jewelery"
    ]

    @staticmethod
    def get_expected_product_keys():
        return ['id', 'title', 'price', 'description', 'category', 'image', 'rating']

    @staticmethod
    def get_expected_rating_keys():
        return ['rate', 'count'] 