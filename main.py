import sqlite3

from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3

class Country(BaseModel):
    name: str
    steel: int
    wood: int
    food: int
    population: int

    # def __init__(self, name: str, steel: int, wood: int, food: int, population: int):
    #     super().__init__()
    #     self.name = name
    #     self.steel = steel
    #     self.wood = wood
    #     self.food = food
    #     self.population = population


app = FastAPI()


countries = [
    Country(name='France',steel=5000,wood=3000,food=10000,population=3000),
    Country(name='Poland',steel=4000,wood=2000,food=14000,population=6000)
]
#
# con =sqlite3.connect("country.db")
# cur = None
# try:
#     cur = con.cursor()
#     cur.execute("CREATE TABLE country(name,steel,wood,food,population)")
#     cur.execute("""INSERT INTO countries VALUES
#         ('France',5000,3000,10000,3000),
#         ('Poland',4000,2000,14000,6000)""")
#     con.commit()
# except sqlite3.OperationalError:
#     pass
#     con.close()


@app.post("/add")
async def add_country(country: Country):
    countries.append(country)
    return {"wiadomosc": "Dodano kraj pomyslnie"}

@app.get("/countries")
async def get_country():
    return countries

@app.post("/update_country/{country_id}")
async def add_country(country_id: int, country:Country):
    pass
