def sum_list(list):
    if len(list)==0:
        return None
    if len(list)==1:
        return list[0]
    return list[0]+sum_list(list[1:])

        

    # else:
    #     if len(list)>1:
    #         sum=sum+list[len(list)-1]
    #         list.remove(list[len(list)-1])
    #         sum_list(list)
    #     else:
    #         sum=sum+list[len(list)-1]
    #         return sum


    
if __name__ == "__main__":
    listA = []
    listB = [3]
    listC = [1, 2, 3, 4]
    assert sum_list(listA) == None
    assert sum_list(listB) == 3
    assert sum_list(listC) == 10
    print('Everything works correctly!') 