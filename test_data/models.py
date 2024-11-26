from dataclasses import dataclass
from typing import Dict, Any, Optional

@dataclass
class Address:
    street: str
    suite: str
    city: str
    zipcode: str
    geo: Dict[str, float]

@dataclass
class User:
    id: int
    name: str
    username: str
    email: str
    address: Address
    phone: str
    website: str
    company: Dict[str, str]

@dataclass
class Product:
    id: int
    title: str
    price: float
    description: str
    category: str
    image: str
    rating: Optional[Dict[str, Any]] = None 