from merge import mergesort

def test():
    
    arr = [3,2,1]
    assert(mergesort(arr) == [1,2,3])

    arr = [1]
    assert(mergesort(arr) == [1])

    arr = [1,9,7,4,6,2,1]
    assert(mergesort(arr) == [1,1,2,4,6,7,9])

    arr = [1,2,3]
    assert(mergesort(arr) == [1,2,3])


    print("All Tests Passed!")


if __name__ == "__main__":
    test()