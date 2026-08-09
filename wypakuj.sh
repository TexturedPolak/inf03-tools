#!/bin/bash
plik=$1
haslo=$2
nazwa_pliku=$(basename "$plik")
nazwa_folderu="${plik%.*}"
7z x "$plik" -p"$haslo" -o"$nazwa_folderu"