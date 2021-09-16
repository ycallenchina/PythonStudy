import pandas as pd
import numpy as np

def 回测(df_ch2,df):
    
    # 设置策略 预盈利价格,止损价格
    df_ch2['止损位']=df_ch2['low']
    df_ch2['预盈位']=df_ch2['close']*(1+df_ch2['pct_change']*2*0.01)
    
    #初始化:
    CD_date=pd.to_datetime('1900-01-01')

    # 回测
    for index,row in df_ch2.iterrows():
        
        #初始化
        into_time=df.iloc[index+1,9] #买入时间,时机的下个五分钟
        into_price=df.iloc[index+1,3] #买入价格,时机的下个五分钟开盘价
        
        deal_during=0
        deal_max=5   #可设置,持股时间(按交易日天算)
        CD_time=0
        
        start_index=index
        start=1
        count=0
        
        #进场前判断
        
        #判断收盘14:49后的时机不进场
        if (row['时间'].hour==14 and row['时间'].minute>49) or row['时间'].hour==15:
            df_ch2.loc[start_index,'盈亏']='未入场'
            df_ch2.loc[start_index,'卖出时间']='未入场'
            df_ch2.loc[start_index,'卖出价']='未入场'
            df_ch2.loc[start_index,'买入价']='未入场'
            df_ch2.loc[start_index,'买入时间']='未入场'
            start=0
            pass
        
        #判断是否在休眠期
        if (row['时间']-CD_date).days<0:
            df_ch2.loc[start_index,'盈亏']='未入场'
            df_ch2.loc[start_index,'卖出时间']='未入场'
            df_ch2.loc[start_index,'卖出价']='未入场'
            df_ch2.loc[start_index,'买入价']='未入场'
            df_ch2.loc[start_index,'买入时间']='未入场'
            start=0
            pass
        
        #进场模拟开始,遍历进场后所有行情
        while start==1:
            index+=1
            count+=1
            
            open1=df.iloc[index,3]
            close=df.iloc[index,4]
            high=df.iloc[index,7]
            low=df.iloc[index,8]
            time1=df.iloc[index,9]
            
            #过滤掉进场当日的记录,因为交易为T+1
            if (df.iloc[index,9]-row['时间']).total_seconds()>66600: 
                #66600换算成秒为18.5小时,刚好是收盘时间到第二天开盘的最短时间
                
                #盈利判断 
                #open位大于预盈时:
                if row['预盈位']<=open1:
                    df_ch2.loc[start_index,'盈亏']=round((open1-into_price)/into_price*100,2)
                    df_ch2.loc[start_index,'卖出时间']=df.iloc[index,9]
                    df_ch2.loc[start_index,'卖出价']=round(row['预盈位'],2)
                    df_ch2.loc[start_index,'买入价']=into_price
                    df_ch2.loc[start_index,'买入时间']=into_time
        #             print(row['预盈位'],df.iloc[index,7])
                    start=0
                
                    #进入休眠日期的计算 :卖出时间+需要休眠的天数
                    CD_date=df.iloc[index+(CD_time)*48,9]
                    print('休眠期的计算',df.iloc[index,9],CD_date)
                    
                #open位大于预盈时:
                elif row['预盈位']<=high:
                    df_ch2.loc[start_index,'盈亏']=round(row['pct_change']*2,2)
                    df_ch2.loc[start_index,'卖出时间']=df.iloc[index,9]
                    df_ch2.loc[start_index,'卖出价']=round(row['预盈位'],2)
                    df_ch2.loc[start_index,'买入价']=into_price
                    df_ch2.loc[start_index,'买入时间']=into_time
        #             print(row['预盈位'],df.iloc[index,7])
                    start=0

                    #进入休眠日期的计算 :卖出时间+需要休眠的天数
                    CD_date=df.iloc[index+(CD_time)*48,9]
                    print('休眠期的计算',df.iloc[index,9],CD_date)
                    
                elif row['止损位']>=open1:
                    df_ch2.loc[start_index,'盈亏']=round((open1-into_price)/into_price*100,2)
                    df_ch2.loc[start_index,'卖出时间']=df.iloc[index,9]
                    df_ch2.loc[start_index,'卖出价']=round(open1,2)
        #             print(row['止损位'],df.iloc[index,8])
                    
                    df_ch2.loc[start_index,'买入价']=into_price
                    df_ch2.loc[start_index,'买入时间']=into_time
                    

                #止损判断
                elif row['止损位']>=low:
                    df_ch2.loc[start_index,'盈亏']=round((row['止损位']-into_price)/into_price*100,2)
                    df_ch2.loc[start_index,'卖出时间']=df.iloc[index,9]
                    df_ch2.loc[start_index,'卖出价']=round(row['止损位'],2)
        #             print(row['止损位'],df.iloc[index,8])
                    
                    df_ch2.loc[start_index,'买入价']=into_price
                    df_ch2.loc[start_index,'买入时间']=into_time
                    start=0

                #进场日计算 and 手持超5日出场
                elif df.iloc[index,9].hour==15 and df.iloc[index,9].minute==0:
                    deal_during+=1
                    if deal_during>deal_max:
                        df_ch2.loc[start_index,'盈亏']=round((df.iloc[index,3]-into_price)/into_price*100,2)
                        df_ch2.loc[start_index,'卖出时间']=df.iloc[index,9]
                        df_ch2.loc[start_index,'卖出价']=df.iloc[index,3]
                        df_ch2.loc[start_index,'买入价']=into_price
                        df_ch2.loc[start_index,'买入时间']=into_time
                        start=0

                
            
    return df_ch2

 def 回测7日峰值(df,df_all):
    
    for index,row in df.iterrows():
        
        峰值日=7
        峰值日期=df_all.iloc[index+(峰值日*48),9]
        start=1
        max_values=0
        start_index=index
        
        while start==1:
            index+=1
            if (峰值日期-df_all.iloc[index,9]).total_seconds()>0:
                if max_values<df_all.iloc[index,7]:
                    max_values=df_all.iloc[index,7]
            else:
                df.loc[start_index,'7日峰值']=round(max_values,2)
                start=0
    return df

if __name__ == '__main__':
    pd.set_option('display.max_columns',None )
    import df股票数据处理 as 处理
    import df寻求时机 
    df=处理.获取csv数据()
    处理.时间格式处理(df)
    df_all=df.copy()
    df=df寻求时机.时机(df)

    # print(df_all.columns)

    print(回测(df,df_all))