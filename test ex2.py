from dataclasses import dataclass 

@dataclass(frozen = True)
class Product:
    name: str
    price: float 
    stock: int = 0

class StockError(Exception):
    pass

class ShoppingCart:
    def __init__(self):
        self._items = []

    def add_product(self, product:Product):
        if product.stock == 0:
            raise StockError(f"Товар '{product.name}' отсутствует на складе.")
        self._items.append(product)

    @property
    def total_price(self):
        return sum(x.price for x in self._items)

    @classmethod
    def from_products(cls, product_list: list):
        a = ShoppingCart()
        for x in product_list:
            if x.stock == 0:
                raise StockError
            a._items.append(x)

        return a
            
        

    def __len__(self):
        return len(self._items)

    def __str__(self):
        return f"В вашей корзине {len(self._items)} товаров на сумму {round(sum(x.price for x in self._items), 2)} руб."

    