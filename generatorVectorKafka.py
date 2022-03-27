'''
Create vector's generator
'''

from time import sleep
from datetime import datetime
from random import random
from kafka import KafkaProducer
import json
import re
import os

producer = KafkaProducer(bootstrap_servers='localhost:9092',
        value_serializer=lambda v: json.dumps(v).encode('utf-8'))

dir_name = 'MyStream'

# Read from csv file

def vector_generators(f_name, limit=5):
    '''
    This generator iterates the (arbitrary) lines of the file Bible.txt
    and yields its verses, as determined by lines beginning with a regex of the
    form [chapter: verse]
    '''
    if limit is None:
        limit = 10**6
    with open(f_name, 'r') as f:
        verse=''
        for i, line in enumerate(f):            # Skip empty lines
            if line=='\n':
                continue
            if limit is not None:               # Keep output limit
                if i>limit:
                    break
                verse = line[:-1]
                yield verse


if not os.path.exists(dir_name):
    os.mkdir(dir_name)

for vector in vector_generators(r'/home/liya/Notebooks/vectors.csv', 200):
    if vector:
        vector_lst = vector.split(",")
        producer.send('vectors', {'id': vector_lst[0], 'student': vector_lst[1], 'school': vector_lst[2], 'class': vector_lst[3], 'vector': vector_lst[4]})
    sleep(random())

