from server import app

@app.route("/songs/next")
def get_songs_next():
    return jsonify( { 'path' : 'tests/assets/test.mp3' } ), 200
