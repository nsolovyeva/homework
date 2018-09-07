
# coding: utf-8

# In[18]:


# В исходном варианте очепятка со скобками
# Первый вариант исправления - список словарей
geo_logs = [
{'visit1': ['Москва', 'Россия']},
{'visit2': ['Дели', 'Индия']},
{'visit3': ['Владимир', 'Россия']},
{'visit4': ['Лиссабон', 'Португалия']},
{'visit5': ['Париж', 'Франция']},
{'visit6': ['Лиссабон', 'Португалия']},
{'visit7': ['Тула', 'Россия']},
{'visit8': ['Тула', 'Россия']},
{'visit9': ['Курск', 'Россия']},
{'visit10': ['Архангельск', 'Россия']},
]
print (geo_logs)


# In[27]:


# Пробовала несколько вариантов решения - и всегда возникает проблема с сокращением длины списка в случае удаления объекта 
# В случае синтаксиса for item in geo_logs при удалении идет пропуск строки в цикле
# Поскольку задача звучит как отфильтровать имебщийся список, а не создать новый с требуемыми значениями - 
# вот такое странное на мой взгляд решение с меняющимся размером цикла.
# В принципе, работает... но обычно так не делаю :)

l=len(geo_logs)
for i in range(0,l):
        item = geo_logs[i]
        for country in item.values():
            if 'Россия' in country:
                geo_logs.remove(item)
                l-=1
            else:
                i+=1
print (geo_logs)
           


# In[47]:


# Второй вариант исправления - словарь со списком в качестве значения
geo_logs = {
'visit1': ['Москва', 'Россия'],
'visit2': ['Дели', 'Индия'],
'visit3': ['Владимир', 'Россия'],
'visit4': ['Лиссабон', 'Португалия'],
'visit5': ['Париж', 'Франция'],
'visit6': ['Лиссабон', 'Португалия'],
'visit7': ['Тула', 'Россия'],
'visit8': ['Тула', 'Россия'],
'visit9': ['Курск', 'Россия'],
'visit10': ['Архангельск', 'Россия'],
}


# In[52]:


# Опять невозможно одновременно двигаться по словарю и сокращать его. Поэтому по сути 2 цикла

key_list=[key for key, country in geo_logs.items() if 'Россия' in country]

for key in key_list:
    del geo_logs[key]

print (geo_logs)


# In[53]:


ids = {'user1': [213, 213, 213, 15, 213], 'user2': [54, 54, 119, 119, 119], 'user3': [213, 98, 98, 35]}


# In[54]:


# А есть решение без вложенного цикла?
unique=[]
for values in ids.values():
    for num in values:
        if not num in unique:
            unique.append(num)
print (unique)


# In[55]:


queries = [
'смотреть сериалы онлайн',
'новости спорта',
'афиша кино',
'курс доллара',
'сериалы этим летом',
'курс по питону',
'сериалы про спорт',
]


# In[65]:


total_number_of_queries = len(queries)
percent={}
for query in queries:
    if len(query.replace(' ',''))>0:
        words=len(query)-len(query.replace(' ',''))+1
    else:
        words=0
    percent[words] = percent[words]+1 if words in percent else 1
for key in percent.keys():
    percent[key] = float("{0:.2f}".format(percent[key]/total_number_of_queries *100))
print (percent)


# In[66]:


stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}


# In[71]:


max_social = max(stats, key=lambda i: stats[i])
print (max_social, stats[max_social])


# In[72]:


stream = [
'2018-01-01,user1,3',
'2018-01-07,user1,4',
'2018-03-29,user1,1',
'2018-04-04,user1,13',
'2018-01-05,user2,7',
'2018-06-14,user3,4',
'2018-07-02,user3,10',
'2018-03-21,user4,19',
'2018-03-22,user4,4',
'2018-04-22,user4,8',
'2018-05-03,user4,9',
'2018-05-11,user4,11',
]


# In[78]:


unique = []
visits = 0
for string in stream:
    line = string.split(',')
    visits+=int(line[2])
    if line[1] not in unique:
        unique.append(line[1])
print (float("{0:.2f}".format(visits/len(unique))))


# In[79]:


stats = [
['2018-01-01', 'google', 25],
['2018-01-01', 'yandex', 65],
['2018-01-01', 'market', 89],
['2018-01-02', 'google', 574],
['2018-01-02', 'yandex', 249],
['2018-01-02', 'market', 994],
['2018-01-03', 'google', 1843],
['2018-01-03', 'yandex', 1327],
['2018-01-03', 'market', 1764],
]


# In[81]:


a = [line[2] for line in stats if line[0]=='2018-01-01' and line[1] == 'yandex']
print (a)


# In[94]:


# Обобщенный вариант
lookup_set=['2018-01-02', 'yandex']
for line in stats:
    *other, last=line
    if other == lookup_set:
        print(last)

