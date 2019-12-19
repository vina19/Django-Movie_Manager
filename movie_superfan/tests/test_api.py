from django.test import TestCase
from unittest.mock import patch, call
from movie_superfan.views_movie_list import get_movie_data
from movie_superfan.views_movie_video import youtube_video

# class TestImdbAPI(TestCase):

#     @patch('movie_superfan.views_movie_list')
#     def test_get_data_for_movies(self, mock_movies):
        
#         test_imdb_response = {
#             'results': [
#                 { 
#                     'popularity': 293.642, 
#                     'vote_count': 344, 
#                     'video': False, 
#                     'poster_path': '/l4iknLOenijaB85Zyb5SxH1gGz8.jpg', 
#                     'id': 512200, 
#                     'adult': False, 
#                     'backdrop_path': "/zTxHf9iIOCqRbxvl8W5QYKrsMLq.jpg", 
#                     'original_language': "en", 
#                     'original_title': "Jumanji: The Next Level", 
#                     'genre_ids' : [
#                         28, 
#                         12, 
#                         35, 
#                         14
#                     ],
#                     'title' : "Jumanji: The Next Level",
#                     'vote_average': 6.8,
#                     'overview': "In Jumanji: The Next Level, the gang is back but the game has changed. As they return to rescue one of their own, the players will have to brave parts unknown from arid deserts to snowy mountains, to escape the world's most dangerous game.",
#                     'release_date': "2019-12-04"
#                 }
#             ],
#             'page': 1,
#             'total_results': 278,
#             'dates': {
#                 'maximum': "2020-01-15",
#                 'minimum': "2019-12-25"
#             },
#             'total_pages': 14
#         }
        
#         mock_movies = [{'title' : "Jumanji: The Next Level", 'release_date': "2019-12-04", 
#         'overview': "In Jumanji: The Next Level, the gang is back but the game has changed. As they return to rescue one of their own, the players will have to brave parts unknown from arid deserts to snowy mountains, to escape the world's most dangerous game.",
#         'vote_average': 6.8, 'poster_path': '/l4iknLOenijaB85Zyb5SxH1gGz8.jpg'}]
        
#         movie = get_movie_data(test_imdb_response)

#         self.assertEqual(mock_movies, movie)

# class TestYoutubeVideo(TestCase):

#     @patch('movie_superfan.views_movie_video')
#     def test_get_youtube_video(self, mock_youtube_video):

#         mock_youtube_video = ['F6QaLsw8EWY']

#         test_youtube_response = { 
#             "kind": "youtube#searchListResponse", 
#             "etag": "\"j6xRRd8dTPVVptg711_CSPADRfg/zYwdMPcHy8SNh_PY5lF8pN-llnk\"", 
#             "nextPageToken": "CAUQAA", 
#             "regionCode": "US", 
#             "pageInfo": {
#                 "totalResults": 1000000, 
#                 "resultsPerPage": 5}, 
#             "items": [{
#                 "kind": "youtube#searchResult", 
#                 "etag": "\"j6xRRd8dTPVVptg711_CSPADRfg/QqYjZM00a3ciXvwZdSM0ok_eOus\"", 
#                 "id": {
#                     "kind": "youtube#video",
#                     "videoId": "gIOyB9ZXn8s"
#                 },
#                 "snippet": {
#                     "publishedAt": "2019-12-04T16:30:01.000Z",
#                     "channelId": "UCgwv23FVv3lqh567yagXfNg",
#                     "title": "Idina Menzel, AURORA - Into the Unknown (From &quot;Frozen 2&quot;)",
#                     "description": "Watch the full “Into the Unknown” sequence from Disney's Frozen 2 featuring the original song performed by Idina Menzel (voice of Elsa) featuring AURORA and ...",
#                     "thumbnails": {
#                     "default": {
#                     "url": "https://i.ytimg.com/vi/gIOyB9ZXn8s/default.jpg",
#                     "width": 120,
#                     "height": 90
#                     },
#                     "medium": {
#                     "url": "https://i.ytimg.com/vi/gIOyB9ZXn8s/mqdefault.jpg",
#                     "width": 320,
#                     "height": 180
#                     },
#                     "high": {
#                     "url": "https://i.ytimg.com/vi/gIOyB9ZXn8s/hqdefault.jpg",
#                     "width": 480,
#                     "height": 360
#                     }
#                     },
#                     "channelTitle": "DisneyMusicVEVO",
#                     "liveBroadcastContent": "none"
#                 }
#             }]
#         }

#         mock_youtube_video.side_effect = [test_youtube_response]

#         get_youtube_video = youtube_video(test_youtube_response)

#         self.assertEqual(get_youtube_video, test_youtube_response)



