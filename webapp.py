'''
codegloo@gmail.com
'''
import os
import web
import time
import tempfile
from random import sample, randrange
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
from settings import db, render, setup_session
    
urls = (
    '/', 'index',
    '/(\d+)',  'view',
    '/(\d+)/copy', 'copy',
    '/about', 'about',   
)

def now_time():
    now = time.localtime(time.time())
    return time.strftime("%Y-%m-%d %H:%M:%S %Z", now)

def pygmentize(source, syntax):
    lexer = get_lexer_by_name(syntax, stripall=True)
    formatter = HtmlFormatter(linenos=True, cssclass="syntax")
    return highlight(source, lexer, formatter)
    
class about:
    def GET(self):
        return render.about()

class index:
    def GET(self):
        print "SESSION : ", dir(session)
        name = session.get('name', '')
        title = session.get('title', '')
        return render.index(src=None,title=title,name=name,cache=False)

    def POST(self):
        i = web.input()
        #store values in session as "remember me"
        session.name = i.name
        session.title = i.title
        session.name = i.name
        syntax = i.syntax.lower()
        if not syntax: syntax = 'text'
        html = pygmentize(i.source, syntax)
        n = db.insert('pastes', source=i.source, title=i.title,
            name=i.name, syntax=i.syntax, html=html, created=now_time(),
            ipaddr=web.ctx.env['REMOTE_ADDR'])

        return web.seeother('/%s' % (n,))
    
class view:
    def GET(self, n):
        res = db.select('pastes', where='id=$n', vars=locals())
        db.update('pastes', where='id=$n',vars=locals(), lastview=now_time())
        if res: 
            return render.view(res[0],n)
        else:
            return web.notfound()

class copy:
    def GET(self,n):
        title = session.get('title', '')
        name = session.get('name', '')
        print 'title, name: ', title, name, '<--'
        
        res = db.select('pastes', where='id=$n', vars=locals())
        if res: 
            return render.index(src=res[0].source, title=title, name=name)
        else:
            return web.notfound()
        
        
app = web.application(urls, globals())
setup_session(app)
application = app.wsgifunc()
if __name__ == "__main__": 
    app.run()