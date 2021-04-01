感想:吐槽一下我的wireshark一开始经常出现TCP Previous segment not captured的问题，就是wireshark没能捕获到全部tcp段，多试几次就好了。另外看到1460这个TCP segment的length的时候感到真的有一种整洁的美的感觉。。。
---
Answer:
1. 均使用HTTP/1.1
2. zh-CN,zh
3. my 26.26.26.1, server's 128.119.245.12
4. 200 OK
5. Wed, 31 Mar 2021 05:59:01 GMT
6. 540B
7. 都有
---
8. 没有
9. 返回了，看响应体有html的内容
10. 看到了 If-Modified-Since: Wed, 31 Mar 2021 05:59:01 GMT\r\n， 一个时间用于判断服务器是否更新，如果没有更新就使用cache内容
11. HTTP/1.1 304 Not Modified\r\n
---
12. 1个GET，4个TCP分组都有
13. 第一个
14. 200 OK
15. 四个
---
16. 3个，178.79.137.164和128.119.245.12
17. 并行，浏览器支持同时开始多个tcp连接来提高并行性(因为HTTP/1.1所以1个TCP1个HTTP请求，而不是单个TCP但HTTP/2.0同时多个请求并发)，另外HTTP1.1的keep-alive与并不并行无关，指的是复用，比如并发多个http请求，每个请求都是keep-alive这样的。
---
18. 401 Unauthorized
19. Authorization: Basic d2lyZXNoYXJrLXN0dWRlbnRzOm5ldHdvcms=(wireshark-students:network的Base64编码(不是加密))
