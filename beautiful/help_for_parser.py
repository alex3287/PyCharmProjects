t = '<a href="/jobs/?page=187">Последняя</a>'
k1=t.find('page=')+5
k2=t.find('Последняя')-2


print(int(t[k1:k2]))