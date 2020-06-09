name="Scumble"
tem=""
t=name.find(',')
print(t)
tem1=(name[t+1:]).strip()
tem2=(name[0:t]).strip()
tem=tem1+' '+tem2
print(tem)



