# Computer Networking : A Top-Down Approach (7th)

#### 一点小建议:强烈推荐看完自顶向下的链路层后(物理层没有存在感hh)，去刷CS144的lab0-lab4，是实现一个miniTCP的lab，刚学完五层模型就去实现个运输层协议绝对不错，我就这样干了（资源可以在我的CS144lab的README找到），我c++入门+一定的数据结构基础+计网看了自顶向下+一点操作系统基础差不多花了60多个小时左右做完了（我把这个当成c++课设了，肝了8天，心累），强烈推荐。另外CS144视频推荐不看，因为确实CS144在YouTube的是远古视频加上感觉哈工大的计网mooc已经质量还不错了，如果需要可以看看CS144相关实验解答的视频，不过我没看。

### 【一】Socket Program: 
* [CH2 Web Server](CH2/Programing/WebServer)<br>这个简单，熟悉下api。
* [CH2 UDPping](CH2/Programing/UDPping)<br>这个简单，熟悉下api。
* [CH2 SMTP Client](CH2/Programing/SMTP)<br>网易邮箱自动成垃圾，我错了，我是垃圾，搞了半天心态，推荐用qq。
* [CH2 Web Proxy](CH2/Programing/WebProxy)<br>因为做过CSAPP的proxy lab所以原理很简单，但是给的python模板一堆坑，各种细节问题，尤其是自动发200 OK完全不考虑304 Not Modified，无语了。另外强调下要用给的网站测试，因为这是特意用的http 80端口，现在常用网站基本都是https 443端口了，哭哭，愣了半天才发觉端口不对。（可选都写在一起了，不过没有找到测试post网站）
 
 ### 【二】Wireshark Experiment: 
* [CH1 Intro](CH1/Wireshark/WiresharkLab1.md)<br>超简单，完全是wireshark入门教程。
* [CH2 HTTP](CH2/Wireshark/WiresharkLab2.md)<br>挺有意思的，也不难，不过花的时间也要接近1h。。
* [CH2 DNS](CH2/Wireshark/WiresharkLab3.md)<br>有意思，另外韩国网站整吐了，🤮，开了vpn还是nslookup超时。开了vpn用wireshark测以太网2，关了测wlan(我的笔记本)，才发现我IP跑到美国去了。。不过不影响。学了nslookup和ipconfig确实有用。
* [CH3 TCP](CH3/Wireshark/WiresharkLab4.md)<br>挺有意思，还帮我复习了下我写的miniTCP，另外wireshark好强大。。。
* [CH3 UDP](CH3/Wireshark/WiresharkLab5.md)<br>快乐复习。
* [CH4 IP](CH4/Wireshark/WiresharkLab6.md)<br>快乐复习。
* [CH4 ICMP](CH4/Wireshark/WiresharkLab7.md)<br>快乐复习。
* [CH4 DHCP](CH4/Wireshark/WiresharkLab8.md)<br>快乐复习。
* [CH4 NAT](CH4/Wireshark/WiresharkLab9.md)<br>快乐复习。
* [CH5 ARP](CH5/Wireshark/Wiresharklab10.md)<br>快乐复习。
* CH6 802.11 因为我是CS的，不是搞通信的，书上简略介绍一下对我已经完全够用，就不浪费时间了。
* [CH8 SSL](CH8/Wireshark/Wiresharklab12.md)<br>稍微看了看复习。

习题解析可以看：https://github.com/moranzcw/Computer-Networking-A-Top-Down-Approach-NOTES/blob/master/Resource/Solutions-7th-Edition.docx
