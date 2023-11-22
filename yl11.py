a = input("sisesta string: ").string()
   
if len(a)>= 7:
        if(len(a) % 2) == 0:
            print("arv on paaris!")
else:
                print("arv ei ole paaris!")
                
print(a[len(a)//2-1:len(a)//2+2])