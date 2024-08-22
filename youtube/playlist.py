from flask import Flask, request, jsonify
from googleapiclient.discovery import build

app = Flask(__name__)

# Configurações da API do YouTube
API_KEY = 'SUA_API_KEY_AQUI'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

def search_videos(api_key, keywords, max_results=5):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=api_key)
    videos = []

    for keyword in keywords:
        search_response = youtube.search().list(
            q=keyword,
            part='snippet',
            maxResults=max_results,
            type='video'
        ).execute()

        for search_result in search_response.get('items', []):
            video_id = search_result['id']['videoId']
            video_title = search_result['snippet']['title']
            videos.append({'title': video_title, 'video_id': video_id})

    return videos

def create_playlist(api_key, title, description):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=api_key)

    playlists_insert_response = youtube.playlists().insert(
        part='snippet,status',
        body=dict(
            snippet=dict(
                title=title,
                description=description
            ),
            status=dict(
                privacyStatus='public'
            )
        )
    ).execute()

    return playlists_insert_response['id']

def add_video_to_playlist(api_key, playlist_id, video_id):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=api_key)

    youtube.playlistItems().insert(
        part='snippet',
        body={
            'snippet': {
                'playlistId': playlist_id,
                'resourceId': {
                    'kind': 'youtube#video',
                    'videoId': video_id
                }
            }
        }
    ).execute()

@app.route('/create_playlist', methods=['POST'])
def create_playlist_api():
    data = request.json
    keywords = data.get('keywords', [])
    playlist_title = data.get('playlist_title', 'Minha Playlist Criada por Python')
    playlist_description = data.get('playlist_description', 'Uma playlist criada automaticamente usando a API do YouTube.')
    max_results = data.get('max_results', 5)

    if not keywords:
        return jsonify({"error": "Nenhuma palavra-chave fornecida."}), 400

    # Passo 1: Buscar vídeos
    videos = search_videos(API_KEY, keywords, max_results)

    # Passo 2: Criar uma nova playlist
    playlist_id = create_playlist(API_KEY, playlist_title, playlist_description)
    print(f"Playlist criada com ID: {playlist_id}")

    # Passo 3: Adicionar vídeos à playlist
    for video in videos:
        add_video_to_playlist(API_KEY, playlist_id, video['video_id'])
        print(f"Adicionado: {video['title']}")

    return jsonify({
        'playlist_id': playlist_id,
        'videos': [{'title': video['title'], 'video_id': video['video_id']} for video in videos]
    })

if __name__ == '__main__':
    app.run(debug=True)
