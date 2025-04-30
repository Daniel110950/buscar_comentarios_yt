from googleapiclient.discovery import build

# Substitua pela sua chave de API do YouTube
API_KEY = 'AIzaSyBrFvdtcH0mqzajVq4oZquAR7QuIgiiwSE'
VIDEO_ID = 'o_yiPCiwzUs'

# Conecta à API do YouTube
youtube = build(
    'youtube', 
    'v3', 
    developerKey=API_KEY
    )

# Busca os comentários do vídeo
request = youtube.commentThreads().list(
    part='snippet',
    videoId=VIDEO_ID,
    maxResults=100,
)
response = request.execute()
comments = []

# Mostra os nomes dos usuários que comentaram
for item in response['items']:
    user_name = item['snippet']['topLevelComment']['snippet']['authorDisplayName']
    comments.append([user_name])

# Salva os nomes em um arquivo de texto
with open("usuarios.txt", "w", encoding="utf-8") as f:
    for c in comments:
        f.write(f"@{c[0]}\n")

print('')

for c in comments:
    print(c[0])