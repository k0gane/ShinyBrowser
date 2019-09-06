"""
ZetCode PyQt5 tutorial 

This program creates a skeleton of
a classic GUI application with a menubar,
toolbar, statusbar, and a central widget. 

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QApplication, QWidget, QLabel, QLineEdit, QGridLayout, QPushButton, QDesktopWidget, qApp, QMenu
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

class Example(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('メニュー')
        
        impMenu = QMenu('アクション', self)
        impAct1 = QAction('メイン画面へ', self) 
        impMenu.addAction(impAct1)
        impAct2 = QAction('フェス画面へ', self) 
        impMenu.addAction(impAct2)
        impAct3 = QAction('新規登録', self)
        impMenu.addAction(impAct3)
     
        fileMenu.addMenu(impMenu)               
        
        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)

        backAct = QAction(QIcon("back.png"), '戻る', self)
        backAct.setShortcut('Ctrl+Z')
        backAct.setStatusTip('ページを戻します')
        backAct.triggered.connect(self.close)

        nextAct = QAction(QIcon("next.png"), '進む', self)
        nextAct.setShortcut('Ctrl+X')
        nextAct.setStatusTip('ページを進めます')
        nextAct.triggered.connect(self.close)

        refreshAct = QAction(QIcon("refresh.png"), '更新', self)
        refreshAct.setShortcut('F5')
        refreshAct.setStatusTip('ページを更新します')
        refreshAct.triggered.connect(self.close)

        exitAct = QAction(QIcon("refresh.png"), '閉じる', self)
        exitAct.setShortcut('Ctrl+Alt+Del')
        exitAct.setStatusTip('ページを閉じます')
        exitAct.triggered.connect(self.close) 

        self.statusBar()

        fileMenu.addAction(backAct)
        fileMenu.addAction(nextAct)
        fileMenu.addAction(exitAct)

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(backAct)
        toolbar.addAction(nextAct)
        toolbar.addAction(refreshAct)

        initurl = 'https://www.google.co.jp'
        self.browser = QWebEngineView()
        self.browser.load(QUrl(initurl))   
        self.setCentralWidget(self.browser)      
        self.setGeometry(200, 200, 1280, 720)
        self.setWindowTitle('ShinyBrowser')    
        self.show()
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)


    ex = Example()
    sys.exit(app.exec_())