studentamount=input('How many participants? :')
groupamount=input('Desired group size? :')

groupformed = (int(studentamount) + int(groupamount) - 1) // int(groupamount)

print(f"Number of groups formed: {groupformed}")