from typing import Dict, List, Tuple
import json
import itertools
from statistics import mean

# Opening and Reading the file

with open("data.json", "r") as data:
    ls = json.load(data)    # converted to list of dicts
    

def gen_tuple(ls):
    """
    Creates a Generator object containing tuple with the star name its rating and name of movie
    @param ls: List of dictionaries 
    """
    for i, v in enumerate(ls):
        v["stars"] = v["stars"].split(", ")
        for star in v["stars"]:
            yield (
                star, v["rating"], v["name"]
            )
            
def MergedTuple(grouped):
    """
    Generates a Generator object containing star name, average rating and number of movies 
    @params grouped: List of key value pairs 
    """
    for j in grouped:
        for k, v in j.items():
            yield (
                f"\'{k}\'",
                round(mean([x for x, y in v]), 2),
                len([y for x, y in v])
            )


tupled_list = sorted(
    [x for x in gen_tuple(ls)], 
    key= lambda x: x[0]
    )

grouped = [ {key: list((float(rating), name) for star, rating, name in value)} 
           for key, value in itertools.groupby(tupled_list, lambda x: x[0]) ]


        
final_list = sorted([v for v in MergedTuple(grouped)], key= lambda x: x[2])
null_s=""
for i in final_list:
    star, rating, movies = i

    if movies >= 2: 
        print(f"Star Name: {star:27} | Movies:  {movies} | AVG Rating: {rating}")
    