from pydantic import BaseModel, Field
from typing import Optional

class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(max_length=15, min_length=5)
    overview: str = Field(max_length=150, min_length=15)
    year: int = Field(le=2023,ge=0)
    rating: float= Field(le=10,ge=0)
    category: str= Field(max_length=15, min_length=5)
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "title": "Mi Pelicula",
                    "overview": "Descripcion de la pelicula",
                    "year": 2022,
                    "rating": 9.9,
                    "category": "Acción"
                }
            ]
        }
    }
