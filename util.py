#utilities

#type helpers
def are_lists(*args):
    for data in args:
        if not type(data)==list:
            return false
    return true

def is_list(arg):
    return type(arg)==list

def is_str(*args):
    for strs in 

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

"""
sorting algorithms with extended functions
"""

def dealer(deal):
    """
    helper function to deal with the deals (how to deal with illeagle data)
    return order: delete(remove the illegal data from the sorting queqe)
                  pack(pack the illegal data in a list and return it with the sorted queqe)
                  back(push the illegal data into the end of the sorted queqe)
    d and b are exclusive to each other; p is containable with the other two
    if b and d happen together CmdError is thrown
    the dealer will not see extra charecters; it will only see if b,d,p is present
    """
    delete=(deal.find("d")!=-1)
    pack=(deal.find("p")!=-1)
    back=(deal.find("b")!=-1)
    if back and delete:
        throw CmdError("d and b were given to the sort dealer at the same time") #to be written
    return delete,pack,back


def Bsort(lst,start,end,method = lambda a,b : a<b,type=None,deal="d"):
    """Bsort"""
    #unfinished
 
