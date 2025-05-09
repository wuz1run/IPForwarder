# server.py
from flask import Flask, request

app = Flask(__name__)

# 存储最新的IP
current_ip = ""

# 更新IP接口
@app.route("/update", methods=["POST"])
def update_ip():
    global current_ip
    ip = request.form.get("ip")
    if ip:
        current_ip = ip
        return "IP Updated", 200
    return "Invalid IP", 400

# 获取当前IP接口
@app.route("/get", methods=["GET"])
def get_ip():
    if current_ip:
        return current_ip
    return "No IP set", 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  # 启动服务器，监听5000端口
