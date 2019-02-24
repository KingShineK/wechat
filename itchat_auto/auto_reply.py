import itchat
import requests
import time
import random
from itchat.content import *
from itchat.content import TEXT,PICTURE,VIDEO,RECORDING,SHARING

# 用于记录回复过的好友
replied = []

# 获取新年祝福语
# def GetRandomGreeting():
#     res = requests.get("http://www.xjihe.com/api/life/greetings?festival=新年&page=10", headers = {'apiKey':'1gF482NU0bzIPRzwveIiPQ2uMokM8YZf'})
#     results = res.json()['result']
#     print(results)
#     return results[random.randrange(len(results))]['words']
# 获取新年祝福语
def GetRandomGreeting():
    results=['除夕到，放鞭炮，家家户户好热闹；舞龙灯，踩高跷，合家欢乐步步高！眼看大年初一快来到，人人开心齐欢笑，提前祝你春节好，猪年祝福我最早！',
             '猪年到喜迎门，送欢乐送祝福，愿您新春欢乐，万事如意，阖家欢乐，百事顺心，吉星高照，添福添寿，幸福美满，快乐一生！',
             '微信来拜年，祝福要提前。送走金狗迎祥猪，新年接旧年。新年新气象，喜事成双全。金猪叩门携好运，日子蜜蜜甜。',
             '点点幸运星，株株幸运草，朵朵幸福花，片片快活林，道道平安符，把把长命锁，颗颗平安豆，粒粒健康米，只只吉祥猪，依依祝福情。预祝猪年春节快乐！',
             '猪年新春到，心情无限妙；快乐把门敲，喜庆身边绕；吉祥跟你跑，幸福对你笑；健康来拥抱，愿你身体好；新的一年，愿你生活美满，幸福逍遥！',
             '谷丰登闹新春，家家户户福相伴，和气美满团圆年，红红春联写美满，文字里面情飞扬，款款祝福送予君，春节愉快合家欢，幸福美满万年长，春节快乐！',
             '新年问声好，祝福要趁早：愿您年轻永不老，薪水月月攀新高，生活每天有欢笑，佳人相伴夕与朝，朋友增多不减少，猪年好运把你找。',
             '走过的是狗年，驱走的是霉运；到来的是猪年，期待的是美好；流逝的是光阴，换回的是记忆；送去的是祝福，留下的是：猪年家和万事兴！',
             '猪年好，猪年妙，猪年的歌声满天飘；猪年烂，猪年暖，猪年的幸福享不完；猪年旺，猪年香，猪年的祝福分外长。愿你猪年心飞扬，万事皆顺畅！',
             '先到身旁，心意情意都献上，愿您接纳永收藏，愿您事业财源广，愿您暖和体安康，愿您烦恼忧愁散，愿您春节安康！',
             '过去一年走过的脚步，留下的是艰辛和攀登的苦，未来一年里展望的路，你我仍需带着更高的理想继续付出。从现在做起迈出勇敢和坚定，祝新的一年里有更大的进步。',
             '除夕夜喧腾，祝福表深情。祝福的短信比爆竹多，祝福的声音比爆竹响，祝福的心意比爆竹震，祝福的时候比爆竹早。除夕快乐。',
             '幸福的锣鼓敲开致富门，快乐的鞭炮引来吉祥路。大红的灯笼照亮光明途，缤纷的烟花献出如意宝。除夕钟声响起时，欢歌笑语声围绕。全家团聚守岁末，美好生活每一天。除夕快乐！',
             '除夕大年将来临，好运滚滚向你行；爆竹声声响翻天，快乐欢庆喜连绵；短信祝福来不断，愿你事事顺心愿。朋友，祝你除夕佳节，快乐不间断，喜笑又开颜！',
             '迎来幸运的门神，贴上喜庆的春联，挂上喜祥的年画，点燃好运的灯笼；除夕到了，祝你幸运迎来幸福，喜庆带来美好，吉祥送来安康，好运得来辉煌！',
             '除夕佳节喜气绕，团圆欢乐真热闹；抒写对联放鞭炮，大红灯笼福字倒；新衣新裤新气象，说声祝福大声笑；祝愿朋友心情悦，阖家团圆乐逍遥。除夕快乐！',
             '又是除夕来到，幸福锐不可当；欢声笑语不断，欢聚一堂热闹；烦恼忧伤全抛，甜蜜好运常抱；福运安康顺畅，健康快乐到老。祝除夕幸福享团圆。',
             '提个前，赶个早，先来道声除夕好；撞好运，遇好事，道个吉祥和如意。祝你新年拥有新气象，春天拥有春的希望，幸运之星照又照，生活快乐又美妙！',
             '祝你一帆风顺，二龙腾飞，三羊开泰，四季平安，五福临门，六六大顺，七星高照，八方来财，九九同心，十全十美。',
             '向你拜大年！祝你身体健康，心情越来越好，人越来越漂亮！生活越来越浪漫！新春快乐！',
             '一年一年开心过，开开心心，一生快快乐乐，一世平平安安，一家和和睦睦，愿你生命中的每一个愿望全能得到实现！']
    return results[random.randrange(len(results))]

# 发送新年祝福语
def SendGreeting(msg):
    global replied
    # 获取发送者的信息
    friend = itchat.search_friends(userName=msg['FromUserName'])
    # 回复时优先使用备注姓名，其次是昵称
    if friend['RemarkName']:
        itchat.send((friend['RemarkName']+'，'+GetRandomGreeting()+'王辉在此给你拜年了~'), msg['FromUserName'])
    else:
        itchat.send((friend['NickName']+'，'+GetRandomGreeting()+'王辉在此给你拜年了~'), msg['FromUserName'])
    # replied.append(msg['FromUserName'])

# 文本消息，如果发送语中含有“年”or“猪”，表示该消息为新年祝福
# and msg['FromUserName'] not in replied
@itchat.msg_register(TEXT)
def text_reply(msg):
    if ('年' in msg['Text'] or '猪' in msg['Text'] or '除夕' in msg['Text'] or '春' in msg['Text'] or '节' in msg['Text']or '2019' in msg['Text']or '祝' in msg['Text']) :

        SendGreeting(msg)

# 其他消息，直接回复新年祝福
@itchat.msg_register([PICTURE, RECORDING, VIDEO, SHARING])
def others_reply(msg):
    if msg['FromUserName'] not in replied:
        SendGreeting(msg)

if __name__ == '__main__':

	print("开始运行程序。。。")
	itchat.auto_login()

	itchat.run()