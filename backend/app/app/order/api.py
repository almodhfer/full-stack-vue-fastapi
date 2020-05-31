from typing import Any, List, Dict

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/", response_model=Dict[str, str])
def read_items(
) -> Any:
    return {'first': 'hello'}
