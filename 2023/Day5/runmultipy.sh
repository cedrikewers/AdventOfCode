#!/bin/bash
for i in {0..15} 
do
    python3 multipy.py $i &
done