import json

#wap to convert  JSON data to python object
# a='{"name":"sourav","age":25,"course":"python"}'
# print(type(a))
# b=json.loads(a)
# print(b)
# print(type(b))

#wap to convert python objects to JSON data
# x={"name":"sourav","age":25,"course":"python"}
# print(type(x))
# y=json.dumps(x)
# print(y)
# print(type(y))

#wap to convert python objects in to JSON strings.print all the values
# p_d={"name":"sourav","age":25,"course":"python"}
# p_l=["apple","orange",1,2,3]
# p_T=("car","bus","bike")
# p_s="sourav"
# p_i=124
# p_F=12.6
# p_n=None
# p_t=True
# p_f=False
#
# print("JSON_D =",json.dumps(p_d))
# print("JSON_L =",json.dumps(p_l))
# print("JSON_T =",json.dumps(p_T))
# print("JSON_S =",json.dumps(p_s))
# print("JSON_I =",json.dumps(p_i))
# print("JSON_F =",json.dumps(p_F))
# print("JSON_N =",json.dumps(p_n))
# print("JSON_T =",json.dumps(p_t))
# print("JSON_F =",json.dumps(p_f))


#wap to convert python dictionary object(sor by key) to JSON data.print the object members with Indent level 4
x={"name":"sourav","age":25,"course":"python"}
print(type(x))
y=json.dumps(x,indent=4,sort_keys=True)
print(y)
print(type(y))


#wap to convert JSON encoded data into python objects
# JSON_D='{"item":"bat","rate":4500,"qty":25}'
# JSON_L='["car","bike","lorry"]'
# print(type(JSON_L))
# JSON_S='"python django"'
# JSON_I='856'
# JSON_F='16.20'
# print(type(JSON_F))
# print("P_D =",json.loads(JSON_D))
# print("P_L =",json.loads(JSON_L))
# print(type(json.loads(JSON_L)))
# print("P_S =",json.loads(JSON_S))
# print("P_I =",json.loads(JSON_I))
# print("P_F =",json.loads(JSON_F))
# print(type(json.loads(JSON_F)))
