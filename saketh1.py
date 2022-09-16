L=["bulbasar_21","coocoo_54","squirtle_42","charmander_09","graoden_69","seviper_68","pavas_00","greninja_07","gengar_77","mew_11","rocky_12","onix_99","raichu_22","hike_23","palkia_27","charlizard_43"]
for L in L:
    print(L[-4::-1])
L=["bulbasar_21","coocoo_54","squirtle_142","charmander_09","graoden_69","seviper_68","pavas_00","greninja_07","gengar_77","mew_11","rocky_12","onix_99","raichu_22","hike_23","palkia_27","charlizard_43"]
for L in L[::-1]:
    print(L[-4::-1])
if L is "squirtle_142":
  print(L[5::1])
else:
 print(L[4::1])
L=["bulbasar_21","coocoo_54","squirtle_42","charmander_09","graoden_69","seviper_68","pavas_00","greninja_07","gengar_77","mew_11","rocky_12","onix_99","raichu_22","hike_23","palkia_27","charlizard_43"]
for i in L[::2]:
 k=i.find('_')
 print(i[:k])
for L in L:
 if L[0]=='g':
  print(L[:-3])
for i in L:
 k=i.startswith("g")
if k==True:
 L= i.find('_')
 print(i[:L])
L2=["saketh_44","shiva_22"]
for i in L[::2]:
 L2.append(i)
 print(L2)
L2=[]
for i in L[::2]:
 L2.append(i)
print(L2)
