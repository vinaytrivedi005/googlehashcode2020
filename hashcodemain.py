import sys
global B,L,D,Bscores
LibSignUpDays=[]
LibMaxBooksSent=[]
LibBooks={}
Libs=(LibSignUpDays,LibMaxBooksSent,LibBooks)
Libstaken={}
LibstakenIndex=[]
procLibCalledCount = 0
sys.setrecursionlimit(1000000)
def take_input(f):
    global B,L,D,Bscores
    [B,L,D] = [int(i) for i in f.readline().split()]
    Bscores = [int(i) for i in f.readline().split()]
    for i in range(L):
        [_,signupdays,maxBooks]=[int(x) for x in f.readline().split()]
        books = set([int(x) for x in f.readline().split()])
        LibSignUpDays.append(signupdays)
        LibMaxBooksSent.append(maxBooks)
        LibBooks[i]=books

def max_score_forgiven_days(Lib2Check,days):
    max_score=0
    days-=Lib2Check[0]
    if days<=0:
        return 0,[]
    else:
        books=Lib2Check[2]
        scoredBooks=[(b,Bscores[b]) for b in books]
        def sortFunc(x):
            return x[1]
        scoredBooks=sorted(scoredBooks,key=sortFunc,reverse=True)
        book2send = []
        for d in range(days*Lib2Check[1]):
            if(d>=len(scoredBooks)):
                break
            max_score+=scoredBooks[d][1]            
            book2send.append(scoredBooks[d][0])
        # return max_score,[bookSent[0] for bookSent in scoredBooks[:d+1]]
        return max_score,book2send


def processLibrary(days):
    global LibSignUpDays,LibMaxBooksSent,LibBooks,Libstaken,LibstakenIndex,procLibCalledCount
    procLibCalledCount +=1; print(procLibCalledCount)
    max_score=0;max_score_lib=-1;max_booksSent=None
    if days<=1:
        return max_score
    # while true:
    for i in range(L):
        if i in Libstaken or len(LibBooks[i])<=0:
            continue
        score,booksSent=max_score_forgiven_days((LibSignUpDays[i],LibMaxBooksSent[i],LibBooks[i]),days)
        if max_score<score:
            max_booksSent=booksSent
            max_score=score
            max_score_lib=i
    # print(max_score)
    if max_score_lib==-1 or max_score==0:
        return 0
    days=days-LibSignUpDays[max_score_lib]
    books2remove=LibBooks[max_score_lib]
    # LibSignUpDays.pop(max_score_lib)
    # LibMaxBooksSent.pop(max_score_lib)
    # LibBooks.pop(max_score_lib)
    Libstaken[max_score_lib]=max_booksSent
    LibstakenIndex.append(max_score_lib)
    # print(LibBooks)
    temp=[(books,b) for books in LibBooks for b in books2remove if b in LibBooks[books]]
    for t in temp:
        LibBooks[t[0]].remove(t[1])
    return max_score + (processLibrary(days))

if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        take_input(f)
        # print(processLibrary())
        processLibrary(D)
        print(len(Libstaken))
        for k in LibstakenIndex:
            print(k,len(Libstaken[k]))
            [print(v1,end=' ') for v1 in Libstaken[k]]
            print()
# print(B,L,D,Bscores,LibSignUpDays,LibMaxBooksSent,LibBooks,sep=' ')