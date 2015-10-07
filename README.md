# smartcar
1)效果：http://v.youku.com/v_show/id_XMTI4MTk5MjAzMg==.html?firsttime=3&from=y1.4-2
2)小车用pcduino做TCPserver，安卓做TCP client
3)小车和安卓连在同一个wifi下（可以用安卓作热点）
4）小车连上wifi后就自动UDP广播到22345端口告诉安卓自己的地址（因为连接wifi时IP地址有时是自动分配的）
5）安卓端收到UDP广播后记下小车IP地址，然后根据倾度传感器的角度进行判断，发送前后左右指令给小车
6）小车收到前后左右指令后输出控制IO口，IO口通过L298电机驱动轮子
