class Permutation:
    nums = list()
    length = 0
    def set(self, nums):
        self.nums = nums
        self.length = len(nums)
    def _find_max_index(sefl, permutation):
        for i in range(len(permutation) - 2, -1, -1):
            if permutation[i] < permutation[i+1]:
                return i
        return -1

    def _find_index_bigger_element(self, permutation, element):
        for i in range(len(permutation) - 1, -1, -1):
            if permutation[i] > element:
                return i
        return -1

    def _factorial(self, n):
        if n == 0:
            return 1
        else: 
            return n*self._factorial(n-1)

    def _swap(self, permutation, i, j):
        permutation[i], permutation[j] = permutation[j], permutation[i]

    def _reverse_permutation(self, permutation, index):
        n = len(permutation)
        permutation = permutation[:index+1:] + permutation[n - 1:index:-1]
        return permutation

    def permutation_generator(self):
        permutation = self.nums
        print(' '.join(permutation))
        index = self._find_max_index(permutation)
        for i in range(1,self._factorial(self.length)):
            if index != -1:
                element = permutation[index]
                self._swap_index = self._find_index_bigger_element(permutation, element)
                self._swap(permutation, index, self._swap_index)
                permutation = self._reverse_permutation(permutation, index)
                print(' '.join(permutation))
                index = self._find_max_index(permutation)
            else:
                permutation = permutation[::-1]
                print(' '.join(permutation))
                index = self._find_max_index(permutation)
                
P = Permutation()
P.set (input().split(" "))
P.permutation_generator()
