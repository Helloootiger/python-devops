# while loop

count = 0

while count < 5:
    print(count)
    count += 1


# making it bit complex using break and continue

count = 0

while count < 5:  
    count += 1
    if count == 4:
        break
    print(count)  


  
count = 0

while count < 5:  
    count += 1
    if count == 3:
        continue
    print(count)


