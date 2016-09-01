#!/usr/bin/env bash

function run_pitchpx () {
    echo "pitchpx -s $1$201 -e $1$231 -o ./output/$1"
    # pitchpx -s "$1$201" -e "$1$231" -o "./output/$1"
}

for (( y=2015; $y < 2017 ; ++y )); do
    mkdir "./output/$y"
    for (( month=3; $month < 12 ; ++month )); do
        m=$(printf %02d $month);
        run_pitchpx $y $m
    done
done
