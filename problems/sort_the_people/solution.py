class Solution(object):
    def sortPeople(self,names, heights):

        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        import numpy as np
        ind = np.lexsort((names,heights))
        ind=ind[::-1]
        namess=[]
        for i in ind:
            print(names[i])
            namess.append(names[i])
        return namess