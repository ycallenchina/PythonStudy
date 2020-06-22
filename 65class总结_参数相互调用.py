
import random
import time

#实验
# for i in range(10):
# 	q=[1,2,3,4]
# 	print(random.randint(1,10))	
# 	print(random.sample(range(len(q)),2))
# 	time.sleep(1)

class role:
	def __init__(self,name,powr,blood):#基本战斗属性,名,攻击力,血量
		self.name=name
		self.powr=powr
		self.blood=blood

	

	def atack(self,enermy):#攻击内容,谁攻击了谁,并执行受伤动作
		print(f'{self.name}开始攻击{enermy.name}')
		enermy.hurt(self.powr)

	def hurt(self,powr):#受伤动作:受攻击人血量减少,并打印剩余血量
		self.blood -= powr
		print(f'{self.name},受到了{powr}点伤害.剩余{self.blood}点血')

	def die(self):#死亡动作:告诉别人我已88
		print(f'imsorry,{self.name},i have to die!------------------------------{self.name},is die!')


class player(role):#特殊角色设计,继承了role的属性和受伤,死亡方法,但有自己独特的攻击方法1,疯狂,2普通.
    def atack(self, enermy):

        print(f'{self.name}开始攻击{enermy.name}')
        choose = int(input('做出你的选择:疯狂1 or 普通2:'))

        if choose == 1:#疯狂的攻击,随机0-3倍的攻击量,并自身消耗3点血量
            print(f'{self.name}开始攻击{enermy.name}')
            enermy.hurt(random.randint(0, 3) * self.powr)
            self.blood -= 3
        elif choose == 2:#普通攻击,常规攻击
            print(f'{self.name}开始攻击{enermy.name}')
            enermy.hurt(self.powr)
        else:#特殊情况,输入错误将惩罚丢失本轮攻击.
            print('this time is over!')


#4位选手,player选手是特殊选手.
all=[role('eff',5,100),role('allen',10,50),role('周星星',7,48),player('me',8,100)]

#随机选择2位选手进行攻击.死亡的选手将被移除.最终剩余一位的选手胜出.
while len(all)>1:
	lucky=random.sample(all,2)#随机选出2名选手
	r1=lucky[0]
	r2=lucky[1]

	r1.atack(r2)#随机战斗回合

	if r2.blood<1:#判断死亡,移除死亡者
		r2.die()
		all.remove(r2)
		
	time.sleep(1)#停顿1秒

print(lucky[0].name,'is winner!')#打印出胜出人

