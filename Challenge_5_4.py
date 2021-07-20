me = {
    "height": "6",
    "fav_color": "red",
    "fav_author": "Orwell"
}

ans = input("Type height, fav_color or fav_author")

if ans in me:
    result = me[ans]
    print(result)
