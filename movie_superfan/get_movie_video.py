# from googleapiclient.discovery import build
# from googleapiclient.errors import HttpError

# import os

# API_KEY = os.environ['YOUTUBE_API_KEY']
# YOUTUBE_API_SERVICE_NAME = 'youtube'
# YOUTUBE_API_VERSION = 'v3'

# def youtube_video(movie):
#     try:
#         youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=API_KEY)

#         search_response = youtube.search().list(
#             q='movie,' + movie,
#             part='id, snippet',
#             maxResult=1,
#             type='videos',
#             safeSearch='strict'
#         ).execute()

#         first_result = search_response.get('items', [])[0]
#         print(first_result)