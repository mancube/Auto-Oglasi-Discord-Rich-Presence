from flask import Flask, jsonify, request
import time

app = Flask(__name__)

global url
global title
global price

@app.route('/send_url', methods=['POST'])
def send_url():
    def url_strip(url):
        if "http://" in url or "https://" in url:
            url = url.replace("https://", '').replace("http://", '').replace('\"', '')
        if "/" in url:
            url = url.split('/', 1)[0]
        return url
    resp_json = request.get_data()
    params = resp_json.decode()
    url = params.replace("url=", "")
    urlCache = open("url.txt", "r+", encoding='utf-8')
    urlCache.truncate(0)
    urlCache.write(url)
    urlCache.flush()
    urlCache.close()
    print("url: " + url)
    shortUrlCache = open("urlshort.txt", "r+", encoding='utf-8')
    shortUrlCache.truncate(0)
    shortUrlCache.write(url_strip(url))
    shortUrlCache.flush()
    shortUrlCache.close()
    print("shorturl: " + url_strip(url))
    return jsonify({'message': 'url success!'}), 200

@app.route('/send_title', methods=['POST'])
def send_title():
    resp_json = request.get_data()
    params = resp_json.decode()
    title = params.replace("title=", "")
    titleCache = open("title.txt", "r+", encoding='utf-8')
    titleCache.truncate(0)
    titleCache.write(title)
    titleCache.flush()
    titleCache.close()
    print("title: " + title)
    return jsonify({'message': 'title success!'}), 200

@app.route('/send_price', methods=['POST'])
def send_price():
    resp_json = request.get_data()
    params = resp_json.decode()
    price = params.replace("price=", "")
    priceCache = open("price.txt", "r+")
    priceCache.seek(0)
    priceCache.write(price)
    priceCache.truncate()
    priceCache.flush()
    priceCache.close()
    print("price: " + price)
    return jsonify({'message': 'price success!'}), 200

@app.route('/quit_url', methods=['POST'])
def quit_url():
    resp_json = request.get_data()
    print("Url closed: " + resp_json.decode())
    return jsonify({'message': 'quit url success!'}), 200

@app.route('/quit_title', methods=['POST'])
def quit_title():
    resp_json = request.get_data()
    print("Title closed: " + resp_json.decode())
    return jsonify({'message': 'quit title success!'}), 200

@app.route('/quit_price', methods=['POST'])
def quit_price():
    resp_json = request.get_data()
    print("Price closed: " + resp_json.decode())
    return jsonify({'message': 'quit price success!'}), 200

app.run(host='0.0.0.0', port=5000)

