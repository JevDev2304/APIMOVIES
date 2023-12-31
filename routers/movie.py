from fastapi import APIRouter
from fastapi import  Path,Query
from fastapi.responses import  JSONResponse
from typing import List
from config.database import Session
from models.movie import Movie as MovieModel
from fastapi.encoders import jsonable_encoder
from services.movie import MovieService
from schemas.movie import Movie
movie_router = APIRouter()


@movie_router.get("/movies", tags=["movies"],response_model=List[Movie], status_code=200)
def get_movies() -> List[Movie]:
    db = Session()
    result = MovieService(db).get_movies()
    result = jsonable_encoder(result)
    return JSONResponse(content=result, status_code=200)


@movie_router.get("/movies/{id}", tags=["movies"], response_model=Movie)
def get_movie(id: int= Path(ge=1,le=2000)) -> Movie:
    db = Session()
    result = MovieService(db).get_movie(id)
    if not result:
        return JSONResponse(content={"message": "No existe ninguna pelicula con este id"}, status_code=404)
    else:
        return JSONResponse(content=jsonable_encoder(result),status_code=200)


@movie_router.get("/movies/", tags=["movies"],response_model=List[Movie])
def get_movies_by_category(category: str =Query(min_length=5,max_length=15)) -> List[Movie]:
    db = Session()
    result = MovieService(db).get_movie_by_category(category)
    if result :
        return JSONResponse(content=jsonable_encoder(result), status_code=200)
    else:
        return JSONResponse(content={"message": "No existe ninguna pelicula con esta categoria"}, status_code=404)


@movie_router.post("/movies", tags=["movies"], response_model=dict,status_code=201)
def create_movie(movie: Movie) -> dict:
    db = Session()
    MovieService(db).create_movie(movie)
    return JSONResponse(content={"message":"Se registro la pelicula"},status_code=201)


@movie_router.put("/movies/{id}", tags=["movies"],response_model=dict,status_code=200)
def update_movie(id: int ,movie: Movie ) -> dict:
    db = Session()
    result = MovieService(db).get_movie(id)
    if not result:
        return JSONResponse(content={"message": "No existe la pelicula"}, status_code=404)
    MovieService(db).update_movie(id,movie)
    return JSONResponse(content={"message": "Ya se modifico la pelicula"}, status_code=201)


@movie_router.delete("/movies/{id}", tags=["movies"],response_model=dict,status_code=200)
def delete_movie(id: int) -> dict:
    db = Session()
    result = MovieService(db).get_movie(id)
    if not result:
        return JSONResponse(content={"message": "No existe la pelicula"}, status_code=404)
    MovieService(db).delete_movie(result)
    return JSONResponse(content={"message": "Ya se elimino la pelicula"}, status_code=201)