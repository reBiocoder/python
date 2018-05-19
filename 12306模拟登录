#12306的验证码初步突破
import  requests
from  PIL   import   Image
#提交检查请求的真实url
check_url="https://kyfw.12306.cn/passport/captcha/captcha-check"
ver_url="https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand&0.5604448691516117"
my_session=requests.session()#建立一个会话，自动保存cookie值
check_res=my_session.get(ver_url)
#将验证码保存到本地
with  open('1.jpg','wb')   as   f:
    f.write(check_res.content)
img=Image.open('1.jpg')
img.show()#将图片表示出来，用画图工具打开，然后就能看见像素
ver=input("请输入验证码>>>")#从验证码中得知的像素
#构造表单,字典类型
datas={"answer":ver,
"login_site":"E",
"rand":"sjrand"}
check_res=my_session.post(check_url,data=datas)
print(check_res.text)
#抓包分析，得到提交账号和密码的url
login_url="https://kyfw.12306.cn/passport/web/login"
username=input("请输入账号：")
password=input("请输入密码：")
data={"username":username,
"password":password,
"appid":"otn"}
login_res=my_session.post(login_url,data=data)
print(login_res.text)
