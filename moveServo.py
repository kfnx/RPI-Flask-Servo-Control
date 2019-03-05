@app.route('/', methods = ['GET'])
def index():
    return "siodank";

@app.route('/stats', methods = ['GET'])
def stats():
    return "stats @pi";

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)	