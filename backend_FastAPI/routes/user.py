from fastapi import APIRouter
import httpx
from schemas.user import UserCreate

user = APIRouter()

@user.post("/users")
async def create_user_endpoint(user_data: UserCreate):
    """
    Endpoint para recibir datos de usuario (name, email) desde Postman
    y reenviarlos al servicio NestJS.
    """
    # URL del endpoint de NestJS (ajusta según tu configuración)
    nestjs_url = "http://localhost:3000/user"

    async with httpx.AsyncClient() as client:
        # Envía los datos a NestJS
        # Nota: Pydantic v2+ usa model_dump(), v1 usa dict()
        user_payload = user_data.model_dump() if hasattr(
            user_data, 'model_dump') else user_data.dict()

        response = await client.post(
            nestjs_url,
            json=user_payload
        )

        response.raise_for_status()
    return response.json()
