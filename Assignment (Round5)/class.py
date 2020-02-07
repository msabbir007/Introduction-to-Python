def main():
    l1=[1,2,3,4,55,6]
    l2=l1
    #insert with splice (:)
    l2[1:1]=[0,0,0,0,0]
    l3=[2,4,5,6]
    l3+=[4,5]
    print(l1)
    print(l2)
    
main()
