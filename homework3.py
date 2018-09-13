
# coding: utf-8

# In[1]:


data = [
[13, 25, 23, 34],
[45, 32, 44, 47],
[12, 33, 23, 95],
[13, 53, 34, 35],
]


# In[4]:


def list_is_square(list):
    if len(list) == len(list[0]):
        return True
    else:
        return False


# In[8]:


def diagonal_sum(list):
    sum=0
    if list_is_square(list):
        for i in range (len(list)):
            sum+=list[i][i]
        print (sum)
    else:
        print ('Wrong list length')
        


# In[9]:


diagonal_sum(data)


# In[10]:


data = [1, '5', 'abc', 20, '2']


# In[14]:


def is_number(s):
    if isinstance(s, str):
        if str.isnumeric(s):
            return True
        else:
            return False
    elif isinstance(s, int):
        return True
    elif isinstance(s, float):
        return True
    else:
        return False


# In[18]:


def sum_squares(data):
    s=0
    if isinstance(data, list):
        for i in range(len(data)):
            if is_number(data[i]):
                if isinstance(data[i], str):
                    s+=float(data[i])**2
                else:
                    s+=data[i]**2
        print (s)
    else:
        print ('Not a list')


# In[19]:


sum_squares(data)


# In[20]:


import requests


# In[58]:


class Rates:
    
    def __init__(self, format, diff):
        self.format = format
        self.diff = diff
    
    def exchange_rates(self):
        r = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
        return r.json()['Valute']
    
    def make_format (self, currency):
        responce = self.exchange_rates()
        
        if currency in responce:
            if self.format == 'full':
                return responce(currency)
            if self.format == 'value':
                if self.diff:
                    return responce[currency]['Value']-responce[currency]['Previous']
                else:
                    return responce[currency]['Value']
            if self.format == 'name':
                return responce[currency]['Name']
    
    def USD(self):
        return self.make_format('USD')
    
    def EUR(self, diff):
        return self.make_format('EUR')
    
    


# In[45]:


rt = Rates('full', False)


# In[46]:


curr = rt.exchange_rates()


# In[49]:


def get_max_rate ():
    rt = Rates('full', False)
    curr = rt.exchange_rates()
    rate = 0

    for c in curr.values():
        if c['Nominal']>rate:
            rate = c['Value']/c['Nominal']
            name = c['Name']
        
    return name


# In[50]:


get_max_rate ()


# In[59]:


rt = Rates('value', True)


# In[60]:


rt.USD()


# In[61]:


def fib(n):
    if n==1 or n==2:
        return 1
    return fib(n-1) + fib(n-2)


# In[64]:


# сумма n чисел Фибоначчи равна n+2 числу - 1
n=10
fib(n+2)-1


# In[12]:


list = ['2018-01-01', 'yandex', 'cpc', 100]


# In[13]:


if len(list)<2:
    print ('List too short')
else:
    *other, last = list
    val = last
    list = other
    *other, last=list
    mydict = {}
    mydict[last]=val
    list = other
    while len(list)>0:
        *other, last=list
        mydict1 = {}
        mydict1[last]=mydict
        mydict = mydict1
        list = other
    print(mydict1)

