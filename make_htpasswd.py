#!/usr/bin/env python3


import htpasswd

with htpasswd.Basic(".htpasswd") as userdb:
    for i in range(10000, 11000):
        userdb.add("{0}".format(i), "saku2020tou")
    userdb.add("jscc", "saku2020tou")
