from assertpy import assert_that
from test_data.fakestore_test_data import FakeStoreTestData

class TestFakeStoreAPI:
    def test_get_single_product(self, fakestore_api):
        product = fakestore_api.get_product_by_id(1)
        expected_product = FakeStoreTestData.EXPECTED_PRODUCT_1
        
        assert_that(product['title']).is_equal_to(expected_product.title)
        assert_that(product['price']).is_equal_to(expected_product.price)
        assert_that(product['category']).is_equal_to(expected_product.category)

    def test_get_all_products(self, fakestore_api):
        products = fakestore_api.get_all_products()
        assert_that(products).is_not_empty()
        
        for product in products:
            assert_that(product).contains_key(*FakeStoreTestData.get_expected_product_keys())
            assert_that(product['rating']).contains_key(*FakeStoreTestData.get_expected_rating_keys())

    def test_get_products_by_category(self, fakestore_api):
        for category in FakeStoreTestData.CATEGORIES:
            products = fakestore_api.get_products_by_category(category)
            assert_that(products).is_not_empty()
            for product in products:
                assert_that(product['category']).is_equal_to(category)