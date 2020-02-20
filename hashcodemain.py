global B,L,D,Bscores
LibSignUpDays=[]
LibMaxBooksSent=[]
LibBooks={}
def take_input():
    global B,L,D,Bscores
    [B,L,D] = [int(i) for i in input().split()]
    Bscores = [int(i) for i in input().split()]
    for i in range(L):
        [_,signupdays,maxBooks]=[int(x) for x in input().split()]
        books = set([int(x) for x in input().split()])
        LibSignUpDays.append(signupdays)
        LibMaxBooksSent.append(maxBooks)
        LibBooks[i]=books

take_input()
# print(B,L,D,Bscores,LibSignUpDays,LibMaxBooksSent,LibBooks,sep=' ')