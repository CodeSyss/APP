from fastapi import APIRouter
import httpx
from schemas.user import UserCreate

user = APIRouter()

# @user.get("/users")
# async def get_users():
#     return {"message": "List of users"}


# @user.post("/", status_code=status.HTTP_201_CREATED)
# async def create_user(user: UserCreate):
#     # URL del endpoint de NestJS (ajusta según tu configuración)
#     nestjs_url = "http://localhost:3000/user"

#     async with httpx.AsyncClient() as client:
#         # Envía los datos a NestJS
#         response = await client.post(
#             nestjs_url,
#             json=user.dict()  # Convierte el modelo a JSON
#         )

#     # Devuelve la respuesta de NestJS
#     return response.json()

# Responde a POST en /users/ (si usas prefijo) o /users (si no)
@user.post("/users")
async def create_user_endpoint(user_data: UserCreate):
    """
    Endpoint para recibir datos de usuario (name, email) desde Postman
    y reenviarlos al servicio NestJS.
    """
    # URL del endpoint de NestJS (ajusta según tu configuración)
    # Asegúrate que NestJS esté corriendo en http://localhost:3000 y tenga un endpoint POST en /user
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

        # Verifica si NestJS devolvió un error (4xx o 5xx)
        # Si hay error, lanzará una excepción HTTPStatusError
        response.raise_for_status()

    # Devuelve la respuesta JSON de NestJS si todo fue bien
    # (Asegúrate que tu endpoint NestJS devuelva el usuario creado como JSON)
    return response.json()
