import easyquotation
import time

def get_stock(name):
    
    try:
        quotation = easyquotation.use('sina')
        tmp_dict = quotation.market_snapshot(prefix=False)

        code=str(name)

        name=tmp_dict[code]['name']
        price=str(tmp_dict[code]['now'])
        now='时间:'+str(time.strftime("%m-%d %H:%M:%S", time.localtime()))
        message=name+'  '+price+'   '+now

        return message

    except:
        message='股票代码输入有误'
        return message

if __name__ == '__main__':
    pass
    # print(get_stock(3002244))