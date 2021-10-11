import sys
import os
import logging
import boto3
import requests
import base64
import json
import psycopg2
from datetime import datetime
import pandas as pd
import jsonpath  # pip3 install jsonpath --user

client_id = "74cbd487458843f1ad3f5fa1e914c02f"
client_secret = ""

host = "spotify2.cjwptwa04yyi.ap-northeast-2.rds.amazonaws.com"
port = 5432
username = "sixmini"
database = "postgres"
password = ""


def main():

    try:
        conn = psycopg2.connect(
            host=host,
            database=database,
            user=username,
            password=password)
        cursor = conn.cursor()
    except:
        logging.error("could not connect to rds")
        sys.exit(1)

    headers = get_headers(client_id, client_secret)

    # RDS - 아티스트 ID를 가져오고
    cursor.execute("SELECT id FROM artists LIMIT 10")
    top_track_keys = {
        "id": "id",
        "name": "name",
        "popularity": "popularity",
        "external_url": "external_urls.spotify"
    }
    # Top Tracks Spotify 가져오고
    # Parquet화 : 스파크가 좋아하는 형태
    top_tracks = []
    for (id, ) in cursor.fetchall():

        URL = "https://api.spotify.com/v1/artists/{}/top-tracks".format(id)
        params = {
            'country': 'US'
        }
        r = requests.get(URL, params=params, headers=headers)

        raw = json.loads(r.text)
        
        for i in raw['tracks']:
            top_track = {}
            for k, v in top_track_keys.items():
                value = jsonpath.jsonpath(i, v)
                if type(value) == bool:
                    continue
                top_track.update({k: value[0]})
                top_track.update({'artist_id': id})
                top_tracks.append(top_track)
    

    # track_ids

    track_ids = [i['id'] for i in top_tracks]

    top_tracks = pd.DataFrame(top_tracks)
    top_tracks.to_parquet('top-tracks.parquet', engine='pyarrow', compression='snappy')

    dt = datetime.utcnow().strftime("%Y-%m-%d")

    s3 = boto3.resource('s3')
    object = s3.Object('6mini-spotify', 'top-tracks/dt={}/top-tracks.parquet'.format(dt)) # partition
    data = open('top-tracks.parquet', 'rb')
    object.put(Body=data)
    # S3 import

    tracks_batch = [track_ids[i: i+100] for i in range(0, len(track_ids), 100)]
    audio_features = []
    for i in tracks_batch:

        ids = ','.join(i)
        URL = "https://api.spotify.com/v1/audio-features/?ids={}".format(ids)

        r = requests.get(URL, headers=headers)
        raw = json.loads(r.text)

        audio_features.extend(raw['audio_features'])

    audio_features = pd.DataFrame(audio_features)
    audio_features.to_parquet('audio-features.parquet', engine='pyarrow', compression='snappy')

    s3 = boto3.resource('s3')
    object = s3.Object('6mini-spotify', 'audio-features/dt={}/top-tracks.parquet'.format(dt)) # dt : 파티션 -> 날짜로 만든다
    data = open('audio-features.parquet', 'rb')
    object.put(Body=data)



def get_headers(client_id, client_secret):

    endpoint = "https://accounts.spotify.com/api/token"
    encoded = base64.b64encode("{}:{}".format(client_id, client_secret).encode('utf-8')).decode('ascii')

    headers = {
        "Authorization": "Basic {}".format(encoded)
    }

    payload = {
        "grant_type": "client_credentials"
    }

    r = requests.post(endpoint, data=payload, headers=headers)

    access_token = json.loads(r.text)['access_token']

    headers = {
        "Authorization": "Bearer {}".format(access_token)
    }

    return headers


if __name__=='__main__':
    main()
