import json
from googleapiclient.discovery import build

api_key = 'AIzaSyA08uOLNC85Y761i8tZw4EcaFyXhC7f4_c'

youtube = build('youtube', 'v3', developerKey=api_key)

request = youtube.search().list(
            part='snippet', 
            maxResults=1, 
            regionCode='US',
            q='python'
        )
response = request.execute()

print(json.dumps(response, indent=4))
with open('response.json', 'w') as f:
    json.dump(response, f)