#!/usr/bin/env python
import cherrypy
import sys

pidfile = None
if len(sys.argv) > 1 and sys.argv[1] == "-p":
    pidfile = sys.argv[2]

class Root(object):
    @cherrypy.expose
    def index(self):
        return open("./index.html", 'r').read()

if __name__ == '__main__':
    cherrypy.server.socket_port = 8087
    cherrypy.server.socket_host = "0.0.0.0"

    root_conf = {
        "/" : {
                  "tools.staticdir.on"    : True,
                  "tools.staticdir.dir"   : "/Users/matto/GoogleDrive/gitwork/jssearch",
                  "tools.staticdir.index" : "index.html",
              },
        "/tn" : {
                  "tools.staticdir.on"    : True,
                  "tools.staticdir.dir"   : "/Users/matto/GoogleDrive/gitwork/jssearch/tn",
              },
        "/pdf" : {
                  "tools.staticdir.on"    : True,
                  "tools.staticdir.dir"   : "/Users/matto/GoogleDrive/gitwork/jssearch/pdf",
              },
        "/index.js" : {
                  "tools.staticfile.on"    : True,
                  "tools.staticfile.filename" : "/Users/matto//GoogleDrive/gitwork/jssearch/index.js",
              }
    }
    cherrypy.quickstart(Root(), "/", root_conf)
