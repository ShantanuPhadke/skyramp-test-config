from typing import Union, Annotated
from fastapi import FastAPI, Query, HTTPException
from .models import create_db_and_tables, SessionDep, Item
from sqlmodel import select
from contextlib import asynccontextmanager

app = FastAPI()

create_db_and_tables()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/")
def read_items(session: SessionDep, offset: int=0, limit: Annotated[int, Query(le=100)] = 100) -> list[Item]:
    items = session.exec(select(Item).offset(offset).limit(limit)).all()
    return items

@app.get("/items/{item_id}")
def read_item(item_id: int, session: SessionDep) -> Item:
    item = session.get(Item, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.post("/items/")
def read_item(item: Item) -> Item:
    return item