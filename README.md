# Pretend_Sign
任务11：伪造签名（假如你是中本聪）、在k泄露和k重用情况下密钥d泄露的算法复现

1、ECDSA签名生成：

![image](https://user-images.githubusercontent.com/108848022/180726584-c0f2828f-d668-4cb7-aabd-605dbd2e1b87.png)

2、ECDSA签名伪造（假如你是中本聪）：

![image](https://user-images.githubusercontent.com/108848022/180726650-415ae4d8-5737-4fc3-b03e-045b0b6f375b.png)

3、k泄露和k重用会导致反解出密钥d：

![image](https://user-images.githubusercontent.com/108848022/180726746-a3fe8b7b-43e4-4b00-a3c6-e38e8ef1eb29.png)

4、打印结果输出：

![image](https://user-images.githubusercontent.com/108848022/180726833-4f1e57d3-70e9-41ec-88d6-87400d41b993.png)

5、注意：在原py文件中，并不包含与输出结果有关的语句，如果需要重新验证，请将new.py中的语句添加到原python文件中再进行调试。
