from apiclient.discovery import build

YOUTUBE_API_KEY = 'AIzaSyDqZZK_zsS-zoJd7ybGI1cjmlwRqFFENzE'

youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

def get_info(keyword):
    search_response = youtube.search().list(
        part='id,snippet',
        #検索したい文字列を指定
        q=keyword,
        #視聴回数が多い順に取得
        # order='viewCount',
        # type='video',
    ).execute()

    return search_response

keyword = input('検索キーワードを入力：')
search_response = get_info(keyword)

for sr in search_response.get('items',[]):
    print(sr['snippet']['title'])
    print(sr['snippet']['channelTitle'])
    print('\n')
