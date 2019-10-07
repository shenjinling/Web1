import re
from regions import regions

def checkIdcard(idcard):
    Errors = ['验证通过!','身份证号码位数不对!','身份证号码出生日期超出范围或含有非法字符!','身份证号码校验错误!']
    area={"11":"北京市","12":"天津市","13":"河北省","14":"山西省","15":"内蒙古自治区","21":"辽宁省","22":"吉林省","23":"黑龙江省",
    "31":"上海市","32":"江苏省","33":"浙江省","34":"安徽省","35":"福建省","36":"江西省","37":"山东省","41":"河南省","42":"湖北省",
    "43":"湖南省","44":"广东省","45":"广西壮族自治区","46":"海南省","50":"重庆市","51":"四川省","52":"贵州省","53":"云南省","54":"西藏自治区",
    "61":"陕西省","62":"甘肃省","63":"青海省","64":"宁夏回族自治区","65":"新疆维吾尔自治区","71":"台湾省","81":"香港特别行政区","82":"澳门特别行政区","91":"国外"}
    idcard=str(idcard)
    idcard=idcard.strip()
    idcard_list=list(idcard)

    if(len(idcard)==18):
        if(int(idcard[6:10]) % 4 == 0 or (int(idcard[6:10]) % 100 == 0 and int(idcard[6:10])%4 == 0 )):
            ereg=re.compile('[1-9][0-9]{5}(19|20)[0-9]{2}((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|[1-2][0-9]))[0-9]{3}[0-9Xx]$')
            #//闰年出生日期的合法性正则表达式
        else:
            ereg=re.compile('[1-9][0-9]{5}(19|20)[0-9]{2}((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|1[0-9]|2[0-8]))[0-9]{3}[0-9Xx]$')
            #//平年出生日期的合法性正则表达式
        if(re.match(ereg,idcard)):
            S = (int(idcard_list[0]) + int(idcard_list[10])) * 7 + (int(idcard_list[1]) + int(idcard_list[11])) * 9 + (int(idcard_list[2]) + int(idcard_list[12])) * 10 + (int(idcard_list[3]) + int(idcard_list[13])) * 5 + (int(idcard_list[4]) + int(idcard_list[14])) * 8 + (int(idcard_list[5]) + int(idcard_list[15])) * 4 + (int(idcard_list[6]) + int(idcard_list[16])) * 2 + int(idcard_list[7]) * 1 + int(idcard_list[8]) * 6 + int(idcard_list[9]) * 3
            Y = S % 11
            M = "F"
            JYM = "10X98765432"
            M = JYM[Y]
            if(M == idcard_list[17]):
                print(Errors[0])
                res=re.search(r'^(((?P<province>[1-9]\d)(?P<city>\d{4}))(?P<born_year>[12]\d{3})(?P<born_month>0[1-9]|1[012])(?P<born_day>0[1-9]|[12][0-9]|3[01])\d{2}(?P<gender>\d)[0-9xX])$',idcard)
                if res:
                    s=res.group(3)
                    print("出生省份：",area[s])
                    n=res.group(2)
                    if(n in regions.keys()):
                        print("出生城市: ",regions[n])
                    else:
                        print("地区非法")
                    print ("出生日期: ",res.group(5),res.group(6),res.group(7))
                    num=int(res.group(8))
                    if (num % 2==0):
                        print("性别为: 女")
                    else:
                        print("性别为: 男")
            else:
                print(Errors[3])
        else:
            print(Errors[2])
    else:
        print(Errors[1])


   #res = re.search('(?P<province>\d{2})(?P<city>\d{4})(?P<born_year>\d{4})(?P<born_month>\d{2})(?P<born_dadt>\d{2})',idcard)

    
        
