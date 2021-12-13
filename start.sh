#! /bin/bash

YEAR=$1
DAY=$2
COOKIE=$(cat ./cookies.txt)
OUTPUT_FILE="$YEAR/$DAY/input"
PART_1="$YEAR/$DAY/01.py"
PART_2="$YEAR/$DAY/02.py"
PY_STARTER="./starter.py"

mkdir $YEAR/$DAY

curl -L -b $COOKIE "https://adventofcode.com/$YEAR/day/$DAY/input" -o $OUTPUT_FILE

cp $PY_STARTER $PART_1
cp $PY_STARTER $PART_2
code $PART_1