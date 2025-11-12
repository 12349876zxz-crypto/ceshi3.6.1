import requests, multiprocessing, time
from app.checkout_service import app # 假设你的 Flask 应用保存在 app/checkout_service.py 文件中

def run_server():
    app.run(port=5000) # 运行 Flask 应用在 5000 端口

def test_checkout_total():
    p = multiprocessing.Process(target=run_server) # 创建一个新进程来运行 Flask 服务
    p.start() # 启动新进程
    time.sleep(1) # 等待服务启动（给服务一点时间来初始化）

    data = {"items": [{"price": 20, "quantity": 3}]} # 准备测试数据：一个包含一个商品的购物车
    res = requests.post("http://127.0.0.1:5000/checkout", json=data) # 发送 POST 请求到微服务

    assert res.status_code == 200 # 断言 HTTP 状态码是否为 200
    assert res.json()["total"] == 60 # 断言返回的 total 是否为 60 (20 * 3)

    p.terminate() # 终止运行服务的进程，释放资源