names=['Chethan', 'Chethan Bekal','Chethan Yeshwanth Bekal']
initials = ["".join([part[0].upper() for part in name.split()]) for name in names]
print(initials)