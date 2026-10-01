class Movie:
    def __init__(self,movie_id,movie_name,genre,rating,ticket_price):
        self.movie_id=movie_id
        self.movie_name=movie_name
        self.genre=genre
        self.rating=rating
        self.ticket_price=ticket_price

    def display(movies):
        for movie in movies:
            print(movie.movie_id,movie.movie_name,movie.genre,movie.rating,movie.ticket_price)

    def rating_greater_than_8(movies):
        for movie in movies:
            if movie.rating>8:
                print(movie.movie_name,movie.rating)

    def action_movies(movies):
        for movie in movies:
            if movie.genre=="Action":
                print(movie.movie_name)

    def highest_rating(movies):
        high=movies[0]
        for movie in movies:
            if movie.rating>high.rating:
                high=movie
        print(high.movie_name,high.rating)

    def search(movies,movie_id):
        for movie in movies:
            if movie.movie_id==movie_id:
                print(movie.movie_id,movie.movie_name,movie.genre,movie.rating,movie.ticket_price)
                return
        print("Movie not found")

    def average_rating(movies):
        total=0
        for movie in movies:
            total+=movie.rating
        average=total/len(movies)
        print(f"{average:.2f}")

    def price_greater_than_300(movies):
        for movie in movies:
            if movie.ticket_price>300:
                print(movie.movie_name,movie.ticket_price)