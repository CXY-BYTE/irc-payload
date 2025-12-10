# 利用IRC批量控制肉鸡进行ddos

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

![屏幕截图 2025-12-03 163743](C:\Users\hp\Pictures\Screenshots\屏幕截图 2025-12-03 163743.png)

/join #bot

## 脚本

上传代码至受害机

## 攻击流程及实验结果

在hexchat上输入!ddos ip port speed

!stop停止攻击

![image-20251202155732002](C:\Users\hp\AppData\Roaming\Typora\typora-user-images\image-20251202155732002.png)

命令执行

![屏幕截图 2025-12-03 163545](C:\Users\hp\Pictures\Screenshots\屏幕截图 2025-12-03 163545.png)

在攻击机上

```
 tcpdump -i any 'udp port 5001' -n#ddos流量
```



![image-20251202154017607](C:\Users\hp\AppData\Roaming\Typora\typora-user-images\image-20251202154017607.png)
