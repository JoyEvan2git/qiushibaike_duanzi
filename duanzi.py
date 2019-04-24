from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
import urllib.request
import ssl
import re
list_duanzi = []
i = 0
page = 1
class duanzi(QWidget):
	def __init__(self,parent = None):
		super().__init__(parent)
		self.setWindowTitle("段子")
		self.resize(400,500)
		self.textEdit = QTextEdit()
		self.textEdit.setFont(QFont('SimSun',14,QFont.Bold))
		self.nextOne = QPushButton("下一条")
		self.reLord = QPushButton("看过了")
		layout = QVBoxLayout()
		layout.addWidget(self.textEdit)
		layout.addWidget(self.nextOne)
		layout.addWidget(self.reLord)
		self.setLayout(layout)
		self.nextOne.clicked.connect(self.btnPress1_Clicked)
		self.reLord.clicked.connect(self.btnPress2_Clicked)
		
	def btnPress1_Clicked(self):
		global i
		try:
			self.textEdit.setPlainText(list_duanzi[i])
			i+=1
		except IndexError:
			global page
			url = "https://www.qiushibaike.com/text/page/"+str(page)+"/"
			list_duanzi.clear()
			i = 0
			info = jokeCrawler(url)
			page+=1
	def btnPress2_Clicked(self):
		global page
		url = "https://www.qiushibaike.com/text/page/"+str(page)+"/"
		list_duanzi.clear()
		i = 0
		info = jokeCrawler(url)
		page+=1

def jokeCrawler(url):
    headers = {
        "User-Agent": "Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.9.168 Version/11.50"
    }
    req = urllib.request.Request(url, headers=headers)
    context = ssl._create_unverified_context()
    response = urllib.request.urlopen(req, context=context)

    HTML = response.read().decode("utf-8")
    pat = r"<div class=.*?<h2>(.*?)</h2>.*?<span>(.*?)</span>"
    pat_xiu = re.compile(pat, re.S)

    s = pat_xiu.findall(HTML)
    for i in s:
        h = i[1]
        h = h.replace('<br/>','')
        h = h.strip()
        list_duanzi.append(h)


if __name__ == "__main__":
	app = QApplication(sys.argv)
	win = duanzi()
	qssStyle = """
		QPushButton{
			background-color:gray
		}
	"""
	win.setStyleSheet(qssStyle)
	win.show()
	sys.exit(app.exec_())
		