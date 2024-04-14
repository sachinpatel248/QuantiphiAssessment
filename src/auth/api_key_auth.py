from fastapi.security.api_key import APIKeyHeader
from fastapi import Depends, Security, HTTPException

from config import *


api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)


async def _validate_api_key(api_key_value: str = Security(api_key_header)) -> bool:
    if api_key_value and api_key_value == API_KEY:
        return True

    raise HTTPException(
        status_code=403,
        detail="Could not validate credentials",
    )


async def validate_user_using_api_key(
    is_authenticated: bool = Depends(_validate_api_key),
) -> bool:
    return is_authenticated
