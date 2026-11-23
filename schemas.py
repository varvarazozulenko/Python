from pydantic import BaseModel, Field, EmailStr

from models import UserRole
from typing import Optional, List
import strawberry

class UserRegister(BaseModel):
    email: EmailStr
    password: str = Field(min_length=6)
    
class UserRoleUpdate(BaseModel):
    role: UserRole

@strawberry.type
class Product:
    id: strawberry.ID
    name: str
    price: float
    description: Optional[str] = None
    
@strawberry.type 
class User:
    id: strawberry.ID
    name: str
    
    @strawberry.field
    def products(self) -> List[Product]:
        return [
            products.get(1),
            products.get(2)
        ]
       
products = {
    1: Product(id=1, name="Laptop", price=80000.5),
    2: Product(id=2, name="Laptop2", price=80000.5),
    3: Product(id=3, name="Laptop3", price=80000.5),
    4: Product(id=4, name="Laptop4", price=80000.5)
}

users = {
    1: User(id=1, name="Mikko"),
    2: User(id=2, name="Mikko2"),
}

@strawberry.type
class Query:
    @strawberry.field
    def product(self, id:int) -> Optional[Product]:
       return products.get(id)
   
    @strawberry.field
    def user(self, id:int) -> Optional[User]:
        return users.get(id)
    
    @strawberry.field
    def products(self) ->List[Product]:
        return list(products.values())
    
   
schema = strawberry.Schema(query=Query)