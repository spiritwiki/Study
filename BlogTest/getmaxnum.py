#-*- coding:utf-8 -*-
"""
对一些数进行排列找出最大的数
"""

def get_max_num(numbers):
    """
    对一些数字寻找最大排列
    """
    str_numbers =[str(i) for i in numbers]
    digit_num = sum(len(i) for i in str_numbers)
    seqs = [NumChooseSeq('', '', str_numbers)]
    
    for _ in range(digit_num):
        new_seqs = []
        for seq in seqs:
            new_seqs += list(seq.choose_next())

        max_num = max(i.curr_num for i in new_seqs)
        new_seqs = [i for i in new_seqs if i.curr_num == max_num]

        seqs = new_seqs

    return int(seqs[0].curr_num)


class NumChooseSeq():


    def __init__(self, curr_num, follow, unused):
        self.curr_num = curr_num
        self.unused = unused
        self.follow = follow


    def choose_next(self):
        if self.follow:
            yield NumChooseSeq(self.curr_num+self.follow[0], self.follow[1:], self.unused)
        else:
            max_num = max(i[0] for i  in self.unused)
            for index,num_ in enumerate(self.unused):
                if num_[0] == max_num:
                    rest = self.unused[:index] + self.unused[index+1:]
                    yield NumChooseSeq(self.curr_num+num_[0], num_[1:], rest)


    def show(self):
        print('curr', self.curr_num, 'follow',self.follow, 'unused', self.unused)
                
def test():
    assert(get_max_num([1,2,3]) == 321)
    assert(get_max_num([1,10,1]) == 1110)
    assert(get_max_num([958,9,5,6]) == 995865)
    assert(get_max_num([30,31,3,2]) == 331302)

if __name__ == '__main__':
    test()
