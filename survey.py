import   requests
import  time
import  re
from  urllib  import  parse
import  random
#获取随机值
while  1:
    my_session=requests.session()
    header={"referer":"https://www.wjx.cn/jq/25877509.aspx",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}
    url="https://www.wjx.cn/jq/25877509.aspx"
    res=my_session.get(url,headers=header,verify=False)
    r=re.findall(r'starttime="(.*?)";',res.text)
    r1=re.findall(r'rndnum="(.*?)";',res.text)
    r1=r1[0]
    t=round(time.time()*1000)
    verify_url="https://www.wjx.cn/wjx/join/AntiSpamImageGen.aspx?q=25877509&t="+str(t)
    ver_res=my_session.get(verify_url,verify=False)
    with   open(r"C:\Users\13016\Desktop\2.jpg", 'wb')   as   f:
        f.write(ver_res.content)
    loc=r"C:\Users\13016\Desktop\2.jpg"
        #TenCent_SDK
    verifycode=input("验证码：")
    data1={"submittype": "1",
    "curID":"25877509",
    "t":round(time.time()*1000),
    "starttime":str(r[0]),
    "validate_text":str(verifycode),
    "rn":"1896873867"}
    print(r[0])
    print(r1)
    rc=parse.urlencode(data1).replace("+","%20")
    url1="https://www.wjx.cn/joinnew/processjq.ashx?"+str(rc)
    print(url1)
    #构造表单
    ch1=random.randint(1,4)
    ch2=random.randint(1,4)
    ch3=random.randint(1,4)
    ch4=random.randint(1,4)
    ch5=random.randint(1,4)
    ch6=random.randint(1,4)
    ch7=random.randint(1,4)
    ch8=random.randint(1,4)
    ch9=random.randint(1,4)
    ch10=random.randint(1,4)
    ch11=random.randint(1,4)
    ch12=random.randint(1,4)
    data2={"submitdata":"1$"+str(ch1)+"}2$"+str(ch2)+"}3$"+str(ch3)+"}4$"+str(ch4)+"}5$"+str(ch5)+"}6$"+str(ch6)+"}7$"+str(ch7)+"}8$"+str(ch8)+"}9$"+str(ch9)+"}10$"+str(ch10)+"}11$"+str(ch11)+"}12$"+str(ch12)+"}13$网约车需要改进"}
    print(data2)
    res1=my_session.post(url1,data=data2,headers=header,verify=False)
    print(res1.text)

