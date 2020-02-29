list_ = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print([list_[el] for el in range(1, len(list_)) if list_[el] > list_[el-1]])

