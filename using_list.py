#!/usr/bin/python
#Filename:using_list.py

#This is the shopping list

shoplist = ['apple','mango','carrot','banana']

print 'I have',len(shoplist),'items to purchase'
print 'These item arr',#continue the line
for item in shoplist:
	print item,
print'\nI also have to buy rice'
shoplist.append('rice')
print'My shopping list now',shoplist

print 'I will sort my list now'
shoplist.sort()
print'Sorted shopping list is ',shoplist
print 'the first item I will buy is',shoplist[0]
olditem = shoplist[0]
del shoplist[0]
print 'I bought the ',olditem
print 'My shopping list is now',shoplist
