from flask import Flask, render_template, request, redirect
from youtubesearchpython import VideosSearch
from pytube import YouTube
from constants import *
from video import Video


app = Flask(__name__)


@app.route(DEFAULT_ROUTE)
def default():
    return render_template(SEARCH_TEMPLATE)


@app.route(SEARCH_ROUTE, methods=[POST])
def search():
    return render_template(RESULTS_TEMPLATE, videos=getVideos(request.form['query']))


@app.route(DOWNLOAD_ROUTE, methods=[POST])
def download():
    video_url = request.form['video_url']
    download_type = request.form['download_type']
    youtube = YouTube(video_url)
    stream = youtube.streams.filter(only_audio=False if download_type == MP4 else True
                                    ,file_extension=MP4).first()
    return redirect(stream.url)


def getVideos(query):
    search_results = VideosSearch(query, QUERY_LIMIT)
    videos = []
    for result in search_results.result()['result']:
        videos.append(Video(result['title'], result['duration'], result['link']))
    return videos


if __name__ == '__main__':
    app.run(debug=True)
    # app.run(debug=True, host='0.0.0.0', port=8000) # for hosting on local network