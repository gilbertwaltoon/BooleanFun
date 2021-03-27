import math

def distinct_elements(F, verbose = False):
    if not F:
        if verbose:
            print("Null set", "No distint elements")
        return {'de': [], 'nde': []}
    else:
        if type(F) is not list:
            F = [F]
        p = set.union(*map(set,F))  
        if verbose:
            print(len(p),"distinct elements",p,"of",F)
        return {'de': p, 'nde': len(p)}


# def make_bkts(F):
#     n = count_distinct_elements(F)
#     return [set() for _ in range(2**n)]

  
def deposit(bks,s):
   oldbk = bks[len(s)].copy()
   bks[len(s)].add(s)
   if oldbk != bks[len(s)]:
        return True
   else:
        return False
    
def nwdeposit(bks,s):
    print("length of new set to be depositied", len(s))
    print("bks[len] is currently", bks[len(s)])
   # bks[len(s)].append(s)    


def bucketise(F):
    bks = make_bkts(F)
    for f in F:
        deposit(bks,f)
    return bks


def powerlist(fs):
    # return power set of fs as a list of sets
    pl = []
    l = [_ for _ in fs] # copy to list for ease of indexing        
    x = len(l)
    pl = []
    for i in range(1<<x):
        pl.append([l[j] for j in range(x) if (i & (1 << j))])
    return pl

def unionise(pl):
    # take a power set list (i.e retuned by powerlist) and form unions
  #  ps = set()
    ps = []
    for i,l in enumerate(pl):
        cs = frozenset()
        for s in l:
           cs = cs.union(s)
        ps.append([cs])
    return ps

def setise(u):
    su = set()
    for l in u:
        for s in l:
            if s:
                su.add(s)
    l = []
    for s in su:
        l.append([s])
    return l

def union_close(F):
    pl = powerlist(F)  # get power set of the family-of-sets
    return unionise(pl)  # form the union for each member of the list

def sort_family(F):
  #  l = [s for s in F] # copy to list for ease of indexing 
    ll = [len(s) for s in F] # make a list of sizes of sets#
  
    return [x for _,x in sorted(zip(ll,F))]

def print_family(F, heading=""):
    if type(F) is set:
        ff = []
        for s in F:
            ff.append([s])
        F = ff
    sF = sort_family(F)
    print(heading)
    for f in F:
        s = ''        
        for n in f:
            for a in n:
                s = s + str(a) + " "
        print(s)

    
def sort_dict(d):
    ds = {}
    sortednames = sorted(d.keys(), key=lambda x:x.lower())    
    for nm in sortednames:
        ds[nm] = d[nm]
    return ds

def count_elements(LofL):
    if type(LofL) is set:
        ll = []
        for s in LofL:
            ll.append([s])
        LofL = ll       
    dic = {}
    for l in LofL:
        de = distinct_elements(l, verbose=False)
        for e in de['de']:
            for s in l:
                if e in s:
                    if str(e) in dic:
                        dic[str(e)] += 1
                    else:
                        dic[str(e)] = 1
         
    return dic


def pairs(n):
    return(n-1)*(n)/2

def chs(k,n):
    return math.factorial(n)/(math.factorial(k) * math.factorial(n-k))
    
    

def quad(n):
    return n*(n+1)*(n+2)*(n+3)
    
def stats(Ps,dic):
    # first get longest poss  
    # mxln = 0
    # for i,p in enumerate(Ps):
    #     if len(p) > mxln:
    #         mxln= len(p)
    #         mxi = i
    # print("max len",mxln,"at",i)
    pmx = (Ps[-1])
    de = distinct_elements(pmx, verbose=False) 
    lps = len(Ps)
    sdic ={}
    for e in de['de']:
        # create emprt matrix to hold stats
        sdic[str(e)] = [0 for _ in range(0,lps)]
        
    for i,p in enumerate(Ps):
        de = distinct_elements(p, verbose=False) 
        for e in de['de']:
            n = 0
            for s in p:
                if e in s:
                    n = n + 1
            sdic[str(e)][i] = n
    for sd in sdic:
        print(sd, ":", sdic[sd], sum(sdic[sd]))
  

F = {
      frozenset([2]),
      frozenset([2,3]), 
      frozenset([1,2]),
      frozenset([4,2]),
      frozenset([5,2]),
      frozenset([6,2]),
  #    frozenset([4,2,7]),
    #  frozenset([5,2]),
    #  frozenset([2,4]),
    #  frozenset([1,2,3]),
      # frozenset([1,4,5]),
      # frozenset([2,4,6]),
      # frozenset([3,5,6]),
      }

depF = count_elements(F)
print_family(F,"0.Initial family" )
print("Element counts in family:",sort_dict(depF))
print("")


#uF = union_close(F)
#print_family(uF)


pL = powerlist(F)
#print(pL)
print_family(pL, "1. Power Family")
depl = count_elements(pL)

#print("Element counts in power family:",sort_dict(depl))
#stats(pL, depl)
#print("")

# print("----")
# u = unionise(pL)
# print_family(u, "2. Unionised power set")
# deu = count_elements(u)
# print("Element counts Unionised power set:",sort_dict(deu))
# print("")
    

# # print("")
# cuf = setise(u)
# decuf = count_elements(cuf)
# print_family(cuf, "3. Members of Unionised set, moved into a set")
# print("Element counts in CUF:",sort_dict(decuf))
# # print("")

print("")
for i in range(3,10):
    print(i, pairs((i)))
    print(i, chs(2,i))
   

       








    


