def main():
    a=input(str("Enter a word: "))
    count=0
    for i in range(len(a)):
        if a[i]=="a" or a[i]=="e" or a[i]=="i" or a[i]=="o" or a[i]=="u":
            count+=1
    print("The word",a[:],"contains",count,"vowels and",len(a)-count,"consonants")
main()
