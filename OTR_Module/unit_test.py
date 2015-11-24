
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


def PrintError(msg):
    print("================= Error =================")
    print(msg)

def PrintAlice(msg) :
    print("================= Alice =================")
    print(msg)


def PrintBob(msg) :
    print("================= Bob =================")
    print(msg)


acc1 = otrmodule.otrimplement.MyAccount('Alice')
acc2 = otrmodule.otrimplement.MyAccount('Bob')


otr1 = otrmodule.OtrModule(acc1, sendToBob, PrintAlice, PrintError)
otr2 = otrmodule.OtrModule(acc2, sendToAlice, PrintBob, PrintError)

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


otr1.RequestVerification()

while not receive2.empty() :
    result = otr2.ReceiveMessage(receive2.get())
    if result :
        print("================== Failed Bob Receive ==================")


while not receive1.empty() :
    result = otr1.ReceiveMessage(receive1.get())
    if result :
        print("================== Failed Alice Receive ==================")





















