from typing import List, Dict, Any
from .api_client import BaseAPIClient

class FakeStoreClient(BaseAPIClient):
    def __init__(self):
        super().__init__('https://fakestoreapi.com')

    def get_all_products(self) -> List[Dict[str, Any]]:
        response = self.get('/products')
        return response.json()

    def get_product_by_id(self, product_id: int) -> Dict[str, Any]:
        response = self.get(f'/products/{product_id}')
        return response.json()

    def get_products_by_category(self, category: str) -> List[Dict[str, Any]]:
        response = self.get(f'/products/category/{category}')
        return response.json() 