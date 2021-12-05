#!/bin/bash
# create directory
mkdir -p $1
# create txt files
touch $1/input_full.txt
git add $1/input_full.txt
touch $1/input_sample.txt
git add $1/input_sample.txt
touch $1/Issue.txt
git add $1/Issue.txt
# create python files
touch $1/part_1.py
git add $1/part_1.py
touch $1/part_2.py
git add $1/part_2.py
# default template py
if [ ! -s $1/part_1.py ]; then
  echo """
def solution():
    pass


if __name__ == \"__main__\":
    # input_file = 'input_sample.txt'
    input_file = 'input_full.txt'

    with open(input_file, 'r') as f:
        for line in f:
            pass
  """ > $1/part_1.py
fi

if [ ! -s $1/part_2.py ]; then
  echo """
def solution():
    pass


if __name__ == \"__main__\":
    # input_file = 'input_sample.txt'
    input_file = 'input_full.txt'

    with open(input_file, 'r') as f:
        for line in f:
            pass
  """ > $1/part_2.py
fi


