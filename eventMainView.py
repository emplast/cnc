
from main import Ui_Panel
from PyQt5 import QtCore, QtGui, QtWidgets, QtOpenGL
from glWidget import GlWidget
from workpiceTurning import Ui_viewWorkpiceTurning
# import OpenGL.GL as g
# from OpenGL import GLU
# from PyQt5.QtCore import Qt

class EventMainView(Ui_Panel,Ui_viewWorkpiceTurning,GlWidget):
    diameter=0.0
    lang=0.0
        
    def setupUi(self,Panel):
        super(EventMainView,self).setupUi(Panel)
        super(EventMainView,self).__init__(self.frame)
        
        self.radioButton.clicked.connect(self.radioEvent)
        self.radioButton_2.clicked.connect(self.radioButton_2Event)
        self.radioButton_3.clicked.connect(self.radioButton_3Event)
        self.radioButton_4.clicked.connect(self.radioButton_4Event)
        self.tabWidget_3.currentChanged.connect(self.tabWidgetEvent)
        self.toolButton_37.clicked.connect(self.workpiceTurning)
        self.toolButton_43.clicked.connect(self.ex)

    def radioEvent(self):
        if self.radioButton.isChecked()==True:
            self.tabWidget_3.setCurrentIndex(0)
            self.enabligItems()
    def radioButton_3Event(self):
        if self.radioButton_3.isChecked()==True:
            self.tabWidget_3.setCurrentIndex(1)
            self.enabligItems()
    def radioButton_4Event(self):
        if self.radioButton_4.isChecked()==True:
            self.tabWidget_3.setCurrentIndex(2)
            self.enabligItems()        
    def radioButton_2Event(self):
        if self.radioButton_2.isChecked()==True:
            self.tabWidget_3.setCurrentIndex(3)
            self.enabligItems()
    def enabligItems(self):
            if self.radioButton.isChecked()==True:
                self.tab_8.setEnabled(True)
                self.tabWidget.setEnabled(True)
                self.tab_2.setEnabled(True)
                self.tab_7.setEnabled(True)
                self.tab.setEnabled(True)
                self.groupBox.setEnabled(True)
                self.groupBox_15.setEnabled(True)
             

                self.tab_14.setEnabled(False)
                self.tabWidget_6.setEnabled(False)
                self.tab_18.setEnabled(False)
                self.tab_19.setEnabled(False)
                self.tab_20.setEnabled(False)
                self.groupBox_46.setEnabled(False)
                self.tab_9.setEnabled(False)
                self.tabWidget_4.setEnabled(False)
                self.tab_10.setEnabled(False)
                self.tab_11.setEnabled(False)
                self.tab_12.setEnabled(False)
                self.groupBox_23.setEnabled(False)
                self.tab_13.setEnabled(False)
                self.tabWidget_5.setEnabled(False)
                self.tab_15.setEnabled(False)
                self.tab_16.setEnabled(False)
                self.tab_17.setEnabled(False)
                self.groupBox_33.setEnabled(False)
            if self.radioButton_2.isChecked()==True:
                self.tab_14.setEnabled(True)
                self.tabWidget_6.setEnabled(True)
                self.tab_18.setEnabled(True)
                self.tab_19.setEnabled(True)
                self.tab_20.setEnabled(True)
                self.groupBox_46.setEnabled(True)

                self.tab_8.setEnabled(False)
                self.tabWidget.setEnabled(False)
                self.tab_2.setEnabled(False)
                self.tab_7.setEnabled(False)
                self.tab.setEnabled(False)
                self.groupBox.setEnabled(False)
                self.groupBox_15.setEnabled(False)
                self.tab_9.setEnabled(False)
                self.tabWidget_4.setEnabled(False)
                self.tab_10.setEnabled(False)
                self.tab_11.setEnabled(False)
                self.tab_12.setEnabled(False)
                self.groupBox_23.setEnabled(False)
                self.tab_13.setEnabled(False)
                self.tabWidget_5.setEnabled(False)
                self.tab_15.setEnabled(False)
                self.tab_16.setEnabled(False)
                self.tab_17.setEnabled(False)
                self.groupBox_33.setEnabled(False)
            if self.radioButton_3.isChecked()==True:
                self.tab_9.setEnabled(True)
                self.tabWidget_4.setEnabled(True)
                self.tab_10.setEnabled(True)
                self.tab_11.setEnabled(True)
                self.tab_12.setEnabled(True)
                self.groupBox_23.setEnabled(True)

                self.tab_14.setEnabled(False)
                self.tabWidget_6.setEnabled(False)
                self.tab_18.setEnabled(False)
                self.tab_19.setEnabled(False)
                self.tab_20.setEnabled(False)
                self.groupBox_46.setEnabled(False)
                self.tab_8.setEnabled(False)
                self.tabWidget.setEnabled(False)
                self.tab_2.setEnabled(False)
                self.tab_7.setEnabled(False)
                self.tab.setEnabled(False)
                self.groupBox.setEnabled(False)
                self.groupBox_15.setEnabled(False)
                self.tab_13.setEnabled(False)
                self.tabWidget_5.setEnabled(False)
                self.tab_15.setEnabled(False)
                self.tab_16.setEnabled(False)
                self.tab_17.setEnabled(False)
                self.groupBox_33.setEnabled(False)
            if self.radioButton_4.isChecked()==True:
                self.tab_13.setEnabled(True)
                self.tabWidget_5.setEnabled(True)
                self.tab_15.setEnabled(True)
                self.tab_16.setEnabled(True)
                self.tab_17.setEnabled(True)
                self.groupBox_33.setEnabled(True)

                self.tab_14.setEnabled(False)
                self.tabWidget_6.setEnabled(False)
                self.tab_18.setEnabled(False)
                self.tab_19.setEnabled(False)
                self.tab_20.setEnabled(False)
                self.groupBox_46.setEnabled(False)
                self.tab_8.setEnabled(False)
                self.tabWidget.setEnabled(False)
                self.tab_2.setEnabled(False)
                self.tab_7.setEnabled(False)
                self.tab.setEnabled(False)
                self.groupBox.setEnabled(False)
                self.groupBox_15.setEnabled(False)
                self.tab_9.setEnabled(False)
                self.tabWidget_4.setEnabled(False)
                self.tab_10.setEnabled(False)
                self.tab_11.setEnabled(False)
                self.tab_12.setEnabled(False)
                self.groupBox_23.setEnabled(False)
                                        
    def tabWidgetEvent(self):
        if self.tabWidget_3.currentIndex()==0:
            self.enabligItems()
        elif self.tabWidget_3.currentIndex()==1:
            self.enabligItems()
        elif self.tabWidget_3.currentIndex()==2:
            self.enabligItems()
        elif self.tabWidget_3.currentIndex()==3:
            self.enabligItems()        
    
    def workpiceTurning(self):
        self.viewWorpice=QtWidgets.QMainWindow()
        self.ui_viewWorkpice=Ui_viewWorkpiceTurning()
        self.ui_viewWorkpice.setupUi(self.viewWorpice)
        self.viewWorpice.show()
        self.ui_viewWorkpice.buttonBox.accepted.connect(self.worpiceDraw)
    def worpiceDraw(self):
        self.diameter=float(self.ui_viewWorkpice.lineEdit.text())
        self.lang=float(self.ui_viewWorkpice.lineEdit_2.text())
        self.paintGL()
        self.viewWorpice.close()

    def paintGL(self):
        self.drawHandle(15)
        self.drawAxisXZ(self.lang,self.diameter/-2,0.0)
        self.drawG54(self.lang,self.diameter/-2,0.0,2.0,1.0,(0,255,0,255))
        self.drawWorkpice(self.diameter,self.lang,0.0)
    def wheelEvent(self,e):
        if e.angleDelta().y()/120==1.0:
            self.zoom+=0.1
        if e.angleDelta().y()/120==-1.0:
            self.zoom-=0.1
        # print(self.zoom)       
    pass
    def ex(self):
        self.uiGl=GlWidget(self.frame)
        self.uiGl.initializeGL()
        print("ok")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Panel = QtWidgets.QMainWindow()
    ui=EventMainView()
    ui.setupUi(Panel)
    Panel.show()
    sys.exit(app.exec_())

