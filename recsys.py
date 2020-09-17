import numpy as np
import reusables

################################################################################################
###        More info about this recys recommender is in jupyter notebook file recys.ipynb ######
################################################################################################


# Load up the files
from tmdb_image import get_image_link

similarities = np.loadtxt('data/similarities.csv', delimiter=',')
movieId2idx = reusables.load_json('data/movieId2idx.json')
movieId2title = reusables.load_json('./data/movieId2title.json')
idx2movieId = reusables.load_json('./data/idx2movieId.json')
movieId2TMDbid = reusables.load_json('./data/movieId2TMDbid.json')

# Titles, This array is sent to front end as choices
TITLES = sorted(list(movieId2title.items()), key=lambda x: x[1])


# Like titles are those titles that are liked by the user
def get_recoms(liked_titles, no_of_recoms=10):
    liked_titles = [movieId2idx[str(i)] for i in liked_titles if str(i) in movieId2idx.keys()]
    number_of_titles = len(liked_titles)
    sim = similarities[liked_titles].sum(axis=0).argsort()[::-1][number_of_titles:no_of_recoms + number_of_titles]
    recoms = [
        (movieId2title[str(idx2movieId[str(i)])], get_image_link(movieId2TMDbid[str(idx2movieId[str(i)])])) for i in
        sim]  # generate recoms with poster image
    return recoms


if __name__ == '__main__':
    # my movie prefrences
    my_movie_lst = [50, 318, 527, 589, 1240, 2959, 4226, 4963, 5989, 8131, 8950, 26614, 33794, 35836, 44665, 48385,
                    48516,
                    48780, 49530, 51540, 52973, 55290, 58559, 59315, 73881, 74458, 74946, 77561, 79132, 80549, 81845,
                    84152,
                    84374, 85414, 86332, 87232, 87869, 88140, 88405, 89745, 91529, 91658, 92259, 102125, 102407, 102903,
                    104879, 105844, 106072, 106782, 109374, 110102, 112175, 112556, 114935, 115569, 115617, 116797,
                    119145,
                    122892, 122900, 122904, 122906, 122912, 122914, 122916, 122920, 122922, 134130, 142488, 150548,
                    152081,
                    157699, 168250, 168252, 194448, 202439]

    print(get_recoms([2085, 79132]))
