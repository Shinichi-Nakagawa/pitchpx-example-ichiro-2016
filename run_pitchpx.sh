#!/usr/bin/env bash

function run_pitchpx () {
    pitchpx -s "$10322" -e "$10331" -o "./output/$1"
    pitchpx -s "$10401" -e "$10430" -o "./output/$1"
    pitchpx -s "$10501" -e "$10531" -o "./output/$1"
    pitchpx -s "$10601" -e "$10630" -o "./output/$1"
    pitchpx -s "$10701" -e "$10731" -o "./output/$1"
    pitchpx -s "$10801" -e "$10831" -o "./output/$1"
    pitchpx -s "$10901" -e "$10930" -o "./output/$1"
    pitchpx -s "$11001" -e "$11031" -o "./output/$1"
}

for (( y=2013; $y < 2015 ; ++y )); do
    mkdir -p "./output/$y"
    run_pitchpx $y
done
