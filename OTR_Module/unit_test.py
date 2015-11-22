
import otrmodule

import queue



receive1 = queue.Queue()
receive2 = queue.Queue()

def sendToBob(msg) :
    print("================= Alice Send To Bob =================")
    print(msg)
    receive2.put(msg)

def sendToAlice(msg) :
    print("================= Bob Send To Alice =================")
    print(msg)
    receive1.put(msg)


def Print(msg) :
    print(msg)



acc1 = otrmodule.otrimplement.MyAccount('Alice')
acc2 = otrmodule.otrimplement.MyAccount('Bob')


otr1 = otrmodule.OtrModule(acc1, sendToBob, Print, Print)
otr2 = otrmodule.OtrModule(acc2, sendToAlice, Print, Print)



otr1.RequestConnect()

while not receive2.empty() :
    result = otr2.ReplyConnect(receive2.get())
    if result :
        print("==================Bob Connection Complete==================")

while not receive1.empty() :
    result = otr1.ReplyConnect(receive1.get())
    if result :
        print("==================Alice Connection Complete==================")

while not receive2.empty() :
    result = otr2.ReplyConnect(receive2.get())
    if result :
        print("==================Bob Connection Complete==================")

while not receive1.empty() :
    result = otr1.ReplyConnect(receive1.get())
    if result :
        print("==================Alice Connection Complete==================")

while not receive2.empty() :
    result = otr2.ReplyConnect(receive2.get())
    if result :
        print("==================Bob Connection Complete==================")



























