from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
import client
import base64

load_dotenv()

app = Flask(__name__)

# Search
@app.route("/")
def hello_world():
    return render_template('index.html')

# File system
@app.route("/public")
async def go_link():
    if 'link' in request.args.keys():
        link = request.args.get('link')
        if 'path' in request.args.keys():
            path = request.args.get('path')
        else:
            path = "/"
        data = await client.get_pub_data(link, path)
        pub_url = data['public_key']
        files = data['_embedded']['items']
        return render_template('dir_viewer.html', files=files, pub_url=pub_url)
    else:
        return f'No link found'

# Download
@app.route("/download")
async def get_download():
    link = base64.b64decode(request.args.get('link')).decode('utf-8')
    path = request.args.get('path')
    data = (await client.get_download_link(link=link, path=path))
    return jsonify({'link': data})