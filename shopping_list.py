from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# a list to store the shopping items the first time the app is run
shopping_list = ['milk', 'bread', 'eggs']

# model for the shopping item
class ShoppingItem(BaseModel):
    item: str

# endpoint to add an item to the shopping list
@app.post('/shopping_list')
def add_item(item: ShoppingItem):
    shopping_list.append(item.item)
    return {'message': 'Item added to shopping list.'}

# endpoint to get the shopping list
@app.get('/shopping_list')
def get_shopping_list():
    return {'shopping_list': shopping_list}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='localhost', port=8000)
