from fastapi import APIRouter


product = APIRouter()


@product.get("/products")
async def get_products():
    return {"message": "List of products"}
