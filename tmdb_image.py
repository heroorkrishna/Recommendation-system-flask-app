import requests
import requests_cache

requests_cache.install_cache()


def get_image_link(movieId):
    response_json = requests.get('https://api.themoviedb.org/3/movie/{}?api_key={}&language=en-US'.format(movieId,                                                                                                     '695405dd49c500e659c471af7f59c9b5')).json()
    if 'poster_path' in response_json:
        poster_path = response_json['poster_path']
        poster_link = 'https://image.tmdb.org/t/p/w154'+poster_path
        return poster_link
    return ' '

if __name__ == '__main__':
    movieId = 525705
    print(get_image_link(movieId))

