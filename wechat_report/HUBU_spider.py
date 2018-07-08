import  TenCent_SDK  as  TS
import  requests
import  yagmail
import  json
import  pandas  as  pd
import  numpy  as  np
from  lxml  import  etree
import  time
def func():
    my_sessoin=requests.session()
    url="http://jwxt.hubu.edu.cn/Logon.do?method=logon"
    encode_url="http://jwxt.hubu.edu.cn/Logon.do?method=logon&flag=sess"
    verification_code="http://jwxt.hubu.edu.cn/verifycode.servlet"
    res=my_sessoin.get(url)
    #获取验证码
    code_res=my_sessoin.get(verification_code)
    with   open(r"C:\Users\13016\Desktop\2.jpg",'wb')   as   f:
        f.write(code_res.content)
    loc=r"C:\Users\13016\Desktop\2.jpg"
    #TenCent_SDK
    verifycode=TS.OCR_url(loc)
    print(verifycode)
    #换位加密算法
    encode_res=my_sessoin.get(encode_url)
    datastr=encode_res.text
    scode=datastr.split("#")[0]
    sxh=datastr.split("#")[1]
    code="201622110710137"+"%%%"+"ZPaixzh1314"
    encoded=""
    i=0
    while(i<len(code)):
        if(i<20):
            encoded=encoded+code[i:i+1]+scode[0:int(sxh[i:i+1])]
            scode=scode[int(sxh[i:i+1]):len(scode)]
            i=i+1
        else:
            encoded=encoded+code[i:len(code)]
            i=len(code)
            i=i+1
    #构造表单
    datas={"USERNAME":"201622110710137",
    "PASSWORD":"ZPaixzh1314",
    "useDogCode":"",
    "useDogCode":"",
    "encoded":encoded,
    "RANDOMCODE":verifycode}
    ver_res=my_sessoin.post(url,data=datas)
    main_url="http://jwxt.hubu.edu.cn/framework/main.jsp"
    main_res=my_sessoin.get(main_url)
    #零级
    header={"Referer":"http://jwxt.hubu.edu.cn/framework/main.jsp"}
    datas={}
    zero_url="http://jwxt.hubu.edu.cn/Logon.do?method=logonBySSO"
    zero_res=my_sessoin.post(zero_url,data=datas,headers=header)
    #一级菜单
    header={"Referer":"http://jwxt.hubu.edu.cn/framework/main.jsp"}
    first_url="http://jwxt.hubu.edu.cn/framework/new_window.jsp?lianjie=&winid=win1"
    first_res=my_sessoin.get(first_url,headers=header)
    #二级菜单
    header={"Accept":"image/gif, image/jpeg, image/pjpeg, application/x-ms-application, application/xaml+xml, application/x-ms-xbap, */*",
    "Referer":"http://jwxt.hubu.edu.cn/framework/new_window.jsp?lianjie=&winid=win1",
    "Accept-Language":"zh-CN",
    "User-Agent":"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; LCTE)",
    "Accept-Encoding":"gzip, deflate",
    "Host":"jwxt.hubu.edu.cn",
    "Connection":"Keep-Alive"
    }
    timestamp=int(time.time())*1000
    second_url="http://jwxt.hubu.edu.cn/jiaowu/cjgl/xszq/query_xscj.jsp?tktime={}".format(timestamp)
    second_res=my_sessoin.get(second_url,headers=header)
    #三级提交表单
    third_url="http://jwxt.hubu.edu.cn/xszqcjglAction.do?method=queryxscj"
    data={"kksj":"2017-2018-2",
          "kcxz":"",
         "kcmc":"",
         "xsfs":"qbcj",
          "ok":""}
    header={"Referer":"http://jwxt.hubu.edu.cn/jiaowu/cjgl/xszq/query_xscj.jsp?tktime=1528474029000"}
    third_res=my_sessoin.post(third_url,data=data,headers=header)
    #----------------至此，教务系统成绩页面爬取成功！---------------
    #数据清洗
    html = third_res.content.decode("utf-8")
    selector=etree.HTML(html)
    content = selector.xpath('//*[@id="mxh"]/tr/td/text()')
    each_content=[content[i:i+15] for i  in  range(0,int(len(content)+1),14)]
    return  each_content
#这里设置一个循环，便于验证码识别出错时，再次循环
useful_data=func()
while  str(useful_data)=="[[]]":
    useful_data=func()
df=pd.DataFrame(useful_data,columns=("序号","学号","姓名","开课时间","科目","成绩","成绩标志","课程性质","课程类别","辅修课程","学时","学分","考试性质","补重学期","序号"))
df.to_excel(r"C:\Users\13016\Desktop\1.xlsx")
print(df)
"""for  each   in  each_content:
    print(each)"""
#-----------------------发送邮件------------------
#msg_from="1301646236@qq.com"
#password="ncrvazjkvxfwggjh"
#yag=yagmail.SMTP(msg_from,password,"smtp.qq.com","465")
#yag.send("1072524648@qq.com","本学期成绩单",contents=["见附件",r"C:\Users\13016\Desktop\1.xlsx"])


vxnz


