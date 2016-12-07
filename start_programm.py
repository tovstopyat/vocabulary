# start_programm.py
#http://www.pythontutor.com/visualize.html#mode=edit
#!/usr/bin/env python
# -*- coding:utf-8 -*-

import shelve
db=shelve.open('db_file')


def eng():
    eng_words=dict([[v, k] for k,v in db.items()])
    find_word=input('Enter word ' '')
    print(eng_words.get(find_word))

def ua():
    key = "keyinput('enter word''')"
    print (db.get(key) or 'no find word')

def newRecord():
    newkey=input('enter new word ' '')
    newvalue=input('enter translate''')
    db[newkey] = newvalue
    db.update()
    db.close()


if __name__ == '__main__':
    start=input('find word, enter "k" or "v"' '' )
    if start == 'k':
        eng()
    if start == 'v':
        ua()
