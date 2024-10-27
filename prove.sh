#!/bin/bash

zokrates compile -i root.zok
zokrates setup
zokrates compute-witness -a 1234 4 2147483648 0 0 0 0 0 0 0 0 0 0 0 0 64 81901710 109647963 216693224 115931701 88406647 57595314 149727287 14904565
zokrates generate-proof
zokrates verify