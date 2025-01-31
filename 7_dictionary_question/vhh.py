emp={
1:{
'name':'vivek',
'address':'pathankot',
'salary':100000

},
2:{
'name':'vive',
'address':'sujanpur',
'salary':70000

},
3:{

'name':'viv',
'address':'punjab',
'salary':40000
}
}
#print(emp)

print(emp)

high_emp = []

for i in emp.values():
    if i['salary'] > 50000:
        high_emp.append(i['name'])

print(high_emp)