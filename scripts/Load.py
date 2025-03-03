import pandas as pd
import os
import shutil
import openpyxl

# Ler os arquivos CSV com a codificação 'utf-8-sig'
albums = pd.read_csv(r'data\processed\albums_Aphex_processed.csv', encoding='utf-8-sig')
all_tracks = pd.read_csv(r'data\processed\all_tracks_processed.csv', encoding='utf-8-sig')
top_tracks = pd.read_csv(r'data\processed\top_tracks_processed.csv', encoding='utf-8-sig')

# Definir os nomes dos arquivos Excel
top_tracks_excel = "top_tracks_processed.xlsx"  # Alterado para .xlsx
albums_excel = "albums_Aphex_processed.xlsx"    # Alterado para .xlsx
all_tracks_excel = "all_tracks_processed.xlsx"  # Alterado para .xlsx

# Salvar os DataFrames como arquivos Excel
albums.to_excel(albums_excel, index=False)
all_tracks.to_excel(all_tracks_excel, index=False)
top_tracks.to_excel(top_tracks_excel, index=False)

# Lista de arquivos Excel
Excels = [all_tracks_excel, albums_excel, top_tracks_excel]

# Diretório de destino
destino = r'C:\ETL\excel'

# Verificar se o diretório de destino existe, se não, criá-lo
if not os.path.exists(destino):
    os.makedirs(destino)

# Mover os arquivos Excel para o diretório de destino
for excel in Excels:
    source = os.path.join(os.getcwd(), excel)  # Caminho completo do arquivo de origem
    destination = os.path.join(destino, excel)  # Caminho completo do arquivo de destino
    
    if os.path.exists(destination):  
        print(f"Arquivo {excel} já existe em {destino}, não será movido.")
        os.remove(source)  # Remove o arquivo de origem se ele já existir no destino
    else:
        shutil.move(source, destination)  # Move o arquivo para o destino
        print(f"Arquivo {excel} movido para {destino}")