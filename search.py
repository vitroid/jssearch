#!/usr/bin/env python3
#結局使わない予定

import cherrypy
import re
import time
from cherrypy.lib.static import serve_file
import os

class Index(object):
    @cherrypy.expose
    def index(self):
        cherrypy.response.headers['Content-Type']
        cookie = cherrypy.request.cookie # share cookie with reg2
        # validate the cookie here!!!
        if "sess" in cookie:
            return serve_file(os.getcwd()+"/index", content_type='text/plain')
        return "var data=[];"


class Search(object):
    @cherrypy.expose
    def index(self):
        cookie = cherrypy.request.cookie # share cookie with reg2
        if "sess" in cookie:
            with open("index.html") as f:
                return f.read()
        return "No access."

    @cherrypy.expose
    def setCookie(self):
        cookie = cherrypy.response.cookie
        cookie['cookieName'] = 'cookieValue'
        cookie['cookieName']['path'] = '/'
        cookie['cookieName']['max-age'] = 3600
        cookie['cookieName']['version'] = 1
        return "<html><body>Hello, I just sent you a cookie</body></html>"

    @cherrypy.expose
    def readCookie(self):
        cookie = cherrypy.request.cookie
        res = """<html><body>Hi, you sent me %s cookies.<br />
                Here is a list of cookie names/values:<br />""" % len(cookie)
        for name in cookie.keys():
            res += "name: %s, value: %s<br>" % (name, cookie[name].value)
        return res + "</body></html>"


class Root(object):
    @cherrypy.expose
    def index(self):
        host = cherrypy.request.headers['Host']
        return "You have successfully reached " + host


root = Root()
root.search = Search()
root.index  = Index()

conf = {
    'global': {
        'server.socket_host': '0.0.0.0',
        'server.socket_port': 8000,
    },
    "/tn" : {
           "tools.staticdir.on"    : True,
           "tools.staticdir.dir"   : os.getcwd()+"/tn",
       },
}
cherrypy.quickstart(root, '/', conf)


  * {
  padding: 0px
;
  margin:  0px;
  }
  body{
  font-family: Helvetica, Ariel, sans-serif;
  font-size: 10pt;
}
div.wrap{
  max-width: 750px;
  background-color:#f0f0f0;
  margin: 0 auto; //centering
}
td{
  margin:0;
  /*padding:0 0 1em 0.5em; modified by mm*/
  padding:0;
}
table tr.r:nth-child(odd){
  background-color: #e0e0e0;
}

@media screen and (min-width: 550px) {
  table tr.r{
    display: flex;           /* flexコンテナ化 */
    flex-direction: row;
    justify-content: flex-start;
  }
}

@media screen and (max-width: 550px) {
  tr.r {
    display: flex;
    flex-direction: column-reverse;
  align-items: center;
}
td.i { justify-content: center; }
}
table tr.r{
  margin: 0px;
  padding:0 0 0.5em 0em;
}
span.l{
	font-size:150%;
	font-weight:bold;
}
div.m{
  color: #808080;
  background-color: #fff;
}
td.ti, span.ti{
	font-weight:bold;
}
td b{
	color:#666600;
	background-color:#ffffdd;
	font-weight:bold;
	border:1px solid #bbbb00;
	margin:0 2px 0 2px;
	padding:0 2px 0 2px;
}

div.ttpanel {
  display: flex;
  flex-wrap: wrap;
}
th.row {
  width: 64px;
  background-color: #fff;
}
th.right {
  font-size: 80%;
  vertical-align: top;
  background-color: #fff;
}
th.corner {
  width: 64px;
  font-size: 150%;
  padding: 10px 10px 0;
}
td.row, th.col {
  padding: 2px 2px 0;
  width: 22px;
}
tr.header{
  background-color: #fff;
}
tr.row{
  background-color: #888;
  height: 25px;
}
[type="checkbox"]{
  width: 1.75em;
  height: 1.75em;
}


#navi{
	margin:0.5rem 0;
	line-height:2rem;
}
#navi span{
	border-top:1px solid #d8d8d8;
	border-bottom:1px solid #d8d8d8;
	padding: 0.33rem 0.66rem;
	cursor:pointer;
	word-wrap:break-word;
}
#navi span.selected{
	background: #D3EDF7;
}
#navi span:first-child{
	border-left:1px solid #d8d8d8;
	border-top-left-radius: 0.4rem;
	border-bottom-left-radius: 0.4rem;
}
#navi span:last-child{
	border-right:1px solid #d8d8d8;
	border-top-right-radius: 0.4rem;
	border-bottom-right-radius: 0.4rem;
}

#searchbox input{
	font-size: 0.8rem;
	padding: 0.25rem;
	margin-bottom: 0.2rem;
}
@media (max-width: 15em) {
	#navi{
		width:300px;
	}
}

/* tabs using CSS https://bagelee.com/design/css/create_tabs_using_only_css/ */

/*タブ切り替え全体のスタイル*/
.tabs {
  margin-top: 50px;
  padding-bottom: 40px;
  background-color: #fff;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
  max-width: 700px;
  margin: 0 auto;}

.tab_item:hover {
  opacity: 0.75;
}

/*ラジオボタンを全て消す*/
input[name="tab_item"] {
  display: none;
}

/*タブ切り替えの中身のスタイル*/
.tab_content {
  display: none;
  padding: 10px 10px 0;
  clear: both;
  overflow: hidden;
}
