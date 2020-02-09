import json

data={}
data['people']=[]
item1={'name':'Phuong','web':'csc.edu.vn','from':'TTTH'}
data['people'].append(item1)
item2={'name':'Phuong2','web':'csc2.edu.vn','from':'TTTH2'}
data['people'].append(item2)
item3={'name':'Phuong3','web':'csc3.edu.vn','from':'TTTH3'}
data['people'].append(item3)
item4={'name':'Phuong4','web':'csc4.edu.vn','from':'TTTH4'}
data['people'].append(item4)

f = open('files/people.json','w')
json.dump(data,f,indent=4)