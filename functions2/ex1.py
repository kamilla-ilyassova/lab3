def is_high_rating(movie):
    return movie['imdb'] > 5.5

# Example:
movie_example = {
    "name": "Usual Suspects", 
    "imdb": 7.0,
    "category": "Thriller"
}

print(is_high_rating(movie_example))  