from flask import Flask, g, request, jsonify, send_from_directory
from API import init, makeTree, Insert, Delete, Traverse, Destroy, makeResult

app = Flask(__name__, static_folder='dist', static_url_path='')
host_addr = "0.0.0.0"
host_port = 5000

# 전역 변수
lib = None
tree = None

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/init', methods=['GET'])
def initTree():
    global lib, tree  # 전역 변수 사용
    lib = init()
    tree = makeTree(lib)

    return "Build Tree Success"

@app.route('/insert', methods=['POST'])
def ins():
    global lib, tree  # 전역 변수 사용
    key = request.json.get('key')
    val = request.json.get('value')
    print(key, val)
    Insert(lib, tree, key, val)
    return f"Insert the key {key}"

@app.route('/delete', methods=['POST'])
def dele():
    global lib, tree  # 전역 변수 사용
    key = request.json.get('key')
    Delete(lib, tree, key)
    return f"Delete the key {key}"

@app.route('/traverse', methods=['GET'])
def trav():
    global lib, tree  # 전역 변수 사용
    r = Traverse(lib, tree)
    result = makeResult(r)

    print(result)

    str_result = {str(key): value for key, value in result.items()}

    print(str_result)
    return jsonify(str_result)

@app.errorhandler(404)
def page_not_found(e):
    # 404 페이지를 반환하거나 사용자 정의 404 페이지로 리디렉션
    return send_from_directory(app.static_folder, 'index.html'), 404

if __name__ == '__main__':
    app.run(debug=True,
            host=host_addr,
            port=host_port)