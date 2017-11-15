import fresh_tomatoes
import media


matrix = media.Movie("The Matrix", "A computer hacker learns from mysterious rebels about the true nature of his"
                                   " reality and his role in the war against its controllers.",
                     "https://www.movieposter.com/posters/archive/main/9/A70-4902",
                     "https://www.youtube.com/watch?v=vKQi3bBA1y8")

john_wick = media.Movie("John Wick", "An ex-hitman comes out of retirement to track down the gangsters that took "
                                     "everything from him.",
                     "https://images-na.ssl-images-amazon.com/images/I/41i2SoUoRjL._AC_UL320_SR214,320_.jpg",
                     "https://www.youtube.com/watch?v=2AUmvWm5ZDQ")

deadpool = media.Movie("Deadpool", "A fast-talking mercenary with a morbid sense of humor is subjected to a rogue "
                                   "experiment that leaves him with accelerated healing powers and a quest for "
                                   "revenge.",
                     "http://assets1.ignimgs.com/2016/01/14/deadpoolver9xxlgjpg-0d72a1_1280w.jpg",
                     "https://www.youtube.com/watch?v=Xithigfg7dA")

prometheus = media.Movie("Prometheus", "Following clues to the origin of mankind, a team finds a structure on a "
                                       "distant moon, but they soon realize they are not alone.",
                     "https://images-na.ssl-images-amazon.com/images/I/51idf0%2BUveL._SY450_.jpg",
                     "https://www.youtube.com/watch?v=nmJOO6D5RvA")

superbad = media.Movie("Superbad", "Two co-dependent high school seniors are forced to deal with separation "
                                   "anxiety after their plan to stage a booze-soaked party goes awry.",
                     "https://images-na.ssl-images-amazon.com/images/I/510azwwei-L._AC_UL320_SR216,320_.jpg",
                     "https://www.youtube.com/watch?v=NjfzRio8iB8")

super_troopers = media.Movie("Super Troopers", "Five Vermont state troopers, avid pranksters with a knack for "
                                               "screwing up, try to save their jobs and out-do the local police "
                                               "department by solving a crime.",
                     "http://img.moviepostershop.com/super-troopers-movie-poster-2001-1020190702.jpg",
                     "https://www.youtube.com/watch?v=2-9D2qUHN-E")

movies = [matrix, john_wick, deadpool, prometheus, superbad, super_troopers]
#fresh_tomatoes.open_movies_page(movies)
print(media.Movie.VALID_RATINGS)
