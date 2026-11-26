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

def select_movie(movies):
    """Fragt eine Vorstellungs-ID ab, bis sie gültig ist."""
    if not movies:
       print("Keine Vorstellungen vorhanden.")
       return None

    while True:
       movie_id = input("Vorstellungs-ID eingeben: ").strip().upper()
       selected_movie = find_movie(movies, movie_id)

       if selected_movie is None:
          print("Vorstellung nicht gefunden. Bitte erneut eingeben.")
          continue

       return selected_movie

def select_category():
    """Fragt eine gültige Ticketkategorie ab."""
    while True:
       category = input("Kategorie (E/S/K): ").strip().upper()

       if category in ("E", "S", "K"):
          return category

       print("Ungültige Kategorie. Bitte E, S oder K eingeben.")

def select_quantity(available_seats):
    """Fragt eine Ticketanzahl innerhalb der Freienplätze ab."""
    if available_seats < 1:
        print("Keine freien Sitzplätze vorhanden.")
        return None
    
    while True:
       try:
          quantity = int(input("Anzahl Tickets: ").strip())
       except ValueError:
          print("Bitte eine ganze Zahl eingeben.")
          continue

       if quantity < 1:
           print("Die Anzahl muss mindestens 1 sein.")
           continue

       if quantity > available_seats:
          print(f"Es sind nur {available_seats} Plätze verfügbar.")
          continue

       return quantity

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
    selected_movie = select_movie(example_movies)
   
    if selected_movie is not None:
       print(f"Ausgewählt: {selected_movie['title']}")
       available_seats = (
           selected_movie["capacity"] - selected_movie["sold"]
       )
       quantity = select_quantity(available_seats)

       if quantity is not None:
           category = select_category()
           print(f"Ticketkategorie: {category}")
           print(f"Anzahl Tickets: {quantity}")