# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 18:18:56 2025

@author: admin
"""

from fastapi import APIRouter

# APIRouter 객체 생성
router = APIRouter()

# 모든 사용자 조회 API
@router.get("/users", tags=["Users"], summary="모든 사용자 조회")
def get_users():
    """
    모든 사용자 목록을 반환하는 API.
    """
    return {"message": "All users"}

# 새로운 사용자 추가 API
@router.post("/users", tags=["Users"], summary="새로운 사용자 추가")
def create_user():
    """
    새로운 사용자를 추가하는 API.
    """
    return {"message": "User created"}

# 특정 사용자 조회 API
@router.get("/users/{user_id}", tags=["Users"], summary="특정 사용자 조회")
def get_user(user_id: int):
    """
    특정 사용자의 정보를 반환하는 API.
    """
    return {"user_id": user_id, "message": f"User {user_id} details"}

# 특정 사용자 삭제 API
@router.delete("/users/{user_id}", tags=["Users"], summary="특정 사용자 삭제")
def delete_user(user_id: int):
    """
    특정 사용자를 삭제하는 API.
    """
    return {"user_id": user_id, "message": f"User {user_id} deleted"}

