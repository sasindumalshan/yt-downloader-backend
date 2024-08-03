from flask import Flask, request, jsonify
from flask_cors import CORS
import yt_dlp

app = Flask(__name__)
CORS(app)  # Enable CORS

@app.route('/download', methods=['POST'])
def download():
    video_url = request.json.get('url')

    ydl_opts = {
        'format': 'best',
        'outtmpl': 'downloads/%(title)s.%(ext)s',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(video_url, download=False)
        formats = info_dict.get('formats', None)
        return jsonify(formats)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
