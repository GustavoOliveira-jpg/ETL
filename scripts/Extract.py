
import pandas as pd
import requests 
import os
from dotenv import load_dotenv, find_dotenv
import base64
import json

# procura em todos os diretórios o arquivo .env
dotenv_path = find_dotenv()
#carrega as variáveis de ambiente que estão no arquivo .env
load_dotenv(dotenv_path)

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')

def get_token():
    string = CLIENT_ID + ":" + CLIENT_SECRET
    string_bytes = string.encode('ascii')
    bytes_base64 = base64.b64encode(string_bytes)
    base64_string = bytes_base64.decode('ascii')

    url = 'https://accounts.spotify.com/api/token'
    headers = {
        "Authorization" : f'Basic {base64_string}',
        "Content-Type" : "application/x-www-form-urlencoded"
        }
    body = {
        "grant_type" : "client_credentials"
    }
    response = requests.post(url, headers=headers, data=body)
    token = response.json()["access_token"]
    return token

#response.json = {'access_token': 'BQD0taO_LHqVqgLap582uHpIDYVlrGn3p6EuYKOyo6gD5EuxeBcGnE_T3vEY3EnY3PGgWkV9ZQv9zFlwfPCdVt8C7XPUYmMDAog8EjcCBR_uXATld_6cCZT0Aeqk4KLXHEYBa8jNBZ8',
#  'token_type': 'Bearer', 
# 'expires_in': 3600}

def get_auth_header(token):
   return {"Authorization" : f"Bearer {token}"}


def search_artist(token, artista):
    headers = get_auth_header(token)
    query = f"https://api.spotify.com/v1/search?q={artista}&type=artist&limit=1"
    result = requests.get(query, headers=headers)
    response = result.json()['artists']['items']
    return response[0]


def Artist_Albums(token, artista_id):
    albums = []
    headers = get_auth_header(token)
    query = f"https://api.spotify.com/v1/artists/{artista_id}/albums"
    result = requests.get(query, headers=headers)
    response = json.loads(result.content)['items']
    while query:
        response = requests.get(query, headers=headers)
        data = response.json()
        albums.extend(data['items'])
        query = data['next']  # Próxima página de resultados (paginção)
    return albums
    


def get_tracks_from_album(token, album_id):
    headers = get_auth_header(token)
    query = f"https://api.spotify.com/v1/albums/{album_id}/tracks"
    response = requests.get(query, headers=headers)
    return response.json()['items']

def get_all_tracks(token, artista_id):
    albums = Artist_Albums(token, artista_id)
    all_tracks = []
    for album in albums:
        tracks = get_tracks_from_album(token, album['id'])
        for track in tracks:
            track['album_name'] = album['name']  # Adiciona o nome do álbum à música
        all_tracks.extend(tracks)
    return all_tracks

def search_artist_music(token, artista_id):
    headers = get_auth_header(token)
    query = f"https://api.spotify.com/v1/artists/{artista_id}/top-tracks?country=BR"
    result = requests.get(query, headers=headers)
    response = json.loads(result.content)['tracks']
    return response




token = get_token()
artista = search_artist(token, 'Aphex Twin')
artista_id = artista['id']
Top_musicas = search_artist_music(token, artista_id)
albums = Artist_Albums(token, artista_id)
all_tracks = get_all_tracks(token, artista_id)

#def get_tracks_from_album(token, album_id):
    #headers = get_auth_header(token)
   # query = f"https://api.spotify.com/v1/albums/{album_id}/tracks"
    #response = requests.get(query, headers=headers)
    #return response.json()['items']

#def get_all_tracks(token, artista_id):
   # albums = Artist_Albums(token, artista_id)
    #all_tracks = []
   # for album in albums:
        #tracks = get_tracks_from_album(token, album['id'])
       # for track in tracks:
            #track['album_name'] = album['name']  # Adiciona o nome do álbum à música
        #all_tracks.extend(tracks)
    #return all_tracks

    #for idx, track in enumerate(all_tracks):
    #print(f'{idx+1}. {track["name"]} (Álbum: {track["album_name"]})')
###
#Esta parte inteira foi feita pelo deepseek, pois a API do Spotify não possui endpoint para pegar todas as musicas de um determinado artista, de resto, todas as outras foram dfeitas por mim em parceria com conteúdos na internet
#Claro, deixarei links de referência

#for idx, track in enumerate(all_tracks):
    #print(f'{idx+1}. {track["name"]} (Álbum: {track["album_name"]})')

#for idx, musica in enumerate(Top_musicas):
   #print(f'{idx+1}. {musica["name"]}')



#for idx, aalbum in enumerate(albums):
    #print(f'{idx+1}. {aalbum["name"]}')

with open('all_tracks.json', 'a') as file:
    json.dump(all_tracks, file, indent=2)

with open('top_tracks.json', 'a') as file:
    json.dump(Top_musicas, file, indent=2)

with open('albums.json', 'a') as file:
    json.dump(albums, file, indent=2)