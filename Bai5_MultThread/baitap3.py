import threading
import random

class MaxThread (threading.Thread):
    def __init__(self,lo,hi,list_nums):
        threading.Thread.__init__(self)
        self.lo = lo
        self.hi = hi
        self.list_nums = list_nums
        self.max = 0
    def run(self):
        self.set_max()
    def set_max(self):
        i = self.lo
        self.max = self.list_nums[i]
        while i < self.hi:
            if self.list_nums[i] > self.max:
                self.max = self.list_nums[i]
            i+=1
        return self.max
    def print_list(self):
        str_list =''
        i = self.lo
        self.max = self.list_nums[i]
        while i < self.hi:
            str_list += str(self.list_nums[i]) + '; '
            if self.list_nums[i] > self.max:
                self.max = self.list_nums[i]
            i += 1
        str_list += 'Max =' + str(self.max)
        return str_list

def tim_max(list_numbers, n_threads):
    max = 0
    so_pt = len(list_numbers)
    list_threads = []

    i = 0
    while i < n_threads:
        lo = int((i*so_pt)/n_threads)
        hi = int(((i+1)*so_pt)/n_threads)
        thread = MaxThread(lo,hi,list_numbers)
        list_threads.append(thread)
        list_threads[i].start()
        i +=1

    j = 0
    max = list_threads[j].set_max()
    while j < n_threads:
        list_threads[j].join()
        if  list_threads[j].set_max() > max:
            max = list_threads[j].set_max()
        print('Thread ', j+1, ":", list_threads[j].print_list())
        j +=1

    return max

if __name__ == "__main__":
    list_numbers = []
    n = int(input('Nhập số phần tử: \t'))
    i = 0
    while i<n:
        list_numbers.append(random.randrange(100))
        i +=1
    print('list:', list_numbers)
    n_threads = int(input('Nhập vào số thread: \t'))
    max = tim_max(list_numbers,n_threads)
    print('Max=',max)