from urllib import request

# 使用代理proxy，使用ProxyHandler构建一个handler
handler = request.ProxyHandler({'http': '27.155.84.233:8081'})
# 使用build_opener构建一个opener
opener = request.build_opener(handler)
# 使用opener发送一个请求
req = request.Request("http://httpbin.org/ip")
resp = opener.open(req)
print(resp.read())
