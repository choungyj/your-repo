# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 18:16:44 2025

@author: admin
"""

from fastapi import APIRouter

router = APIRouter()

@router.get("/items")
def get_items():
    return {"message": "All items"}

@router.get("/items/{item_id}")
def get_item(item_id: int):
    return {"message": f"Item {item_id}"}
