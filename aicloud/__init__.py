import os
import http.client, urllib.parse
import json
import requests


name = "aicloud"

__cloudUrl = ''
__isInCloud=False
__token=''
__bucket=''

def __getAccess():
    headers2 = {'Content-type': 'application/json',"Authorization": "Bearer " + __token}
    res = requests.get(__cloudUrl + "/v1/access", headers=headers2)
    if res.status_code != 200:
        print(res.status_code, res.reason, res.text)
        return
    # os.environ[''] = res.text
    access = json.loads(res.text)
    os.environ["AWS_ACCESS_KEY_ID"]=access['AccessKeyid']
    os.environ["AWS_SECRET_ACCESS_KEY"]=access['SecretaccessKey']
    os.environ["AWS_REGION"]="us-east-1" 
    os.environ["S3_REGION"]="us-east-1" 
    os.environ["S3_USE_HTTPS"]=access['Secure']
    os.environ["S3_VERIFY_SSL"]=access['Secure']
    os.environ["S3_ENDPOINT"]=access['SvcAdress']
    global __bucket
    __bucket = access['MyBucket']



def modelName(name):
    '''
    传入model名，返回在云上保存的模型名，如果在云外部调用，原值返回
    '''
    if __isInCloud == False:
        return name
    tmp=name.split('/')
    ret = os.path.join(__bucket,'models',tmp[-1])
    return 's3://'+ret


def __init__():
    global __cloudUrl
    global __isInCloud
    global __token
    __isInCloud='AICLOUD' in os.environ
    if __isInCloud == False:
        return

    __cloudUrl=os.environ['AICLOUD']

    if 'CLOUD_TOKEN' in os.environ:
        __token=os.environ['CLOUD_TOKEN']
    else:
        raise Exception('没有获取到有效token')
    __getAccess()
        

# 测试用的函数
def login():
    os.environ['AICLOUD']='http://localhost:8080'
    # 登录
    params = {'username': 'abcd', 'password': '123123'}
    json_foo = json.dumps(params)
    headers = {'Content-type': 'application/json'}
    url=os.environ['AICLOUD']
    res = requests.post(url + "/auth", data=json_foo, headers=headers)
    if res.status_code != 200:
        print(res.status_code, res.reason, res.text)
        return
    print("登录ok")
    data = res.text
    # print(data)
    token = json.loads(data)
    print(token['token'])
    os.environ['CLOUD_TOKEN']=token['token']
    return

if __name__=='__main__':
    login()
    __init__()
    a=modelName("abc/ab")
    print(a)
else:
    __init__()