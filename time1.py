class Course(object):
    def __init__(self, name, subject, creadit, room, totsub, ctchr, allsub, breaks):
        self.name = name
        self.subject = subject
        self.creadit = creadit
        self.room = room
        self.totsub = totsub
        self.ctchr = ctchr
        self.allsub = allsub
        self.breaks = breaks


co = []*20
co.append(Course)


class Teach(object):
    def _init_(self, name, sub, cors, totalsub, allsub):
        self.name= name
        self.sub = sub
        self.cors = cors
        self.totalsub = totalsub
        self.allsub = allsub

    class Teach1:
        class Teach2:
            busy = [True, False]
            bool([busy])
        busy=[]*10
    busy = []*10


th = []*20
th.append(Teach)


class Room(object):
    def _init_(self, room, allsub):
        self.room = room
        self.allsub = allsub

    class R1:
        class R2:
            busy = [True, False]
            bool([busy])
        busy = []*10
    busy=[]*10

    class L1:
        class L2:
            lunch = [True, False]
            bool([lunch])
        lunch = []*10
    lunch = []*2


room_ro = []*20
room_ro.append(Room)


class Tmpsub(object):

    class T1:
        class T2:
            tmpsub = []*20

        Tmpsub = []*20
    Tmpsub=[]*20


Tmpsub = []*20
Tmpsub.append(Tmpsub)


class Tmptchr(object):

    class Tc1:
        class Tc2:
            tmptchr = []*20

        Tmptchr = []*20
    Tmptchr=[]*20


Tmptchr = []*20
Tmptchr.append(Tmptchr)


class Fisup(object):

    class Fu1:
        class Fu2:
            fisub = []*20

        Fisup = []*20
    Fisup = []*20


Fisup = []*20
Fisup.append(Fisup)


class Fitch(object):

    class Ft1:
        class Ft2:
            fitch = []*20

        Fitch = []*20
    Fitch = []*20


Fitch = []*20
Fitch.append(Fitch)


def input():

    print("enter total no. of days,lectures,courses,teachers and rooms")
    dys = int(input("enter no. of days:"))
    lects = int(input("enter no. of lectures:"))
    crs = int(input("enter total courses:"))
    tch = int(input("enter no. of teachers:"))
    room = int(input("enter no. of rooms:"))

    for i in range(1 , room):
       print("enter room no")
       room_ro[i].room = int(input())

    for i in range(1 , tch):
       print("enter teacher name")
       th[i].name =input()

    for i in range(1, crs):
       print("enter room no")
       co[i].name =input()
       co[i].totsub=int(input())
       for j in range(1 , co[i].totsub):
            print("enter room no")
            co[i].subject[j] =input()
            co[i].creadit[j]=int(input())
            co[i].allsub+=co[i].creadit[j]
            print("select a teacher for subject")
            for k in range(1,tch):
                print(th[k].name)
                tmptch=int(input())
                th[tmptch].sub[th[tmptch].totsub]=j
                th[tmptch].cors[th[tmptch].totsub]=i
                th[tmptch].totsub+1
                th[tmptch].allsub+=co[i].creadit[j]

                if th[tmptch].allsub>((lects*dys)-dys):
                    print("more than limited sub to a teacher")



            print("enter a room for this course")
            for j in range(1,room):
                print("room"+j+" "+room_ro[j].room)
            tmproom=int(input())
            co[i].room=tmproom
            room_ro[tmproom].allsub+=co[i].allsub
            if room_ro[tmproom].allsub>lects*dys-dys:
                print("more than limited sub in a room")
