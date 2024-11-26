from typing import Dict, Any
from assertpy import assert_that
from test_data.fakestore_test_data import FakeStoreTestData
from test_data.jsonplaceholder_test_data import JSONPlaceholderTestData

class ResponseValidator:
    @staticmethod
    def validate_product_structure(product: Dict[str, Any]) -> None:
        assert_that(product).contains_key(*FakeStoreTestData.get_expected_product_keys())
        if product['rating']:
            assert_that(product['rating']).contains_key(*FakeStoreTestData.get_expected_rating_keys())

    @staticmethod
    def validate_user_structure(user: Dict[str, Any]) -> None:
        assert_that(user).contains_key(*JSONPlaceholderTestData.get_expected_user_keys())
        assert_that(user['address']).contains_key(*JSONPlaceholderTestData.get_expected_address_keys()) 