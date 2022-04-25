# 依赖环境:pip install -i https://mirrors.tencent.com/pypi/simple/ --upgrade tencentcloud-sdk-python
# 注意:单词发送100w条,针对每个手机号30秒只能发一次,且每天只能发10次.

import json
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.sms.v20210111 import sms_client, models
try:
    # API密匙管理 中的SecretID 和secretKey 需要到腾讯云启动
    cred = credential.Credential("AKIDmNima6ML2SbT3MOAfusa1A2e05uSjjSt", "C7l8F5evvf8KFtGMBk23nGSN1OUJr88r")
    httpProfile = HttpProfile()
    httpProfile.endpoint = "sms.tencentcloudapi.com"

    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    # 'ap-guangzhou'为腾讯服务器端参数,还有'ap-nanjing'可选
    client = sms_client.SmsClient(cred, "ap-guangzhou", clientProfile)

    req = models.SendSmsRequest()
    params = {
        "PhoneNumberSet": [ "+8618680241848" ],# 发送号码
        "SmsSdkAppId": "1400630400",# 短信默认应用SKD的ID
        "SignName": "突破学习个人网",#短信内容:标题
        "TemplateId": "1300195",#短信内容模板id
        "TemplateParamSet": [ "520520", "2" ]#短信内容模板的参数,注意,第一个是验证码(数字,最大长度6位),第二个是分钟限时
    }
    req.from_json_string(json.dumps(params))

    resp = client.SendSms(req)
    print(resp.to_json_string())

except TencentCloudSDKException as err:
    print('发送失败,错误是:',err)