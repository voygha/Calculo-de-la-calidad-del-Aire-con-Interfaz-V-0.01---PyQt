# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'caldiaddelaire.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMdiSubWindow, QMainWindow, QWidget, QPushButton,QTableView,QHeaderView,QTableWidgetItem
from PyQt5.QtGui import QPainter, QColor, QPen
import random

import pymysql





class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(933, 611)
        MainWindow.setStyleSheet("*{\n"
"background: #eeeded;\n"
"}\n"
"\n"
"QFrame{\n"
"border-radius:30px;\n"
"}\n"
"QPushButton{\n"
"border-radius:15px;\n"
"background:#30475e;\n"
"color: #ffffff;\n"
"font-size: 15px;\n"
"}\n"
"\n"
"QlineEdit{\n"
"background: #eeeded;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 10, 300, 50))
        self.label_2.setScaledContents(False)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 60, 251, 16))
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(570, -60, 471, 281))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("imagenes/a.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 120, 901, 451))
        self.tabWidget.setStyleSheet("border:none;")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.btnreporte = QtWidgets.QPushButton(self.tab)
        self.btnreporte.setGeometry(QtCore.QRect(780, 370, 111, 31))
        self.btnreporte.setStyleSheet("background-color: rgb(236, 82, 75);")
        self.btnreporte.setObjectName("btnreporte")
        self.btnsensor = QtWidgets.QPushButton(self.tab)
        self.btnsensor.setGeometry(QtCore.QRect(780, 30, 111, 31))
        self.btnsensor.setObjectName("btnsensor")
        self.frame1 = QtWidgets.QFrame(self.tab)
        self.frame1.setGeometry(QtCore.QRect(10, 20, 751, 391))
        self.frame1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame1.setObjectName("frame1")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.frame1)
        self.tableWidget_2.setGeometry(QtCore.QRect(30, 20, 701, 351))
        self.tableWidget_2.setStyleSheet("border:none; color:#fff; background-color: #283747")
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.btnsensor.raise_()
        self.frame1.raise_()
        self.btnreporte.raise_()
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.frame1_2 = QtWidgets.QFrame(self.tab_2)
        self.frame1_2.setGeometry(QtCore.QRect(10, 19, 871, 391))
        self.frame1_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame1_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame1_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame1_2.setObjectName("frame1_2")
        self.lineEdit = QtWidgets.QLineEdit(self.frame1_2)
        self.lineEdit.setGeometry(QtCore.QRect(50, 100, 280, 31))
        self.lineEdit.setStyleSheet("background: #eeeded;\n"
"\n"
"     border-radius: 5px;\n"
"    \n"
"    border-bottom: 1px solid black;")
        self.lineEdit.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(self.frame1_2)
        self.label_4.setGeometry(QtCore.QRect(50, 50, 111, 31))
        self.label_4.setObjectName("label_4")
        self.btnguardar = QtWidgets.QPushButton(self.tab_2)
        self.btnguardar.setGeometry(QtCore.QRect(370, 110, 161, 41))
        self.btnguardar.setObjectName("btnguardar")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 933, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.btnsensor.clicked.connect(self.valores)


    def valores(self):
        a= round(random.uniform(0,0.6),3)
        a= (a * 100)
        
        

        ozono=0

        c=0
        k=0
        bphi=0
        bplo=0
        ihi=0
        ilo=0
        resta=0




        bphi= round(random.uniform(0.001,0.604),3)
        #bphi=0.070
        print("El valor de bphi EL QUE IMPORTA es: ",bphi)

        if bphi >= 0.000 and bphi  <= 0.070:
            bplo=round(random.uniform(0,bphi - 0.001),3)
            print(bplo)
            ihi=50
            ilo=0
            k= ihi - ilo
            resta= round((bphi - bplo),3)
            print("El valor de la resta es: ",resta)
            k= round((k / resta),2)
            print("El valor de K es: ",k)
            c=round(random.uniform(bplo+0.001,0.070),3)
            print("El valor redondeado para la concentraci??n del contaminante es: ", c)
            ozono = k * (c - bplo)
            ozono= round((ozono + ilo))
            print("El indice de contaminaci??n en ozono es: ", ozono)



            bphi1=0
            bplo1=0
            k1=0
            resta=0
            c1=0
            pam10=0
            print("\n")
            print("\n")
            #SIEMPRE HAY QUE DARLE UNNO MAS
            bphi1= round(random.uniform(1,40))
            print("El valor de bphi es: ", bphi1)
            #bphi=40
            #SIEMPRE HAY QUE DARLE UNNO MAS
            bplo1=round(random.uniform(0,bphi1 - 1))
            print("El valor de bplo es: ", bplo1)
            k1= ihi - ilo
            resta= round((bphi1 - bplo1))
            print("El valor de la resta es: ",resta)
            k1= round((k1 / resta),3)
            print("El valor de K es: ",k1)
            c1=round(random.uniform(bplo1+1,40))
            print("El valor redondeado para la concentraci??n del contaminante es: ", c1)
            pam10 = k1 * (c1 - bplo1)
            pam10= round((pam10 + ilo))
            print("El indice de contaminaci??n en Part??culas Menores a 10 micr??metros (PM10) es: ", pam10)
            


            bphi2=0
            bplo2=0
            k2=0
            resta=0
            c2=0
            pam25=0
            print("\n")
            print("\n")
            bphi2= round(random.uniform(0.0,12.0),1)
            print("El valor de bphi es: ", bphi2)
            #bphi=12.0
            bplo2=round(random.uniform(0.1,bphi2 - 0.1),1)
            print("El valor de bplo es: ", bplo2)
            k2= ihi - ilo
            resta= round((bphi2 - bplo2),1)
            print("El valor de la resta es: ",resta)
            k2= round((k2 / resta),3)
            print("El valor de K es: ",k2)
            c2=round(random.uniform(bplo2+0.1,12.0),1)
            print("El valor redondeado para la concentraci??n del contaminante es: ", c2)
            pam25 = k2 * (c2 - bplo2)
            pam25= round((pam25 + ilo))
            print("El indice de contaminaci??n en Part??culas Menores a 2.5 micr??metros (PM2.5) es: ", pam25)


            print("\n")
            print("\n")
            print("La Calidad del Aire es BUENA")
            calidada="BUENA"

        """
        AQUI COMIENZA EL SEGUNDO
        """




        if bphi >= 0.071 and bphi  <= 0.095:
            bplo=round(random.uniform(0.071,bphi - 0.001),3)
            print(bplo)
            ihi=100
            ilo=51
            k= ihi - ilo
            resta= round((bphi - bplo),3)
            print("El valor de la resta es: ",resta)
            k= round((k / resta),2)
            print("El valor de K es: ",k)
            c=round(random.uniform(bplo+0.001,0.095),3)
            print("El valor redondeado para la concentraci??n del contaminante es: ", c)
            ozono = k * (c - bplo)
            ozono= round((ozono + ilo))
            print("El indice de contaminaci??n en ozono es: ", ozono)



            bphi1=0
            bplo1=0
            k1=0
            resta=0
            c1=0
            pam10=0
            print("\n")
            print("\n")
            bphi1= round(random.uniform(41,75))
            print("El valor de bphi es: ", bphi1)
            #bphi=40
            #SIEMPRE HAY QUE DARLE UNNO MAS
            bplo1=round(random.uniform(40,bphi1 - 1))
            print("El valor de bplo es: ", bplo1)
            k1= ihi - ilo
            resta= round((bphi1 - bplo1))
            print("El valor de la resta es: ",resta)
            k1= round((k1 / resta),3)
            print("El valor de K es: ",k1)
            c1=round(random.uniform(bplo1+1,75))
            print("El valor redondeado para la concentraci??n del contaminante es: ", c1)
            pam10 = k1 * (c1 - bplo1)
            pam10= round((pam10 + ilo))
            print("El indice de contaminaci??n en Part??culas Menores a 10 micr??metros (PM10) es: ", pam10)
            


            bphi2=0
            bplo2=0
            k2=0
            resta=0
            c2=0
            pam25=0
            print("\n")
            print("\n")
            bphi2= round(random.uniform(12.2,45.0),1)
            print("El valor de bphi es: ", bphi2)
            #bphi=12.0
            bplo2=round(random.uniform(12.1,bphi2 - 0.1),1)
            print("El valor de bplo es: ", bplo2)
            k2= ihi - ilo
            resta= round((bphi2 - bplo2),1)
            print("El valor de la resta es: ",resta)
            k2= round((k2 / resta),3)
            print("El valor de K es: ",k2)
            c2=round(random.uniform(bplo2+0.1,45.0),1)
            print("El valor redondeado para la concentraci??n del contaminante es: ", c2)
            pam25 = k2 * (c2 - bplo2)
            pam25= round((pam25 + ilo))
            print("El indice de contaminaci??n en Part??culas Menores a 2.5 micr??metros (PM2.5) es: ", pam25)


            print("\n")
            print("\n")
            print("La Calidad del Aire es REGULAR")
            calidada="REGULAR"





        """
        AQUI COMIENZA EL TERCERO
        """




        if bphi >= 0.096 and bphi  <= 0.154:
            bplo=round(random.uniform(0.096,bphi - 0.001),3)
            print(bplo)
            ihi=150
            ilo=101
            k= ihi - ilo
            resta= round((bphi - bplo),3)
            print("El valor de la resta es: ",resta)
            k= round((k / resta),2)
            print("El valor de K es: ",k)
            c=round(random.uniform(bplo+0.001,0.154),3)
            print("El valor redondeado para la concentraci??n del contaminante es: ", c)
            ozono = k * (c - bplo)
            ozono= round((ozono + ilo))
            print("El indice de contaminaci??n en ozono es: ", ozono)



            bphi1=0
            bplo1=0
            k1=0
            resta=0
            c1=0
            pam10=0
            print("\n")
            print("\n")
            #SIEMPRE HAY QUE DARLE UNNO MAS
            bphi1= round(random.uniform(77,214))
            print("El valor de bphi es: ", bphi1)
            #bphi=40
            bplo1=round(random.uniform(76,bphi1 - 1))
            print("El valor de bplo es: ", bplo1)
            k1= ihi - ilo
            resta= round((bphi1 - bplo1))
            print("El valor de la resta es: ",resta)
            k1= round((k1 / resta),3)
            print("El valor de K es: ",k1)
            c1=round(random.uniform(bplo1+1,214))
            print("El valor redondeado para la concentraci??n del contaminante es: ", c1)
            pam10 = k1 * (c1 - bplo1)
            pam10= round((pam10 + ilo))
            print("El indice de contaminaci??n en Part??culas Menores a 10 micr??metros (PM10) es: ", pam10)
            


            bphi2=0
            bplo2=0
            k2=0
            resta=0
            c2=0
            pam25=0
            print("\n")
            print("\n")
            bphi2= round(random.uniform(45.2,97.4),1)
            print("El valor de bphi es: ", bphi2)
            #bphi=12.0
            bplo2=round(random.uniform(45.1,bphi2 - 0.1),1)
            print("El valor de bplo es: ", bplo2)
            k2= ihi - ilo
            resta= round((bphi2 - bplo2),1)
            print("El valor de la resta es: ",resta)
            k2= round((k2 / resta),3)
            print("El valor de K es: ",k2)
            c2=round(random.uniform(bplo2+0.1,97.4),1)
            print("El valor redondeado para la concentraci??n del contaminante es: ", c2)
            pam25 = k2 * (c2 - bplo2)
            pam25= round((pam25 + ilo))
            print("El indice de contaminaci??n en Part??culas Menores a 2.5 micr??metros (PM2.5) es: ", pam25)


            print("\n")
            print("\n")
            print("La Calidad del Aire es MALA")

            calidada="MALA"






        """
        AQUI COMIENZA EL CUARTO
        """




        if bphi >= 0.155 and bphi  <= 0.204:
            bplo=round(random.uniform(0.155,bphi - 0.001),3)
            print(bplo)
            ihi=200
            ilo=151
            k= ihi - ilo
            resta= round((bphi - bplo),3)
            print("El valor de la resta es: ",resta)
            k= round((k / resta),2)
            print("El valor de K es: ",k)
            c=round(random.uniform(bplo+0.001,0.204),3)
            print("El valor redondeado para la concentraci??n del contaminante es: ", c)
            ozono = k * (c - bplo)
            ozono= round((ozono + ilo))
            print("El indice de contaminaci??n en ozono es: ", ozono)



            bphi1=0
            bplo1=0
            k1=0
            resta=0
            c1=0
            pam10=0
            print("\n")
            print("\n")
            #SIEMPRE HAY QUE DARLE UNNO MAS
            bphi1= round(random.uniform(216,354))
            print("El valor de bphi es: ", bphi1)
            #bphi=40
            bplo1=round(random.uniform(215,bphi1 - 1))
            print("El valor de bplo es: ", bplo1)
            k1= ihi - ilo
            resta= round((bphi1 - bplo1))
            print("El valor de la resta es: ",resta)
            k1= round((k1 / resta),3)
            print("El valor de K es: ",k1)
            c1=round(random.uniform(bplo1+1,354))
            print("El valor redondeado para la concentraci??n del contaminante es: ", c1)
            pam10 = k1 * (c1 - bplo1)
            pam10= round((pam10 + ilo))
            print("El indice de contaminaci??n en Part??culas Menores a 10 micr??metros (PM10) es: ", pam10)
            


            bphi2=0
            bplo2=0
            k2=0
            resta=0
            c2=0
            pam25=0
            print("\n")
            print("\n")
            bphi2= round(random.uniform(97.6,150.4),1)
            print("El valor de bphi es: ", bphi2)
            #bphi=12.0
            bplo2=round(random.uniform(97.5,bphi2 - 0.1),1)
            print("El valor de bplo es: ", bplo2)
            k2= ihi - ilo
            resta= round((bphi2 - bplo2),1)
            print("El valor de la resta es: ",resta)
            k2= round((k2 / resta),3)
            print("El valor de K es: ",k2)
            c2=round(random.uniform(bplo2+0.1,150.4),1)
            print("El valor redondeado para la concentraci??n del contaminante es: ", c2)
            pam25 = k2 * (c2 - bplo2)
            pam25= round((pam25 + ilo))
            print("El indice de contaminaci??n en Part??culas Menores a 2.5 micr??metros (PM2.5) es: ", pam25)


            print("\n")
            print("\n")
            print("La Calidad del Aire es MUY MALA")
            calidada="MUY MALA"



        """
        AQUI COMIENZA EL ULTIMO
        """

        if bphi >= 0.205 and bphi  <= 0.604:
            bplo=round(random.uniform(0.205,bphi - 0.001),3)
            print(bplo)
            ihi=401
            ilo=201
            k= ihi - ilo
            resta= round((bphi - bplo),3)
            print("El valor de la resta es: ",resta)
            k= round((k / resta),2)
            print("El valor de K es: ",k)
            c=round(random.uniform(bplo+0.001,0.604),3)
            print("El valor redondeado para la concentraci??n del contaminante es: ", c)
            ozono = k * (c - bplo)
            ozono= round((ozono + ilo))
            print("El indice de contaminaci??n en ozono es: ", ozono)



            bphi1=0
            bplo1=0
            k1=0
            resta=0
            c1=0
            pam10=0
            print("\n")
            print("\n")
            #SIEMPRE HAY QUE DARLE UNNO MAS
            bphi1= round(random.uniform(356,604))
            print("El valor de bphi es: ", bphi1)
            #bphi=40
            bplo1=round(random.uniform(355,bphi1 - 1))
            print("El valor de bplo es: ", bplo1)
            k1= ihi - ilo
            resta= round((bphi1 - bplo1))
            print("El valor de la resta es: ",resta)
            k1= round((k1 / resta),3)
            print("El valor de K es: ",k1)
            c1=round(random.uniform(bplo1+1,604))
            print("El valor redondeado para la concentraci??n del contaminante es: ", c1)
            pam10 = k1 * (c1 - bplo1)
            pam10= round((pam10 + ilo))
            print("El indice de contaminaci??n en Part??culas Menores a 10 micr??metros (PM10) es: ", pam10)
            


            bphi2=0
            bplo2=0
            k2=0
            resta=0
            c2=0
            pam25=0
            print("\n")
            print("\n")
            bphi2= round(random.uniform(150.6,500.4),1)
            print("El valor de bphi es: ", bphi2)
            #bphi=12.0
            bplo2=round(random.uniform(150.5,bphi2 - 0.1),1)
            print("El valor de bplo es: ", bplo2)
            k2= ihi - ilo
            resta= round((bphi2 - bplo2),1)
            print("El valor de la resta es: ",resta)
            k2= round((k2 / resta),3)
            print("El valor de K es: ",k2)
            c2=round(random.uniform(bplo2+0.1,500.4),1)
            print("El valor redondeado para la concentraci??n del contaminante es: ", c2)
            pam25 = k2 * (c2 - bplo2)
            pam25= round((pam25 + ilo))
            print("El indice de contaminaci??n en Part??culas Menores a 2.5 micr??metros (PM2.5) es: ", pam25)


            print("\n")
            print("\n")
            print("La Calidad del Aire es EXTREMADAMENTE MALA")    
            calidada="EXTREMADAMENTE MALA"


            
        self.tableWidget_2.setRowCount(5)         
        self.tableWidget_2.setColumnCount(10)
        
        self.tableWidget_2.setHorizontalHeaderLabels(['id','Nombre','BPHi','BPLo','Ihi','Ilo','K','C','Valor','Categor??a'])
        #self.tableWidget_2.resizeColumnToContents(1)
        #self.tableWidget_2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        self.tableWidget_2.setColumnWidth(0, 20);
        self.tableWidget_2.setColumnWidth(1, 170);
        self.tableWidget_2.setColumnWidth(2, 50);
        self.tableWidget_2.setColumnWidth(3, 50);
        self.tableWidget_2.setColumnWidth(4, 40);
        self.tableWidget_2.setColumnWidth(5, 40);
        self.tableWidget_2.setColumnWidth(6, 60);
        self.tableWidget_2.setColumnWidth(7, 45);
        self.tableWidget_2.setColumnWidth(8, 45);
        self.tableWidget_2.setColumnWidth(9, 160);
        
        for i in range(5):
            
            miConexion = pymysql.connect( host='localhost', user= 'root', passwd='12345', db='calidad_aire' )
            cur = miConexion.cursor()
            cur.execute( "SELECT nombre_contaminante FROM contaminante where id_contaminante=%s",i+1 )
            #print(cur.fetchall())
            nombre_con=cur.fetchall()
            nombre_con=[i[0] for i in nombre_con]
            nombre_con=nombre_con[-1]
            cur.execute( "SELECT id_contaminante FROM contaminante where id_contaminante=%s",i+1 )
            id_con=cur.fetchall()
            id_con=[i[0] for i in id_con]
            id_con=id_con[-1]
            """for id_contaminante, nombre_contaminante in cur.fetchall() :
                print (id_contaminante, nombre_contaminante)"""
            


            
            miConexion.close()
            self.tableWidget_2.setItem(i,0,QTableWidgetItem(str(id_con)))
            self.tableWidget_2.setItem(i,1,QTableWidgetItem(str(nombre_con)))


            if nombre_con == "ozono (o3)" or nombre_con == "bioxido de nitrogeno (NO2)" or nombre_con == "bioxido de azufre (SO2)":
                self.tableWidget_2.setItem(i,2,QTableWidgetItem(str(bphi)))
                self.tableWidget_2.setItem(i,3,QTableWidgetItem(str(bplo)))
                self.tableWidget_2.setItem(i,4,QTableWidgetItem(str(ihi)))
                self.tableWidget_2.setItem(i,5,QTableWidgetItem(str(ilo)))
                self.tableWidget_2.setItem(i,6,QTableWidgetItem(str(k)))
                self.tableWidget_2.setItem(i,7,QTableWidgetItem(str(c)))
                self.tableWidget_2.setItem(i,8,QTableWidgetItem(str(ozono)))
           

            if nombre_con == "particulas suspendidas (PM10)":
                self.tableWidget_2.setItem(i,2,QTableWidgetItem(str(bphi1)))
                self.tableWidget_2.setItem(i,3,QTableWidgetItem(str(bplo1)))
                self.tableWidget_2.setItem(i,4,QTableWidgetItem(str(ihi)))
                self.tableWidget_2.setItem(i,5,QTableWidgetItem(str(ilo)))
                self.tableWidget_2.setItem(i,6,QTableWidgetItem(str(k1)))
                self.tableWidget_2.setItem(i,7,QTableWidgetItem(str(c1)))
                self.tableWidget_2.setItem(i,8,QTableWidgetItem(str(pam10)))
                
            if nombre_con == "particulas menores a 2.5 micrometros":
                self.tableWidget_2.setItem(i,2,QTableWidgetItem(str(bphi2)))
                self.tableWidget_2.setItem(i,3,QTableWidgetItem(str(bplo2)))
                self.tableWidget_2.setItem(i,4,QTableWidgetItem(str(ihi)))
                self.tableWidget_2.setItem(i,5,QTableWidgetItem(str(ilo)))
                self.tableWidget_2.setItem(i,6,QTableWidgetItem(str(k2)))
                self.tableWidget_2.setItem(i,7,QTableWidgetItem(str(c2)))
                self.tableWidget_2.setItem(i,8,QTableWidgetItem(str(pam25)))



            
            
            
            
            self.tableWidget_2.setItem(i,9,QTableWidgetItem(str(calidada)))
            #self.tableWidget_2.item(i,9).setText(QtGui.QColor("color:#fff"))
            #self.tableWidget_2.setItem(i,9, QTableWidgetItem(str(calidada)).setForeground(QtGui.QColor('#ffffff')))
            if calidada=="BUENA":
                self.tableWidget_2.item(i,9).setBackground(QtGui.QColor('#188654'))
                #self.tableWidget_2.item.styleSheet("color: #ffffff;")
                
                #self.tableWidget_2.item(i,9).setColor(QtGui.QColor(white))
                #self.tableWidget_2.item(i,9), QtGui.QBrush(QtGui.QColor(236,47,6)), QtCore.Qt.BackgroundRole
            if calidada=="REGULAR":
                self.tableWidget_2.item(i,9).setBackground(QtGui.QColor('#0D6EFD'))
            if calidada=="MALA":
                self.tableWidget_2.item(i,9).setBackground(QtGui.QColor('#FC7E15'))
            if calidada=="MUY MALA":
                self.tableWidget_2.item(i,9).setBackground(QtGui.QColor('#E25C6A'))
            if calidada=="EXTREMADAMENTE MALA":
                self.tableWidget_2.item(i,9).setBackground(QtGui.QColor('#DD3445'))
            
    

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; font-weight:600; color:#30475e;\">Calidad del Aire</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#1d1f1e;\">Simulador de la calidad del aire</span></p></body></html>"))
        self.btnreporte.setText(_translate("MainWindow", "Reporte"))
        self.btnsensor.setText(_translate("MainWindow", "Sensor"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Estadisticas"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Nombre:</span></p></body></html>"))
        self.btnguardar.setText(_translate("MainWindow", "Guardar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Nuevo parametro"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
