import object
import dict
import float
import int
import list

if __name__ == "__main__":
    print([1, 2, 3].filter(lambda x: x <= 2).to_list())
    print(range(10).filter(lambda x: x % 2 == 0).to_list())
    print([1,2,3].map(lambda x: pow(x, 2)).to_list())
    print([1,2,3].map(lambda x: pow(x, 2)).to_list())
    print(range(5).reduce(lambda a, x: a+x, 0).to_str().to_list())
    print([1, 2, 3].to_tuple())