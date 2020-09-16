#!/usr/bin/env python3

import htpasswd
import json

setting = json.load(open("setting.json"))

with htpasswd.Basic(".htpasswd") as userdb:
    for i in range(10000, 11000):
        userdb.add("{0}".format(i), setting["passwd"])
    userdb.add("jscc", setting["passwd"])
