from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/checkout", methods=["POST"])
def checkout():
    data = request.get_json()  # 从请求体中获取 JSON 数据
    items = data.get("items", [])  # 从 JSON 数据中获取 "items" 列表，如果不存在则默认为空列表
    if not items:
        return jsonify({"error": "empty cart"}), 400  # 如果购物车为空，返回错误信息和 400 状态码

    total = sum(i["price"] * i["quantity"] for i in items) # 计算商品总价：遍历 items 列表，将每个商品的 price * quantity 累加
    return jsonify({"total": total, "status": "ok"}), 200 # 返回总价和成功状态，以及 200 状态码