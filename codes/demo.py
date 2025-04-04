import requests

url="http://172.16.3.19/eportal/InterFace.do?method=login"

data={
	"userId":"210106109",
	"password":"3a13ac035f222c0c2b89b7d4e9bfcf094180f3257464d2a912949f8efe62a68461da12d2f3b406eb7cd82bf940942ecb8ec7b0f06c2b3ed8916bb947489b4c0740a899edde1b9f551cd45dedf86e8da73e49ac22287c9ed4ddbe3ac8f9ddf876aeedba70404348ea58b5ae3073be27c00aba3cafe4c6b27c6054a8276678dd97",
	"service":"yidong",
	"queryString":"wlanacname%3DSuShe-HeXin%26wlanuserip%3D10.16.151.72%26wlanparameter%3Dc87f540b22d8%26nasip%3D172.16.10.252",
	"operatorPwd":"",
	"operatorUserId":"",
	"validcode":"",
	"passwordEncrypt":"true"
}

header={
	"Accept":"*/*",
	"Accept-Encoding":"gzip, deflate",
	"Accept-Language":"en-GB,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
	"Connection":"keep-alive",
	"Content-Length":"492",
	"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
	"Cookie":"EPORTAL_COOKIE_DOMAIN=true; EPORTAL_COOKIE_USERNAME=210106109; EPORTAL_COOKIE_OPERATORPWD=; EPORTAL_COOKIE_SAVEPASSWORD=true; EPORTAL_COOKIE_PASSWORD=3a13ac035f222c0c2b89b7d4e9bfcf094180f3257464d2a912949f8efe62a68461da12d2f3b406eb7cd82bf940942ecb8ec7b0f06c2b3ed8916bb947489b4c0740a899edde1b9f551cd45dedf86e8da73e49ac22287c9ed4ddbe3ac8f9ddf876aeedba70404348ea58b5ae3073be27c00aba3cafe4c6b27c6054a8276678dd97; EPORTAL_AUTO_LAND=; EPORTAL_COOKIE_SERVER=yidong; EPORTAL_COOKIE_SERVER_NAME=%E4%B8%AD%E5%9B%BD%E7%A7%BB%E5%8A%A8; EPORTAL_USER_GROUP=%E5%AD%A6%E7%94%9F; JSESSIONID=0531213A0CF77E73CDF127AF4849C155",
	"Host":"172.16.3.19",
	"Origin":"http://172.16.3.19",
	"Referer":"http://172.16.3.19/eportal/index.jsp?wlanacname=SuShe-HeXin&wlanuserip=10.16.151.72&wlanparameter=c87f540b22d8&nasip=172.16.10.252",
	"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.46"
}

dd=requests.post(url,data=data,headers=header)

print(dd.text)
