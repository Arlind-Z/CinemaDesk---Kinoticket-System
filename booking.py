def show_movies(movies):    
    """Zeigt die übergebenen Vorstellungen in der Konsole an."""
    if not movies:
        print("Keine Vorstellungen vorhanden.")
        return

    for movie in movies:
     available_seats = movie["capacity"] - movie["sold"]
     print(
        f"{movie['id']} | {movie['title']} | "
        f"Saal {movie['hall']} | {movie['time']} | "
        f"{movie['format']} | CHF {movie['base_price']:.2f} | "
        f"Freie Plätze: {available_seats}"
    )

def find_movie(movies,movie_id):
   """Sucht eine Vorstellung anhand ihrer ID"""
   for movie in movies:
      if movie["id"] == movie_id:
         return movie
   
   return None

if __name__ == "__main__":
    example_movies = [
        {
            "id": "V001",
            "title": "Avatar",
            "hall": 4,
            "time": "20:00",
            "format": "3D",
            "base_price": 18.50,
            "capacity": 50,
            "sold": 20,
        },
        {
            "id": "V002",
            "title": "Der König der Löwen",
            "hall": 1,
            "time": "18:00",
            "format": "2D",
            "base_price": 12.00, 
            "capacity": 50,
            "sold": 5,
        },
     ]

    show_movies(example_movies)
    movie_id = input("Vorstellung-ID eingeben: ").strip().upper()
    selected_movie = find_movie(example_movies, movie_id)

    if selected_movie is None:
       print("Vorstellung nicht gefunden")
    else:
       print(f"Ausgewählt: {selected_movie['title']}")