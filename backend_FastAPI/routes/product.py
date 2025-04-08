from fastapi import APIRouter
from schemas.product import ProductCreate
import httpx

product = APIRouter()


@product.get("/products")
async def get_products():
    return {"message": "List of products"}


@product.post("/products")
async def create_product(product_data: ProductCreate):
    nestjs_url = "http://localhost:3000/product"

    async with httpx.AsyncClient() as client:
        product_payload = product_data.model_dump() if hasattr(
            "product_data", 'model_dump') else product_data.dict()
        response = await client.post(
            nestjs_url,
            json=product_payload
        )
        response.raise_for_status()

    return response.json()



