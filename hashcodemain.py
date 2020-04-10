import sys 
global B,L,D,Bscores
LibSignUpDays=[]
LibMaxBooksSent=[]
LibBooks={}
# Libs=(LibSignUpDays,LibMaxBooksSent,LibBooks)
Libs=[]
Libstaken={}
LibstakenIndex=[]
procLibCalledCount = 0
LimitThreshold=10
sys.setrecursionlimit(1000000)

def take_input(f):
    global B,L,D,Bscores
    [B,L,D] = [int(i) for i in f.readline().split()]
    Bscores = [int(i) for i in f.readline().split()]
    for i in range(L):
        [_,signupdays,maxBooks]=[int(x) for x in f.readline().split()]
        books = [int(x) for x in f.readline().split()]
        books.sort(lambda x: Bscores[x],reverse=False)
        LibSignUpDays.append(signupdays)
        LibMaxBooksSent.append(maxBooks)
        LibBooks[i]=books
        Libs.append((signupdays,maxBooks,books))

def calculateScoreAndBooksSent(libry,days):
    bookCount=libry[1]*days
    score = 0;books2Sent=[]
    while len(books2Sent)<books2Sent or libry[2] not in books2Sent :
        if 

def max(days,current_samples,remainingLibs):
    if days <= 0:
        return 0,[]
    if current_samples is None or current_samples==[]:
        scoresAndBooks=[]
        for l in Libs:
            score,booksSent=calculateScoreAndBooksSent(l,1)
    else:
        pass
    

if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        take_input(f)
        # print(processLibrary())
        # processLibrary(D)
        print(len(Libstaken))
        for k in LibstakenIndex:
            print(k,len(Libstaken[k]))
            [print(v1,end=' ') for v1 in Libstaken[k]]
            print()