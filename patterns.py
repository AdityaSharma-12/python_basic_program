a=int(input("Enter the range of pattern:"))

'''for i in range(1,a+1):
    for j in range(i):
        print("*",end=" ")
    print()
o/p:
* 
* *
* * *
* * * *
* * * * *
* * * * * *   '''


'''for i in range(1,a+1):
    for j in range(a+1-i):
        print("*",end=" ")
    print()
o/p:
* * * * * * 
* * * * *
* * * *
* * *
* *
*     '''


'''for i in range(1,a+1):
    for j in range(i):
        print(j+1,end=" ")
    print()
o/p:
1 
1 2
1 2 3
1 2 3 4
1 2 3 4 5
1 2 3 4 5 6   '''


'''for i in range(1,a+1):
    for j in range(a+1-i):
        print(j+1,end=" ")
    print()
o/p:
1 2 3 4 5 6 
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1     '''


'''k=1
for i in range(1,a+1):
    for j in range(i):
        print(k,end=" ")
        k+=1
    print()
o/p:
1 
2 3
4 5 6
7 8 9 10
11 12 13 14 15
16 17 18 19 20 21   '''


'''k=1
for i in range(1,a+1):
    for j in range(a+1-i):
        print(k,end=" ")
        k+=1
    print()
o/p:
1 2 3 4 5 6 
7 8 9 10 11
12 13 14 15
16 17 18
19 20
21  '''


'''for i in range(1,a+1):
    for j in range(1,a+1):
        print("*",end=" ")
    print()
o/p:
* * * * * * 
* * * * * *
* * * * * *
* * * * * *
* * * * * *
* * * * * *    '''


'''for i in range(1,a+1):
    for j in range(i):
        print("*",end=" ")
    print()
for i in range(1,a+1):
    for j in range(a+1-i):
        print("*",end=" ")
    print()
o/p:
* 
* *
* * *
* * * *
* * * * *
* * * * * *
* * * * * *
* * * * *
* * * *
* * *
* *
*   '''


'''for i in range(1,a+1):
    for j in range(i):
        print(i,end=" ")
    print()
o/p:
1 
2 2
3 3 3
4 4 4 4
5 5 5 5 5
6 6 6 6 6 6  '''


'''for i in range(1,a+1):
    for j in range(i):
        print(chr(ord("A")+j),end=" ")
    print()
o/p:
A 
A B
A B C
A B C D
A B C D E
A B C D E F   '''


'''k=ord("A")
for i in range(1,a+1):
    for j in range(i):
        print(chr(k),end=" ")
        k+=1
    print()
o/p:
A 
B C
D E F
G H I J
K L M N O
P Q R S T U   '''


'''for i in range(1,a+1):
    for k in range(a-i):
        print("",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()
o/p:
     * 
    * *
   * * *
  * * * *
 * * * * *
* * * * * *   '''


'''for i in range(1,a+1):
    for k in range(a-i):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()
o/p:
          * 
        * *
      * * *
    * * * *
  * * * * *
* * * * * *   '''


'''for i in range(1,a+1):
    for k in range(a-i):
        print("",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()
for i in range(1,a+1):
    for k in range(i-1):
        print("",end=" ")
    for j in range(a+1-i):
        print("*",end=" ")
    print() 
o/p:
     * 
    * *
   * * *
  * * * *
 * * * * *
* * * * * *
* * * * * *
 * * * * *
  * * * *
   * * *
    * *
     *    '''


