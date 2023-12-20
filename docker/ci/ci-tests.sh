#!/usr/bin/env sh
if ! pytest --cov  --create-db;then /usr/games/cowsay -f eyes "!!!!!!!! YOUR TESTS FAILED !!!!!!!!"; exit 1; fi
