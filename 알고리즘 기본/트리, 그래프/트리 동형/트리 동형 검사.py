def TreeIsomorphisTest(RootNodeA, RootNodeB):
    if RootNodeA == None and RootNodeB == None :
        return True
    if RootNodeA != None or RootNodeB != None:
        return False
    if RootNodeA.Data != RootNodeB.Data :
        return False
    return ((TreeIsomorphisTest(RootNodeA.LeftChild, RootNodeB.LeftChild) and
             TreeIsomorphisTest(RootNodeA.RightChild, RootNodeB.RightChild)) or
             (TreeIsomorphisTest(RootNodeA.LeftChild, RootNodeB.RightChild) and
              TreeIsomorphisTest(RootNodeA.RightChild, RootNodeB.LeftChild)))