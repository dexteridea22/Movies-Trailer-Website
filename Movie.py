import media
import fresh_tomatoes
dangal=media.Movie("Dangal","Story of a wrestler who makes his daughter wrestlers","http://www.hindustantimes.com/rf/image_size_640x362/HT/p2/2016/07/04/Pictures/aamir-khan-dangal-the-new-poster-of_cdfced44-41c0-11e6-8e05-c384b245cd95.jpg","https://www.youtube.com/watch?v=x_7YlGv9u1g")
Mummy=media.Movie("The Mummy ","Return of a mummy","https://upload.wikimedia.org/wikipedia/en/b/b7/The_Mummy_Returns_poster.jpg","https://www.youtube.com/watch?v=IjHgzkQM2Sg&t=2s")
Avatar=media.Movie("Avatar","Story of love in different worlds","https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg","https://www.youtube.com/watch?v=5PSNL1qE6VY")
Okjannu=media.Movie("ok Jannu","story of love","http://fabnewz.com/wp-content/uploads/2016/12/ok-jaanu-poster-is-out.png","https://www.youtube.com/watch?v=HLdbAdya2po")
Raees=media.Movie("Raees","story of a dacoit","http://images.mid-day.com/images/2015/jul/16-Raees-srk-poster.jpg","https://www.youtube.com/watch?v=J7_1MU3gDk0&t=44s")
Jolly=media.Movie("Jolly LLB","","https://3.bp.blogspot.com/-n9nn6IiOq9s/WFeTamC4V5I/AAAAAAAAKWI/JG_QFP2jAxwQl5F1-4mP54H6agO_G7GUACLcB/s1600/jolly-llb-2-movie-trailer-launch-poster-wallpape-akshay-kumar.JPG","https://www.youtube.com/watch?v=kvjxoBG5euo")
movies=[dangal,Okjannu,Raees,Jolly,Mummy,Avatar]
fresh_tomatoes.open_movies_page(movies)

