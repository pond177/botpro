print ("""

  ▄████ █    ██ ▄████▄  ▄████▄  ██▓    ▄▄▄▄   ▒█████ ▄▄▄█████▓    ██▓███  ██▀███  ▒█████
 ██▒ ▀█▒██  ▓██▒██▀ ▀█ ▒██▀ ▀█ ▓██▒   ▓█████▄▒██▒  ██▓  ██▒ ▓▒   ▓██░  ██▓██ ▒ ██▒██▒  ██▒
▒██░▄▄▄▓██  ▒██▒▓█    ▄▒▓█    ▄▒██▒   ▒██▒ ▄█▒██░  ██▒ ▓██░ ▒░   ▓██░ ██▓▓██ ░▄█ ▒██░  ██▒
░▓█  ██▓▓█  ░██▒▓▓▄ ▄██▒▓▓▄ ▄██░██░   ▒██░█▀ ▒██   ██░ ▓██▓ ░    ▒██▄█▓▒ ▒██▀▀█▄ ▒██   ██░
░▒▓███▀▒▒█████▓▒ ▓███▀ ▒ ▓███▀ ░██░   ░▓█  ▀█░ ████▓▒░ ▒██▒ ░    ▒██▒ ░  ░██▓ ▒██░ ████▓▒░
 ░▒   ▒░▒▓▒ ▒ ▒░ ░▒ ▒  ░ ░▒ ▒  ░▓     ░▒▓███▀░ ▒░▒░▒░  ▒ ░░      ▒▓▒░ ░  ░ ▒▓ ░▒▓░ ▒░▒░▒░
  ░   ░░░▒░ ░ ░  ░  ▒    ░  ▒   ▒ ░   ▒░▒   ░  ░ ▒ ▒░    ░       ░▒ ░      ░▒ ░ ▒░ ░ ▒ ▒░
░ ░   ░ ░░░ ░ ░░       ░        ▒ ░    ░    ░░ ░ ░ ▒   ░         ░░        ░░   ░░ ░ ░ ▒
      ░   ░    ░ ░     ░ ░      ░      ░         ░ ░                        ░        ░ ░
               ░       ░                    ░
#ห้ามขายไอเด็กเปรต
#เล่นฟรีไม่เข้าใจทักมาถาม ID: psh100
""")
from linepy import *
from datetime import datetime
from time import sleep
import livejson, random, sys , null, threading, time, requests, schedule, os, datetime, re, json
import requests
from bs4 import BeautifulSoup
import threading
from collections import MutableMapping, MutableSequence

data = livejson.File('data.json')
user = livejson.File('user.json')
#เปลี่ยน os เองนะครับ
#line = LINE("gmail","passwd")

lineMid = line.profile.mid
linePoll = OEPoll(line)
botStart = time.time()
print (lineMid)
owner = "" #mid owner
settings = {
    "members": 20,
    "keyCommand": "",
    "setKey": False,
    "self": True,
    "joinlink": True
}

def restart():
    print ("[ RESTART BOT KICK]")
    python = sys.executable
    os.execl(python, python, *sys.argv)

def runtime(secs):
    mins, secs = divmod(secs,60)
    return '%02d' % (mins)

def runtime1(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d วัน %02d ชม %02d นาที' % (days, hours, mins)

def command(text):
    pesan = text.lower()
    if settings["setKey"] == True:
        if pesan.startswith(settings["keyCommand"]):
            cmd = pesan.replace(settings["keyCommand"],"")
        else:
            cmd = "Undefined command"
    else:
        cmd = text.lower()
    return cmd

def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 13:
            try:
                if lineMid in op.param3:
                    group = line.getGroup(op.param1).members
                    if len(group)>settings["members"]:
                        line.acceptGroupInvitation(op.param1)
                        if op.param1 in data["group"]:
                            return line.sendMessage(op.param1, data["spammsg"])
                        data["group"][op.param1]=True
                        line.sendMessage(owner, f"{line.getContact(op.param2).displayName} invite to {line.getGroup(op.param1).name}[{len(line.getGroup(op.param1).members)}]")
                        line.sendMessage(op.param1, data["joinmsg"])
                        if op.param2 in user:
                            user[op.param2]+=5
                        else:
                            if op.param2 not in user:
                                user[op.param2]=5
            except Exception as e:
                print (e)

        if op.type == 26:
            try:
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                    if msg.toType == 0:
                        if sender != line.profile.mid:
                            to = sender
                        else:
                            to = receiver
                    elif msg.toType == 1:
                        to = receiver
                    elif msg.toType == 2:
                        to = receiver
                if msg.contentType == 0:
                    if settings["joinlink"]==True:
                        if "/ti/g/" in msg.text.lower():
                            link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                            links = link_re.findall(text)
                            n_links = []
                            for l in links:
                                if l not in n_links:
                                    n_links.append(l)
                            for ticket_id in n_links:
                                group = line.findGroupByTicket(ticket_id)
                                if group.id in data["group"]:
                                    return
                                else:
                                    line.acceptGroupInvitationByTicket(group.id,ticket_id)
                                    data["group"][group.id]=True
                                    line.sendMessage(owner, f"join link {group.name}[{len(group.members)}] invite is {line.getContact(msg._from).displayName}")
                if msg.contentType == 0:
                    if text is None:
                        return
                    else:
                        cmd = command(text)
                        if "bot" == msg.text:
                            if settings["self"]==True:
                                line.sendMessage(to, "ออนไลน์")
                        if "/คำสั่ง" == msg.text:
                            line.sendMessage(to, data["help"])
                        if "/ck" == msg.text:
                            if data["time"]<=time.time():
                                line.sendMessage(to, "𝙍𝙚𝙖𝙙𝙮")
                            else:
                                secs = data["time"]-time.time()
                                tm = runtime(secs)
                                line.sendMessage(to, f"𝗖𝗼𝗼𝗹𝗱𝗼𝘄𝗻 {tm} 𝗺𝗶𝗻𝘂𝘁𝗲𝘀.")
                        if "/ticket:bot" == msg.text:
                            ticket = line.getUserTicket()
                            line.sendMessage(to, f"ลิ้งติดต่อบอทจ้าาาา\n{ticket}")
                        elif "/pro " in msg.text:
                            def pro():
                                if settings["self"]!=True:
                                    return line.sendMessage(to, "บอทปิดอยู่จ้า...")
                                if data["time"]>=time.time():
                                    secs = data["time"]-time.time()
                                    tm = runtime(secs)
                                    return line.sendMessage(to, f"𝗖𝗼𝗼𝗹𝗱𝗼𝘄𝗻 {tm} 𝗺𝗶𝗻𝘂𝘁𝗲𝘀.")
                                if sender not in user:
                                    return line.sendMessage(to, "คุณไม่อยู่ในระบบเชิญบอทเข้ากลุ่มเพื่อสมัครเข้าระบบจะได้รับตั๋วจำนวน5ใบ")
                                if user[sender]<=0:
                                    return line.sendMessage(to,"ตั๋วของคุณไม่เพียงพอสำหรับการโปรครั้งนี้กรุณาดึงบอทเข้ากลุ่มเพื่อรับตั๋ว5ใบ")
                                user[sender]-=1
                                s = msg.text.replace("/pro ","")
                                find = line.getGroupIdsJoined()
                                f = time.time()+600
                                data["time"]=f
                                for i in find:
                                    time.sleep(0.5)
                                    line.sendMessage(str(i), "{}".format(s))
                                line.sendMessage(msg.to, f"You ticket : {user[sender]}")
                                line.sendMessage(msg.to, f"โปรแล้วจำนวน {len(find)} กลุ่ม")
                            threading.Thread(target=pro).start()
                        elif "/listgroup" == msg.text:
                            group = line.getGroupIdsJoined()
                            line.sendMessage(msg.to, f"กลุ่มของบอทมีจำนวน {len(group)} จ้ะ..")
                        elif "/sc " in msg.text:
                            s = msg.text.replace("/sc ","")
                            line.sendContact(to, s)
                        elif "/msg:spam " in msg.text:
                            if sender in owner:
                                s = msg.text.replace("/msg:spam ","")
                                data["spammsg"]=str(s)
                                line.sendMessage(to, "ตั้งข้อความสแปมเชิญ:\n"+data["spammsg"]+" สำเร็จ")
                        elif "/msg:join " in msg.text:
                            if sender in owner:
                                s = msg.text.replace("/msg:join ","")
                                data["joinmsg"]=str(s)
                                line.sendMessage(to, "ตั้งข้อความเชิญ:\n"+data["joinmsg"]+" สำเร็จ")
                        elif "/msg:help " in msg.text:
                            if sender in owner:
                                s = msg.text.replace("/msg:help ","")
                                data["help"]=str(s)
                                line.sendMessage(to, "ตั้งข้อความคำสั่ง:\n"+data["help"]+" สำเร็จ")
                        elif "/rules" == msg.text:
                            if data["rules"]!="":
                                line.sendMessage(to,str(data["rules"]))
                            else:
                                line.sendMessage(to,"กรุณาตั้งกฏก่อนเจ้าค่ะ")
                        elif "/msg:rules " in msg.text:
                            if sender in owner:
                                s = msg.text.replace("/msg:rules ","")
                                data["rules"]=str(s)
                                line.sendMessage(to, "ตั้งข้อความกฏ:\n"+data["rules"]+" สำเร็จ")
                        elif "/ticket" == msg.text:
                             if sender in user:
                                 line.sendMessage(to, "Ticket you {}".format(user[sender]))
                             else:
                                 user[sender]=0
                                 line.sendMessage(to, "Ticket you {}".format(user[sender]))
                        elif "/mid" in msg.text:
                             line.sendMessage(to, f"{sender}")
                        elif text.lower() == 'แทค':
                            if msg._from in owner:
                                group = line.getGroup(msg.to)
                                nama = [contact for contact in group.members]
                                k = len(nama)//20
                                for a in range(k+1):
                                    txt = u''
                                    s=0
                                    b=[]
                                    for i in group.members[a*20 : (a+1)*20]:
                                        b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                                        s += 7
                                        txt += u'@POND \n'
                                    line.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                                line.sendMessage(to, "สมาชิก {} ".format(str(len(nama))))
            except Exception as e:
                print (e)
    except Exception as e:
        print (e)
profile = line.getProfile()
profile.displayName = "ᴘʀᴇᴍɪᴜᴍ ʙᴏᴛ ᴘʀᴏ"
line.updateProfile(profile)
def run():
    while True:
        try:
            ops = linePoll.singleTrace(count=100)
            if ops is not None:
                for op in ops:
                    th = threading.Thread(target=bot, args=(op,))
                    th.start()
                    th.join()
                    linePoll.setRevision(op.revision)
        except Exception as error:
            print (error)
if __name__ == "__main__":
    run()
