#coding:utf-8
import sys,signal
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *

class Render(QWebPage):  
    def __init__(self, url):  
      QWebPage.__init__(self)
      self._url = url
      #self.loadFinished.connect(self._loadFinished)  
      #self.mainFrame().load(QUrl(url))  
      #self.app.exec_() 

    def _save(self):
      signal.signal(signal.SIGINT, signal.SIG_DFL)
      self.connect(self, SIGNAL('loadFinished(bool)'), self._finish_loading)
      print('载入网页..')
      self.mainFrame().load(QUrl(self._url))
    
    def _finish_loading(self, result):
      f = open('./test.html','w')       
      f.write(self.mainFrame().toHtml().toUtf8())
      f.close()
      sys.exit(0)

def saveHTML():
  url = 'http://www.neeq.com.cn/disclosure'

  app = QApplication(sys.argv)
  r = Render(url)
  r._save()
  sys.exit(app.exec_())

if __name__ == '__main__':
	saveHTML()