import pandas as pd
import requests 
import os
from dotenv import load_dotenv, find_dotenv
import base64
import json
import numpy as np
import shutil

with open('albums.json') as f:
    albums_data = json.load(f)

with open('all_tracks.json') as g:
    all_tracks_data = json.load(g)

with open('top_tracks.json') as h:
    top_tracks_data = json.load(h)



df_all_tracks = pd.DataFrame(all_tracks_data)

df_albums = pd.DataFrame(albums_data)

df_top_tracks = pd.DataFrame(top_tracks_data)


df_all_tracks_clean = df_all_tracks.drop(['artists','disc_number','restrictions','preview_url','href','type','is_local'], axis=1)

df_all_tracks_clean.iloc[310:320]



x = df_all_tracks_clean['available_markets'] #verifica quantos países permitem a reprodução da faixa na primeira linha

print(len(x)) 


# Conjunto de siglas totais (códigos de países)
siglas_totais = {
    'AF', 'AL', 'DZ', 'AS', 'AD', 'AO', 'AI', 'AQ', 'AG', 'AR', 'AM', 'AW', 'AU', 'AT', 'AZ', 
    'BS', 'BH', 'BD', 'BB', 'BY', 'BE', 'BZ', 'BJ', 'BM', 'BT', 'BO', 'BA', 'BW', 'BR', 'IO', 
    'BN', 'BG', 'BF', 'BI', 'KH', 'CM', 'CA', 'CV', 'KY', 'CF', 'TD', 'CL', 'CN', 'CX', 'CC', 
    'CO', 'KM', 'CD', 'CG', 'CK', 'CR', 'CI', 'HR', 'CU', 'CY', 'CZ', 'DK', 'DJ', 'DM', 'DO', 
    'EC', 'EG', 'SV', 'GQ', 'ER', 'EE', 'SZ', 'ET', 'FK', 'FO', 'FJ', 'FI', 'FR', 'GF', 'PF', 
    'TF', 'GA', 'GM', 'GE', 'DE', 'GH', 'GI', 'GR', 'GL', 'GD', 'GP', 'GU', 'GT', 'GG', 'GN', 
    'GW', 'GY', 'HT', 'HM', 'VA', 'HN', 'HK', 'HU', 'IS', 'IN', 'ID', 'IR', 'IQ', 'IE', 'IM', 
    'IL', 'IT', 'JM', 'JP', 'JE', 'JO', 'KZ', 'KE', 'KI', 'KP', 'KR', 'KW', 'KG', 'LA', 'LV', 
    'LB', 'LS', 'LR', 'LY', 'LI', 'LT', 'LU', 'MO', 'MG', 'MW', 'MY', 'MV', 'ML', 'MT', 'MH', 
    'MQ', 'MR', 'MU', 'YT', 'MX', 'FM', 'MD', 'MC', 'MN', 'ME', 'MS', 'MA', 'MZ', 'MM', 'NA', 
    'NR', 'NP', 'NL', 'NC', 'NZ', 'NI', 'NE', 'NG', 'NU', 'NF', 'MK', 'MP', 'NO', 'OM', 'PK', 
    'PW', 'PS', 'PA', 'PG', 'PY', 'PE', 'PH', 'PN', 'PL', 'PT', 'PR', 'QA', 'RE', 'RO', 'RU', 
    'RW', 'BL', 'SH', 'KN', 'LC', 'MF', 'PM', 'VC', 'WS', 'SM', 'ST', 'SA', 'SN', 'RS', 'SC', 
    'SL', 'SG', 'SX', 'SK', 'SI', 'SB', 'SO', 'ZA', 'GS', 'SS', 'ES', 'LK', 'SD', 'SR', 'SJ', 
    'SE', 'CH', 'SY', 'TW', 'TJ', 'TZ', 'TH', 'TL', 'TG', 'TK', 'TO', 'TT', 'TN', 'TR', 'TM', 
    'TC', 'TV', 'UG', 'UA', 'AE', 'GB', 'US', 'UY', 'UZ', 'VU', 'VE', 'VN', 'WF', 'EH', 'YE', 
    'ZM', 'ZW'
}

def VerificarSiglasFaltantes(siglas_totais, x):
    for i, linhas in enumerate(x.to_numpy()):
        linha = set(linhas)  
        siglas_faltantes = siglas_totais - linha  
        print(f"Linha {i+1}:{len(siglas_faltantes)} mercados não aceitam a comercialização das musicas do Aphex Twin, sendo eles: {siglas_faltantes}.")






name = df_all_tracks['artists']
df_name= pd.DataFrame(name)

dict_artist = df_name.to_dict()

nome = dict_artist['artists'][0][0]['name']
uri = dict_artist['artists'][0][0]['uri']
external_urls =  dict_artist['artists'][0][0]['external_urls']['spotify']
dict_artist['artists'][0][0]['external_urls']['spotify']
df_all_tracks_clean['external_urls'] = dict_artist['artists'][0][0]['external_urls']['spotify']




df_all_tracks_clean.drop(['uri'], axis=1)

df_all_tracks_processed = df_all_tracks_clean.drop(['uri'], axis=1)



df_albums['album_group'] == 'appears_on'

df_albums_Aphex = df_albums[df_albums['album_group'] != 'appears_on']
df_albums_Aphex_clean = df_albums_Aphex.drop(['href','type','release_date_precision','images'], axis=1)

dict_album = df_albums_Aphex_clean.to_dict()
nome = dict_album['artists'][0][0]['name']
uri = dict_album['artists'][0][0]['uri']
external_urls =  dict_album['artists'][0][0]['external_urls']['spotify']

df_albums_Aphex_clean['external_urls'] = dict_album['artists'][0][0]['external_urls']['spotify']
df_albums_Aphex_clean['uri'] = uri = dict_album['artists'][0][0]['uri']

df_albums_Aphex_clean.drop(['artists'], axis=1)

df_albums_Aphex_processed = df_albums_Aphex_clean.drop(['artists'], axis=1)

df_top_tracks_clean = df_top_tracks.drop(['album','href','is_local','is_playable','preview_url','disc_number','uri','external_ids'],axis=1)

dict_top_tracks = df_top_tracks_clean.to_dict()

nome_top_tracks = dict_top_tracks['artists'][0][0]['name']
df_top_tracks_clean['external_urls'] = dict_top_tracks['artists'][0][0]['external_urls']['spotify']
df_top_tracks_clean['uri'] = uri = dict_top_tracks['artists'][0][0]['uri']
df_top_tracks_clean['nome'] = nome_top_tracks
df_top_tracks_processed = df_top_tracks_clean.drop(['artists'], axis=1)



top_tracks_csv = "top_tracks_processed.csv"
albums_csv = "albums_Aphex_processed.csv"
all_tracks_csv = "all_tracks_processed.csv"

df_top_tracks_processed.to_csv(top_tracks_csv, index=False)
df_albums_Aphex_processed.to_csv(albums_csv, index=False)
df_all_tracks_processed.to_csv(all_tracks_csv, index=False)

csvs = [all_tracks_csv, albums_csv, top_tracks_csv]

destino = r'C:\ETL\data\processed'
for csv in csvs:
    source = os.path.join(os.getcwd(), os.path.basename(csv))
    destination = os.path.join(destino, os.path.basename(csv))
    if os.path.exists(destination):  
        print(f"Arquivo {csv} já existe em {destino}, não será movido.")
        os.remove(source) #quando rodava mais de uma vez, o arquivo que não era movido ficava dentro da pasta de origem (essa aqui), então resolvi excluir, acho que se apenas movesse denovo o arquivo csv gerado iria sobrescrever o antigo (que ja estava na pasta de destino)
    else:
        shutil.move(source, destination)
        print(f"Arquivo {csv} movido para {destino}")
