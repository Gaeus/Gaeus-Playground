studentamount=input('How many students on the course? :')
groupamount=input('Desiredgroupsize? :')

groupformed=int(studentamount)//int(groupamount)

groupformed = (int(studentamount) + int(groupamount) - 1) // int(groupamount)

print(f"Number of groups formed: {groupformed}")