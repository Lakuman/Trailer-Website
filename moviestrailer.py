# -*- coding: utf-8 -*-
import webbrowser
import medias
import fresh_tomatoes

# Each part as next one represent instances of the movies class.
what_happened_to_monday = medias.Movie(
    "What Happened to Monday",
    "Seven Sisters for each days of the weeks" +
    " in a single child world.",
    "https://images-na.ssl-images-amazon.com/" +
    "images/M/MV5BMjE4MDQxMDg3MF5BMl5BanBnXk" +
    "FtZTgwNjQ0MTcwMzI@._V1_UX182_CR0,0,1822" +
    "68_AL_.jpg",
    "https://www.youtube.com/watch?v=YvEwlpds" +
    "nrM")


porco_rosso = medias.Movie(
    "Porco Rosso",
    "A pig drive planes",
    "https://entertainednews1.files.wordpress.com/2012" +
    "/05/porco_rosso1.jpg",
    "https://youtu.be/awEC-aLDzjs")


treasure_planet = medias.Movie(
    "Treasure Planet",
    "A young man full of dreams share exploring " +
    "an unknown planet.",
    "https://upload.wikimedia.org/wikipedia/en/7/" +
    "7e/Treasure_Planet_poster.jpg",
    "https://www.youtube.com/watch?v=EA68KUb4e7Q")

man_of_steel = medias.Movie(
    "Superman",
    "It’s Supe… No he is just a savior.",
    "https://i.pinimg.com/736x/1b/40/da/1b40da5cfe4fa" +
    "e8c1cc9bfbacc6a19f3--superman--superman-stuff." +
    "jpg",
    "https://youtu.be/DIgYuPdZgpM")

looper = medias.Movie(
    "Looper",
    "A man kill people comping from the future." +
    " One day he should kill himself.",
    "https://images-na.ssl-images-amazon.com/ima" +
    "ges/I/5107O7vLGFL._SY445_.jpg",
    "https://youtu.be/Y0fCYfFHbAI")


batman = medias.Movie(
    "Batman - The Dark Knight",
    "Batman is back and his worst enemy is here" +
    " : Joker",
    "http://pm1.narvii.com/6177/97aba847342a87e" +
    "cb566c55ecfe96d08859ad301_hq.jpg",
    "https://youtu.be/EXeTwQWrcwY")


the_silence_of_the_lambs = medias.Movie(
    "The silence of the lambs",
    "A police inspector ask help" +
    " to a serial killer to find" +
    " another serial killer.",
    "https://images-na.ssl-imag" +
    "es-amazon.com/images/I/71" +
    "Hx1kJa5vL._RI_.jpg",
    "https://youtu.be/ZWCAf-xLV" +
    "2k")

# Here instances of the movies class are defines.
movies = [
    what_happened_to_monday, porco_rosso, man_of_steel, treasure_planet,
    looper, batman, the_silence_of_the_lambs]
# This is the call of fresh_tomatoes class.
fresh_tomatoes.open_movies_page(movies)
