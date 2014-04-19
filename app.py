from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/songs/next")
def get_songs_next():
    return jsonify( { 'path' : 'tests/assets/test.mp3' } ), 200

if __name__ == "__main__":
    app.run()