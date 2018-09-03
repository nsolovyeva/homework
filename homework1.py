
# coding: utf-8

# In[1]:


long_phrase = 'Насколько проще было бы писать программы, если бы не заказчики'


# In[2]:


short_phrase = '640Кб должно хватить для любых задач. Билл Гейтс (по легенде)'


# In[3]:


len(long_phrase) > len(short_phrase)


# In[4]:


text = 'Если программист в 9-00 утра на работе, значит, он там и ночевал'


# In[44]:


a = 0
i = 0
for k in range (len(text)):
    if text[k]=='а':
        a+=1
    if text[k]=='и':
        i+=1
if a>i:
    print ('A встречается чаще')
if i>a:
    print ('И встречается чаще')
if a==i:
    print ('Число вхождений букв A и И в строку одинаково')


# In[45]:


FileInBytes = 5987654
FileInMegaBytes=FileInBytes/1024/1024
result=f'Объем файла равен ({FileInMegaBytes: .2f}) Mb'
result


# In[46]:


import math
math.sin(30)


# In[47]:


a=0.1+0.2
a
# в двоичной системе 0.1 - это бесконечная дробь


# In[48]:


a = 3
b = 5
a, b


# In[49]:


a = a + b 
b = a - b 
a = a - b

a, b


# In[50]:


num = '10011'
dec = 0
pos = 0
for i in range(len(num)):
    pos = len(num)-i-1
    dec += int(num[i])*2**pos
dec

