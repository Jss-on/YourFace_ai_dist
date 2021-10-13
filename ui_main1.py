# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main1WSJcTP.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import backgnd_rc
from control import *
import numpy as np

#import cv2
import sys
#ui_ids = {}

# ID's for each widgets
# dirname = os.path.dirname(PySide2.__file__)
# plugin_path = os.path.join(dirname, 'plugins', 'platforms')
# os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(985, 686)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(985, 686))
        MainWindow.setMaximumSize(QSize(985, 686))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("")
        self.main_frame = QFrame(self.centralwidget)
        self.main_frame.setObjectName("main_frame")
        self.main_frame.setGeometry(QRect(0, 0, 981, 691))
        self.main_frame.setStyleSheet(
            "background-color: rgb(255, 255, 255);;\n" "\n" ""
        )
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.main_title_name = QLabel(self.main_frame)
        self.main_title_name.setObjectName("main_title_name")
        self.main_title_name.setGeometry(QRect(0, 0, 981, 181))
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(40)
        self.main_title_name.setFont(font)
        self.main_title_name.setStyleSheet("color: rgb(2, 48, 38);")
        self.main_title_name.setAlignment(Qt.AlignCenter)
        self.enrolface_but = QPushButton(self.main_frame)
        self.enrolface_but.setObjectName("enrolface_but")
        self.enrolface_but.setGeometry(QRect(70, 320, 291, 61))
        font1 = QFont()
        font1.setFamily("Arial")
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(50)
        font1.setStrikeOut(False)

        self.enrolface_but.setFont(font1)
        self.enrolface_but.setStyleSheet(
            """QPushButton:hover{
	
	
	
	background-color: rgb(255, 170, 0);
	
	color: rgb(0, 0, 0);
	
	font: 75 13pt "Arial";
}

QPushButton{
	background-color: rgb(2, 48, 38);
	font: 12pt "Arial";
	color: rgb(255, 255, 255);
}"""
        )
        self.startrecog_but = QPushButton(self.main_frame)
        self.startrecog_but.setObjectName("startrecog_but")
        self.startrecog_but.setGeometry(QRect(610, 320, 281, 61))
        self.startrecog_but.setStyleSheet(
            """QPushButton:hover{
	
	
	
	background-color: rgb(255, 170, 0);
	
	color: rgb(0, 0, 0);
	
	font: 75 13pt "Arial";
}

QPushButton{
	background-color: rgb(2, 48, 38);
	font: 12pt "Arial";
	color: rgb(255, 255, 255);
}"""
        )
        self.add_user_frame = QFrame(self.centralwidget)
        self.add_user_frame.setObjectName("add_user_frame")
        self.add_user_frame.setGeometry(QRect(-1, -1, 981, 691))
        self.add_user_frame.setStyleSheet(
            "background-color: rgb(255, 255, 255);"
        )
        self.add_user_frame.setFrameShape(QFrame.StyledPanel)
        self.add_user_frame.setFrameShadow(QFrame.Raised)
        self.widget = QWidget(self.add_user_frame)
        self.widget.setObjectName("widget")
        self.widget.setGeometry(QRect(10, 70, 201, 611))
        self.uploadface_but_2 = QPushButton(self.widget)
        self.uploadface_but_2.setObjectName("uploadface_but_2")
        self.uploadface_but_2.setGeometry(QRect(10, 40, 191, 71))
        self.uploadface_but_2.setStyleSheet(
            """QPushButton:hover{
	
	
	
	background-color: rgb(255, 170, 0);
	
	color: rgb(0, 0, 0);
	
	font: 75 13pt "Arial";
}

QPushButton{
	background-color: rgb(2, 48, 38);
	font: 12pt "Arial";
	color: rgb(255, 255, 255);
}"""
        )
        
        self.back_but_3 = QPushButton(self.widget)
        self.back_but_3.setObjectName("back_but_3")
        self.back_but_3.setGeometry(QRect(20, 520, 171, 61))
        self.back_but_3.setStyleSheet(
            """QPushButton:hover{
	
	
	
	background-color: rgb(255, 170, 0);
	
	color: rgb(0, 0, 0);
	
	font: 75 13pt "Arial";
}

QPushButton{
	background-color: rgb(2, 48, 38);
	font: 12pt "Arial";
	color: rgb(255, 255, 255);
}"""
        )
        self.deleteface_but_2 = QPushButton(self.widget)
        self.deleteface_but_2.setObjectName("deleteface_but_2")
        self.deleteface_but_2.setGeometry(QRect(10, 200, 181, 71))
        self.deleteface_but_2.setStyleSheet(
            """QPushButton:hover{
	
	
	
	background-color: rgb(255, 170, 0);
	
	color: rgb(0, 0, 0);
	
	font: 75 13pt "Arial";
}

QPushButton{
	background-color: rgb(2, 48, 38);
	font: 12pt "Arial";
	color: rgb(255, 255, 255);
}"""
        )
        self.display_data_but = QPushButton(self.widget)
        self.display_data_but.setObjectName(u"display_data_but")
        self.display_data_but.setGeometry(QRect(10, 360, 181, 71))
        self.display_data_but.setStyleSheet("""QPushButton:hover{
	
	
	
	background-color: rgb(255, 170, 0);
	
	color: rgb(0, 0, 0);
	
	font: 75 13pt "Arial";
}

QPushButton{
	background-color: rgb(2, 48, 38);
	font: 12pt "Arial";
	color: rgb(255, 255, 255);
}""")
        self.widget_2 = QWidget(self.add_user_frame)
        self.widget_2.setObjectName("widget_2")
        self.widget_2.setGeometry(QRect(220, 70, 771, 621))
        self.listView = QListWidget(self.widget_2)
        self.listView.setObjectName(u"listView")
        self.listView.setGeometry(QRect(150, 10, 491, 581))
        self.listView.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.main_title_name_2 = QLabel(self.add_user_frame)
        self.main_title_name_2.setObjectName("main_title_name_2")
        self.main_title_name_2.setGeometry(QRect(10, 10, 971, 41))
        self.main_title_name_2.setFont(font)
        self.main_title_name_2.setStyleSheet("color: rgb(2, 48, 38);")
        self.main_title_name_2.setAlignment(
            Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter
        )
        self.ai_frame = QFrame(self.centralwidget)
        self.ai_frame.setObjectName(u"ai_frame")
        self.ai_frame.setGeometry(QRect(-1, -1, 981, 691))
        self.ai_frame.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.ai_frame.setFrameShape(QFrame.StyledPanel)
        self.ai_frame.setFrameShadow(QFrame.Raised)
        self.graphicsView = QGraphicsView(self.ai_frame)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(180, 60, 801, 621))
        self.graphicsView.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.frame = QFrame(self.ai_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(9, 79, 161, 581))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.webcam_but_2 = QPushButton(self.frame)
        self.webcam_but_2.setObjectName(u"webcam_but_2")
        self.webcam_but_2.setGeometry(QRect(10, 20, 141, 71))
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(50)
        self.webcam_but_2.setFont(font2)
        self.webcam_but_2.setStyleSheet("""QPushButton:hover{
	
	
	
	background-color: rgb(255, 170, 0);
	
	color: rgb(0, 0, 0);
	
	font: 75 13pt "Arial";
}

QPushButton{
	background-color: rgb(2, 48, 38);
	font: 12pt "Arial";
	color: rgb(255, 255, 255);
}""")
        self.video_but = QPushButton(self.frame)
        self.video_but.setObjectName(u"video_but")
        self.video_but.setGeometry(QRect(20, 160, 121, 71))
        self.video_but.setStyleSheet("""QPushButton:hover{
	
	
	
	background-color: rgb(255, 170, 0);
	
	color: rgb(0, 0, 0);
	
	font: 75 13pt "Arial";
}

QPushButton{
	background-color: rgb(2, 48, 38);
	font: 12pt "Arial";
	color: rgb(255, 255, 255);
}""")
        self.ai_back_but = QPushButton(self.frame)
        self.ai_back_but.setObjectName(u"ai_back_but")
        self.ai_back_but.setGeometry(QRect(20, 460, 121, 71))
        self.ai_back_but.setStyleSheet("""QPushButton:hover{
	
	
	
	background-color: rgb(255, 170, 0);
	
	color: rgb(0, 0, 0);
	
	font: 75 13pt "Arial";
}

QPushButton{
	background-color: rgb(2, 48, 38);
	font: 12pt "Arial";
	color: rgb(255, 255, 255);
}""")
        self.frame_2 = QFrame(self.ai_frame)
        self.frame_2.setObjectName("frame_2")
        self.frame_2.setGeometry(QRect(0, 0, 981, 51))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.main_title_name_3 = QLabel(self.frame_2)
        self.main_title_name_3.setObjectName("main_title_name_3")
        self.main_title_name_3.setGeometry(QRect(10, 0, 971, 51))
        self.main_title_name_3.setFont(font)
        self.main_title_name_3.setStyleSheet("color: rgb(2, 48, 38);")
        self.main_title_name_3.setAlignment(
            Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter
        )
        self.frame_for_video = QFrame(self.ai_frame)
        self.frame_for_video.setObjectName(u"frame_for_video")
        self.frame_for_video.setGeometry(QRect(230, 70, 731, 611))
        self.frame_for_video.setFrameShape(QFrame.StyledPanel)
        self.frame_for_video.setFrameShadow(QFrame.Raised)

        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName("frame_4")
        self.frame_4.setGeometry(QRect(9, 9, 971, 671))
        self.frame_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.widget_4 = QWidget(self.frame_4)
        self.widget_4.setObjectName("widget_4")
        self.widget_4.setGeometry(QRect(60, 110, 871, 131))
        self.widget_4.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.label_3 = QLabel(self.widget_4)
        self.label_3.setObjectName("label_3")
        self.label_3.setGeometry(QRect(6, 10, 861, 151))
        font3 = QFont()
        font3.setPointSize(40)
        self.label_3.setFont(font3)
        self.widget_5 = QWidget(self.frame_4)
        self.widget_5.setObjectName("widget_5")
        self.widget_5.setGeometry(QRect(80, 400, 231, 161))
        self.widget_5.setStyleSheet("background-color: rgb(170, 0, 255);")
        self.label_4 = QLabel(self.widget_5)
        self.label_4.setObjectName("label_4")
        self.label_4.setGeometry(QRect(80, 80, 47, 14))
        self.frame_3 = QFrame(self.frame_4)
        self.frame_3.setObjectName("frame_3")
        self.frame_3.setGeometry(QRect(30, 250, 901, 141))
        self.frame_3.setStyleSheet("background-color: rgb(0, 85, 0);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame_3)
        self.label.setObjectName("label")
        self.label.setGeometry(QRect(10, 0, 241, 141))
        self.label.setFont(font3)
        self.frame_5 = QFrame(self.centralwidget)
        self.frame_5.setObjectName("frame_5")
        self.frame_5.setGeometry(QRect(9, 9, 971, 671))
        self.frame_5.setStyleSheet("")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        
        MainWindow.setCentralWidget(self.centralwidget)

        # controller for windows
        #self.enrolface_but.pressed.connect(self.add_user_page)

        self.frame_5.raise_()
        self.frame_4.raise_()
        # self.add_user_frame.raise_()
        # self.ai_frame.raise_()
        self.main_frame.raise_()

        self.retranslateUi(MainWindow)
        

        QMetaObject.connectSlotsByName(MainWindow)
        self.handleEvent(MainWindow)
    # setupUi
    


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "MainWindow", None)
        )
        self.main_title_name.setText(
            QCoreApplication.translate(
                "MainWindow", "<strong>YOUR</strong> FACE AI", None
            )
        )
        # if QT_CONFIG(tooltip)
        self.enrolface_but.setToolTip("")
        # endif // QT_CONFIG(tooltip)
        self.enrolface_but.setText(
            QCoreApplication.translate("MainWindow", "ENROLL FACE", None)
        )
        self.startrecog_but.setText(
            QCoreApplication.translate("MainWindow", "START RECOG", None)
        )
        # if QT_CONFIG(tooltip)
        self.add_user_frame.setToolTip("")
        # endif // QT_CONFIG(tooltip)
        self.uploadface_but_2.setText(
            QCoreApplication.translate("MainWindow", "UPLOAD FACE", None)
        )
        self.back_but_3.setText(QCoreApplication.translate("MainWindow", "BACK", None))
        self.deleteface_but_2.setText(
            QCoreApplication.translate("MainWindow", "DELETE FACE", None)
        )
        self.display_data_but.setText(QCoreApplication.translate("MainWindow", u"DISPLAY DATA", None))
        self.main_title_name_2.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p><span style=" font-size:20pt; font-weight:600;">YOUR</span><span style=" font-size:20pt;"> FACE AI</span></p></body></html>',
                None,
            )
        )
        self.webcam_but_2.setText(
            QCoreApplication.translate("MainWindow", "WEBCAM", None)
        )
        self.video_but.setText(QCoreApplication.translate("MainWindow", u"VIDEO", None))
        self.ai_back_but.setText(QCoreApplication.translate("MainWindow", u"BACK", None))
        self.main_title_name_3.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p><span style=" font-size:20pt; font-weight:600;">YOUR</span><span style=" font-size:20pt;"> FACE AI</span></p></body></html>',
                None,
            )
        )
        self.label_3.setText(
            QCoreApplication.translate("MainWindow", "TextLabel", None)
        )
        self.label_4.setText(
            QCoreApplication.translate("MainWindow", "TextLabel", None)
        )
        self.label.setText(QCoreApplication.translate("MainWindow", "TextLabel", None))
        
    # retranslateUi


    def handleEvent(self, MainWindow):
        self.enrolface_but.pressed.connect(self.add_user_page)
        self.deleteface_but_2.pressed.connect(self.delete_user)
        self.back_but_3.pressed.connect(self.main_window_page)
        self.startrecog_but.pressed.connect(self.ai_page)
        self.ai_back_but.pressed.connect(self.main_window_page)

        #self.startrecog_but.pressed.connect(self.ai_page)
    def delete_user(self):
        
        x = self.listView.selectedItems()
        x_list = []
        for i in x:
            x_list.append(i.text())
        print(x_list)

        deleteUsers(x_list)
        self.display_entry()

        

    def main_window_page(self):
        self.main_frame.raise_()
        self.listView.clear()
    
    def add_user_page(self):
        self.add_user_frame.raise_()
        self.uploadface_but_2.pressed.connect(self.open_file_directory)
        self.display_data_but.pressed.connect(self.display_entry)
        #self.back_but_3.pressed.connect
        
    def ai_page(self):
        self.ai_frame.raise_()
        self.webcam_but_2.pressed.connect(self.openWebCam)
        pass

    def openWebCam(self):
        runWebCam(0)


        

    def display_entry(self):
        self.listView.clear()
        names = np.load('data.npz').files
        counter = 0
        for name in names:
                self.listView.insertItem(counter, name)
                counter += 1
        self.listView.setStyleSheet(
            
            
            '	font: 16pt "Arial";\n'
            
        )
    def open_file_directory(self):
        #self.display_entry()
        fname = QFileDialog.getOpenFileNames(filter ="Image File(*.jpg *.jpeg *.png *.gif *.webp *.tiff *.psd *.raw *bmp)")
        
        if bool(fname[0]):
            
            dlg = UIDialog()
            personName = dlg.showDialog()
            #print(personName)
            if personName:
                #print(type(personName))
                #print("Person: {}, Images: {}".format(personName,fname[0]))
                #con = Control(personName,fname[0])
                pop_up = add_user_data(personName,fname[0]) #saves data
                if pop_up == "image_exist":
                    dlg.imageExists()
                #self.display_entry()
                #print(list(np.load("data.npz").keys()))
                elif pop_up == "no_face":
                    dlg.noDetectedFace()
                else:
                    self.display_entry()
                    dlg.uploadSuccess(personName)
                    
            else:
                dlg.uploadCancelled()
        else:
            dlg = UIDialog()
            dlg.uploadCancelled()


class UIDialog(QWidget):
        def __init__(self):
                super().__init__()
                #self.showDialog()
                

        def showDialog(self):
                text, ok = QInputDialog.getText(self, 'Person Label Dialog', 'Enter Name:')
                if ok:
                        return text

        def uploadCancelled(self):
            QMessageBox.about(self, "Upload Face", "Upload is cancelled")

        def uploadSuccess(self,other):
            QMessageBox.about(self, "Upload Face", "{} is successfully registered".format(other))
        def imageExists(self):
            QMessageBox.about(self, "Reminder", "Image already exists.")

        def noDetectedFace(self):
            QMessageBox.about(self, "Note", "No detected face.")


# class videoHandler(QWidget):
#         def __init__(self):
#                     super().__init__()
#                     #self.showDialog()
        
#         def setup_camera(self,other=0):
#             self.capture = cv2.VideCapture(other)
#             self.capture.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, self.video_size.width())
#             self.capture.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, self.video_size.height())

#             self.timer = QTimer()
#             self.timer.timeout.connect(self.display_video_stream)
#             self.timer.start(30)

#         def display_video_stream(self):
#             """Read frame from camera and repaint QLabel widget.
#             """
#             _, frame = self.capture.read()
#             frame = cv2.cvtColor(frame, cv2.cv.CV_BGR2RGB)
#             frame = cv2.flip(frame, 1)
#             image = QIimage = qimage2ndarray.array2qimage(frame)
#             self.image_label.setPixmap(QPixmap.fromImage(image))                 