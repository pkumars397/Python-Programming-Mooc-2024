# Write your solution here
def add_movie(database: list, name: str, director: str, year: int, runtime: int):
    dictionary={};
    dictionary["name"]=name
    dictionary["director"]=director
    dictionary["year"]=year
    dictionary["runtime"]=runtime
    database.append(dictionary)