#python3调用TencentAI接口签名算法
# - * - coding:utf-8 - * -
import hashlib
import time
import random
from urllib import parse
import base64,requests
info = {
    "ID":"1106960784",
    "KEY":"lelHKW1sC9bZ5DGA"
}
def getTimestamp():
    '''
    返回秒级时间戳
    '''
    t = time.time()
    return int(t)
def getMD5(strings):
    my_Md5 = hashlib.md5()
    my_Md5.update(strings.encode("utf-8"))
    secure = my_Md5.hexdigest()
    #print (secure)
    return secure
def parser(paramsDic):
    params = sorted(paramsDic.items())
    data = parse.urlencode(params).encode("utf-8")
    return data
def imgProcessing(imgPathstr):
    '''
    :param imgPathstr:图片路径
    :return: 图片base64编码
    '''
    f = open(imgPathstr, "rb")
    ls_f = base64.b64encode(f.read())
    ls_f = str(ls_f,encoding = "utf-8")
    f.close()
    return ls_f
def getReqSign(paramsDic, AppKey):
    '''
    签名有效期5分钟
    :param paramsDic: 参数字典
    :param AppKey: APPKey
    :return:
    '''
    params = sorted(paramsDic.items())
    url_data = parse.urlencode(params)
    url_data = url_data + "&" + "app_key" + "=" + str(info["KEY"])
    url_data = getMD5(url_data).upper()
    return  url_data
#if __name__=="__main__":
def  OCR_url(pic_loc):
    url="https://api.ai.qq.com/fcgi-bin/ocr/ocr_generalocr"
    reqDic = {
        "app_id": int(info["ID"]),
        "image": imgProcessing(pic_loc),
        "nonce_str": int(getTimestamp()),#getNonce_str(),
        "time_stamp": int(getTimestamp()),
    }
    reqDic["sign"] = getReqSign(reqDic, info["KEY"])
    req = requests.post(url, reqDic)
    if req.json()["msg"] =="ok":
        return(req.json()["data"]["item_list"][0]["itemstring"])
    if  req.json()["msg"]!="ok":
        return  u"验证码识别有误"
