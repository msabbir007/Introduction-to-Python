a=int(input("Purchase price:"))
b=int(input("Paid amount of money:"))

if a>=b:
    print("No change")
else:
    print("Offer change:")
    c=b-a;
    if c%10==0 and c//10!=0 :
        d = c//10;
        e=c%10;
        print(d,"ten-euro notes")
    elif c%10!=0 and c//10!=0 :
        d = c // 10;
        print(d,"ten-euro notes")
        e = c % 10
        if  e%5==0 and e//5!=0:
            f=e//5;
            print(f,"five-euro notes")
            g = e % 5;
        elif e%5!=0 and e//5!=0:
            f = e // 5;
            print(f,"five-euro notes")
            g = e % 5;
            if  g%2==0 and g//2!=0:
                h=g//2;
                i=g%2;
                print(h,"two-euro coins")
            elif g%2!=0 and g//2!=0:
                h = g // 2;
                i = g % 2;
                print(h, "two-euro coins")
                if i%1==0 and i//1!=0:
                    j=i//1;
                    k=i%1;
                    print(j, "one-euro coins")
                elif i%1!=0 and i//1!=0:
                    j=i//1;
                    k=i%1;
                    print(j, "one-euro coins")
            else:
                h = g // 2;
                i = g % 2;
                if i%1==0 and i//1!=0:
                    j=i//1;
                    k=i%1;
                    print(j, "one-euro coins")
                elif i%1!=0 and i//1!=0:
                    j=i//1;
                    k=i%1;
                    print(j, "one-euro coins")


        else:
            f = e // 5;
            g = e % 5;
            if g % 2 == 0 and g // 2 != 0:
                h = g // 2;
                i = g % 2;
                print(h, "two-euro coins")
            elif g % 2 != 0 and g // 2 != 0:
                h = g // 2;
                i = g % 2;
                print(h, "two-euro coins")
                if i%1==0 and i//1!=0:
                    j=i//1;
                    k=i%1;
                    print(j, "one-euro coins")
                elif i%1!=0 and i//1!=0:
                    j=i//1;
                    k=i%1;
                    print(j, "one-euro coins")
            else:
                i = g % 2;
                h = g // 2;

                if i%1==0 and i//1!=0:
                    j=i//1;
                    k=i%1;
                    print(j, "one-euro coins")
                elif i%1!=0 and i//1!=0:
                    j=i//1;
                    k=i%1;
                    print(j, "one-euro coins")

    else:
        if  c%5==0 and c//5!=0:
            f=c//5;
            print(f,"five-euro notes")
            g = c % 5;
        elif c%5!=0 and c//5!=0:
            f = c // 5;
            print(f,"five-euro notes")
            g = c % 5;
            if  g%2==0 and g//2!=0:
                h=g//2;
                i=g%2;
                print(h,"two-euro coins")
            elif g%2!=0 and g//2!=0:
                h = g // 2;
                i = g % 2;
                print(h, "two-euro coins")
                if i%1==0 and i//1!=0:
                    j=i//1;
                    k=i%1;
                    print(j, "one-euro coins")
                elif i%1!=0 and i//1!=0:
                    j=i//1;
                    k=i%1;
                    print(j, "one-euro coins")
            else:
                h = g // 2;
                i = g % 2;
                if i%1==0 and i//1!=0:
                    j=i//1;
                    k=i%1;
                    print(j, "one-euro coins")
                elif i%1!=0 and i//1!=0:
                    j=i//1;
                    k=i%1;
                    print(j, "one-euro coins")


        else:
            f = c // 5;
            g = c% 5;
            if g % 2 == 0 and g // 2 != 0:
                h = g // 2;
                i = g % 2;
                print(h, "two-euro coins")
            elif g % 2 != 0 and g // 2 != 0:
                h = g // 2;
                i = g % 2;
                print(h, "two-euro coins")
                if i%1==0 and i//1!=0:
                    j=i//1;
                    k=i%1;
                    print(j, "one-euro coins")
                elif i%1!=0 and i//1!=0:
                    j=i//1;
                    k=i%1;
                    print(j, "one-euro coins")
            else:
                i = g % 2;
                h = g // 2;

                if i%1==0 and i//1!=0:
                    j=i//1;
                    k=i%1;
                    print(j, "one-euro coins")
                elif i%1!=0 and i//1!=0:
                    j=i//1;
                    k=i%1;
                    print(j, "one-euro coins")


