from fastapi import APIRouter

router = APIRouter(prefix="/services", tags=["services"])


@router.get("")
def list_services() -> list[dict[str, str]]:
    return []
