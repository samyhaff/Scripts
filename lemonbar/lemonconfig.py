#!/usr/bin/python3

def module():
    return "Hello, World!"

print("%{r}" + module() + "%{l}1 2 3")

# bspc query -D -d .occupied --names
# bspc query -D -d focused --names
