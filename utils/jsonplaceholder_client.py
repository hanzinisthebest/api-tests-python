from typing import List, Dict, Any
from .api_client import BaseAPIClient

class JSONPlaceholderClient(BaseAPIClient):
    def __init__(self):
        super().__init__('https://jsonplaceholder.typicode.com')

    def get_all_users(self) -> List[Dict[str, Any]]:
        response = self.get('/users')
        return response.json()

    def get_user_by_id(self, user_id: int) -> Dict[str, Any]:
        response = self.get(f'/users/{user_id}')
        return response.json()

    def get_user_posts(self, user_id: int) -> List[Dict[str, Any]]:
        response = self.get(f'/users/{user_id}/posts')
        return response.json() 