from assertpy import assert_that
from test_data.jsonplaceholder_test_data import JSONPlaceholderTestData

class TestJSONPlaceholderAPI:
    def test_get_users_status_code(self, jsonplaceholder_api):
        users = jsonplaceholder_api.get_all_users()
        assert_that(users).is_not_none()

    def test_users_count(self, jsonplaceholder_api):
        users = jsonplaceholder_api.get_all_users()
        assert_that(len(users)).is_equal_to(JSONPlaceholderTestData.EXPECTED_USER_COUNT)

    def test_first_user_structure(self, jsonplaceholder_api):
        users = jsonplaceholder_api.get_all_users()
        first_user = users[0]
        assert_that(first_user).contains_key(*JSONPlaceholderTestData.get_expected_user_keys())
        assert_that(first_user['address']).contains_key(*JSONPlaceholderTestData.get_expected_address_keys())

    def test_third_user_data(self, jsonplaceholder_api):
        user = jsonplaceholder_api.get_user_by_id(3)
        expected_user = JSONPlaceholderTestData.EXPECTED_USER_3
        assert_that(user['name']).is_equal_to(expected_user.name)
        assert_that(user['username']).is_equal_to(expected_user.username)
        assert_that(user['email']).is_equal_to(expected_user.email) 