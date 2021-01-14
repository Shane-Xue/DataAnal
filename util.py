#utilities

#type helpers
def are_lists(*args):
    for data in args:
        if not type(data)==list:
            return false
    return true

def is_list(arg):
    return type(arg)==list

def copy_merge(one,two):
    rt=[]
    for data in one:
        rt.append(data)
    for data in two:
        rt.append(data)
    return rt

def append_merge(one,two):
    for data in two:
        one.append(data)
    return one

def list_collapse(lst):
    """
    only collapses the second layer of list; does not touch others such as individual data
    or other data containers (sets,dicts,etc)
    """
    if not is_list(lst):
        raise TypeError(f"Wrong type: list_collapse() expected list; got {type(lst)}")
    m=[]
    for sub in lst:
        if is_list(sub):
            append_merge(m,sub)
    return lst

def Bsort(lst,start,end,method = lambda a,b : a<b,type=None,deal="d"):
    """Bsort"""
    #unfinished
 
