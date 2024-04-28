import sys
import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QIntValidator 
from PyQt5.QtGui import QFont, QPixmap, QIcon,QColor, QPalette
from PyQt5.QtWidgets import QMainWindow, QDialog, QApplication, QLabel, QComboBox, QLineEdit,QPushButton, QFrame,QRadioButton,QHeaderView
from PyQt5.QtWidgets import QButtonGroup,QTableWidget,QTableWidgetItem,QVBoxLayout,QCheckBox, QMessageBox

lista_estudiantes = list()

##QDIALOG-Segunda Ventana##
class Dialogo(QDialog):
    def clear(self):
        del lista_estudiantes[:]
        self.ventana_tabla.clearContents()
        self.ventana_tabla.setRowCount(0)
    
    def deleteRow(self):
        filaSeleccionada = self.ventana_tabla.selectedItems()

        if filaSeleccionada:
            row = filaSeleccionada[0].row()
            self.ventana_tabla.removeRow(row)

            self.ventana_tabla.clearSelection()
            lista_estudiantes.pop()
        else:
            QMessageBox.critical(self, "ERROR", "No hay fila que eliminar.", QMessageBox.Ok)
    
    
            
    def __init__(self):
        filas = 0
        QDialog.__init__(self)
        self.setFixedSize(800, 500)
        self.setWindowTitle("REGISTRO DE ESTUDIANTES")
        self.ventana_tabla = QTableWidget(self)
        self.ventana_tabla.resize(800,400)
        self.ventana_tabla.setRowCount(12)  
        self.ventana_tabla.setColumnCount(12) 
        self.ventana_tabla.horizontalHeader().setStretchLastSection(True) 
        self.ventana_tabla.horizontalHeader().setSectionResizeMode( QHeaderView.Stretch)
        columnas = ("Nombre","Apellido Paterno", "Apellido Materno","Matricula","Edad", "Domicilio","Municipio","Estado","Porcentaje Beca","Materias Favoritas")
        self.ventana_tabla.setHorizontalHeaderLabels(columnas) 
        for i in lista_estudiantes:
            self.ventana_tabla.setRowCount(filas + 1)
            indice = QTableWidgetItem(i[0])
            indice.setTextAlignment(4)
            self.ventana_tabla.setItem(filas, 0, indice)
            self.ventana_tabla.setItem(filas, 1, QTableWidgetItem(i[1]))
            self.ventana_tabla.setItem(filas, 2, QTableWidgetItem(i[2]))
            self.ventana_tabla.setItem(filas, 3, QTableWidgetItem(i[3]))
            self.ventana_tabla.setItem(filas, 4, QTableWidgetItem(i[4]))
            self.ventana_tabla.setItem(filas, 5, QTableWidgetItem(i[5]))
            self.ventana_tabla.setItem(filas, 6, QTableWidgetItem(i[6]))
            self.ventana_tabla.setItem(filas, 7, QTableWidgetItem(i[7]))
            self.ventana_tabla.setItem(filas, 8, QTableWidgetItem(i[8]))
            self.ventana_tabla.setItem(filas, 9, QTableWidgetItem(i[9]))
            filas += 1
        
        
        buttnRegresar = QPushButton("Regresar", self)
        buttnRegresar.setFixedWidth(150)
        buttnRegresar.move(500, 440)
        buttnRegresar.setIcon(QIcon("img\ico-back.png"))
        buttnRegresar.setIconSize(QtCore.QSize(30,30))
        
        
        buttnLimpiar = QPushButton("Borrar Todo", self)
        buttnLimpiar.setFixedWidth(150)
        buttnLimpiar.move(300, 440)
        buttnLimpiar.setIcon(QIcon("img\ico-delete.png"))
        buttnLimpiar.setIconSize(QtCore.QSize(30,30))
        
        
        self.buttnDeleteRow = QPushButton("Eliminar fila",self)
        self.buttnDeleteRow.setFixedWidth(150)
        self.buttnDeleteRow.move(100, 440)
        self.buttnDeleteRow.setIcon(QIcon("img\ico-eliminar-fila.svg"))
        self.buttnDeleteRow.setIconSize(QtCore.QSize(30,30))
        
        
        
        
        
        buttnRegresar.clicked.connect(self.close)
        buttnLimpiar.clicked.connect(self.clear)
        self.buttnDeleteRow.clicked.connect(self.deleteRow)

##VENTANA PRINCIPAL##
class Ventana_principal(QMainWindow):
    def abrirDialogo(self):
        self.dialogo.exec_()
    
    def __init__(self, parent=None):
        super(Ventana_principal, self).__init__(parent)
        self.setWindowTitle("Captura Alumnos")
        self.setWindowIcon(QIcon("img\ico-pantalla.svg"))
        self.setFixedSize(800, 550)
        paleta = QPalette()
        paleta.setColor(QPalette.Background, QColor(85, 85, 127))
        self.setPalette(paleta)
        self.initUI()

#---------------------APARTADO OPERATIVO---------------------#
    def guardar(self):
        Nombre = self.lineEditNombre.text()
        Apellido_Paterno = self.lineEditApellido_Paterno.text()
        Apellido_Materno = self.lineEditApellido_Materno.text()
        Matricula = self.lineEditMatricula.text()
        Edad = self.lineEditEdad.text()
        Domicilio = self.lineEditCalle.text()
        Estado = self.comboBoxEstado.currentText()
        Municipio = self.comboBoxMunicipio.currentText()
        
        Beca = list()
        if self.radio_cero.isChecked():
            cero = self.radio_cero.text()
            Beca.append(cero)
        if self.radio_25.isChecked():
            veinticinco = self.radio_25.text()
            Beca.append(veinticinco)
        if self.radio_cien.isChecked():
            cien = self.radio_cien.text()
            Beca.append(cien)
        if self.radio_50.isChecked():
            cincuenta = self.radio_50.text()
            Beca.append(cincuenta)
        
        Materias_favoritas = list()
        if self.Programacionbox.isChecked()==True:
                Programacion = "Programacion"
                Materias_favoritas.append(Programacion)
        if self.Contabilidadbox.isChecked()==True:
                Contabilidad = "Contabilidad"
                Materias_favoritas.append(Contabilidad)
        if self.boxEstadistica.isChecked()==True:
                Estadistica = "Estadistica"
                Materias_favoritas.append(Estadistica)
        if self.Basebox.isChecked()==True:
                Base = "Base de Datos"
                Materias_favoritas.append(Base)      
        if self.Investigacionbox.isChecked()==True:
                Investigación = "Investigacion de Operaciones"
                Materias_favoritas.append(Investigación)
        
        if Edad == str:
            print("Valor de cadena")

        else:
            VALUES = list()
            VALUES.append(Nombre)
            VALUES.append(Apellido_Paterno)
            VALUES.append(Apellido_Materno)
            VALUES.append(Matricula)
            VALUES.append(Edad)
            VALUES.append(Domicilio)
            VALUES.append(Municipio)
            VALUES.append(Estado)
            Porcentajes = str(Beca)
            VALUES.append(Porcentajes)
            Materias_fav = str(Materias_favoritas)
            VALUES.append(Materias_fav)
            lista_estudiantes.append(VALUES)
            
            self.dialogo = Dialogo()
            self.abrirDialogo() 

    def escribir(self):
        registro = pd.DataFrame(lista_estudiantes)
        r = registro.rename(columns={0:'Nombre', 1:'Apellido Paterno', 2:'Apellido Materno', 3:'Matricula',4:'Edad', 5:'Domicilio', 6:'Municipio', 7:'Estado', 8:'Porcentaje Beca', 9:'Materia Favorita'})
        r.to_csv (r'Registro_alumnos.csv', index=True, header=True)

        print("Se ha registrado la información en un archivo CSV con el nombre de 'Registro_alumnos'")

    def limpiar(self):
        self.comboBoxMunicipio.setCurrentIndex(-1)
        self.comboBoxEstado.setCurrentIndex(-1)
        
        for line in [self.lineEditNombre, self.lineEditApellido_Paterno,self.lineEditApellido_Materno,
                    self.lineEditMatricula,self.lineEditEdad,self.lineEditCalle]: line.clear()
        
        for box in [self.Programacionbox,self.Contabilidadbox,self.boxEstadistica,
                    self.Basebox,self.Investigacionbox]:box.setChecked(False)

        for buttn in [self.radio_cero, self.radio_25, self.radio_50, self.radio_cien]:
            buttn.setAutoExclusive(False)
            buttn.setChecked(False)
            buttn.repaint()
            buttn.setAutoExclusive(True)  

#---------------------DISEÑO---------------------#

    def initUI(self):
        labelTitulo= QLabel("Captura de Alumnos", self)
        labelTitulo.setFont(QFont("MS Shell Dlg 2", 20))
        labelTitulo.setStyleSheet('color:white')
        labelTitulo.move(300, 10)
        #labelTitulo2= QLabel("ALUMNOS", self)
        #labelTitulo2.setFont(QFont("MS Shell Dlg 2", 11))
        #labelTitulo2.setStyleSheet('color:white')
        #labelTitulo2.move(390, 10)
        
        buttonGuardar = QPushButton(" Grabar", self)
        buttonGuardar.setFixedWidth(135)
        buttonGuardar.setFixedHeight(35)
        buttonGuardar.move(150, 450)
        buttonGuardar.setIcon(QIcon("img\ico-save.png"))
        buttonGuardar.setIconSize(QtCore.QSize(30,30))

        
        buttonEscribir = QPushButton(" Escribir", self)
        buttonEscribir.setFixedWidth(135)
        buttonEscribir.setFixedHeight(35)
        buttonEscribir.move(310, 450)
        buttonEscribir.setIcon(QIcon("img\ico-excel.svg"))
        buttonEscribir.setIconSize(QtCore.QSize(25,25))
        
        
        buttonLimpiar = QPushButton(" Limpiar", self)
        buttonLimpiar.setFixedWidth(135)
        buttonLimpiar.setFixedHeight(35)
        buttonLimpiar.move(470, 450)
        buttonLimpiar.setIcon(QIcon("img\ico-clean.png"))
        buttonLimpiar.setIconSize(QtCore.QSize(25,25))

        
        
        buttonGuardar.clicked.connect(self.guardar)
        buttonEscribir.clicked.connect(self.escribir)
        buttonLimpiar.clicked.connect(self.limpiar)
        
        labelNombre = QLabel("Nombre", self)
        labelNombre.setFont(QFont("MS Shell Dlg 2", 9))
        labelNombre.setStyleSheet('color:white')
        labelNombre.move(7, 60)
        frameNombre = QFrame(self)
        frameNombre.setFixedWidth(285)
        frameNombre.setFixedHeight(28)
        frameNombre.move(60, 60)
        self.lineEditNombre = QLineEdit(frameNombre)
        self.lineEditNombre.setFrame(True)
        self.lineEditNombre.setTextMargins(7, 1, 6, 1)
        self.lineEditNombre.setFixedWidth(245)
        self.lineEditNombre.setFixedHeight(29)
        self.lineEditNombre.move(40, 1)
        
        
        labelApellido_Paterno = QLabel("Apellido Paterno", self)
        labelApellido_Paterno.setFont(QFont("MS Shell Dlg 2", 9))
        labelApellido_Paterno.setStyleSheet('color:white')
        labelApellido_Paterno.setLineWidth(8)
        labelApellido_Paterno.move(7, 120)
        frameApellido_Paterno = QFrame(self)
        frameApellido_Paterno.setFixedWidth(290)
        frameApellido_Paterno.setFixedHeight(29)
        frameApellido_Paterno.move(60, 120)
        self.lineEditApellido_Paterno = QLineEdit(frameApellido_Paterno)
        self.lineEditApellido_Paterno.setFrame(True)
        self.lineEditApellido_Paterno.setTextMargins(7, 1, 6, 1)
        self.lineEditApellido_Paterno.setFixedWidth(245)
        self.lineEditApellido_Paterno.setFixedHeight(29)
        self.lineEditApellido_Paterno.move(40, 1)
        
        
        labelApellido_Materno = QLabel("Apellido Materno", self)
        labelApellido_Materno.setFont(QFont("MS Shell Dlg 2", 9))
        labelApellido_Materno.setStyleSheet('color:white')
        labelApellido_Materno.move(7, 180)
        frameApellido_Materno = QFrame(self)
        frameApellido_Materno.setFixedWidth(290)
        frameApellido_Materno.setFixedHeight(29)
        frameApellido_Materno.move(60, 180)
        self.lineEditApellido_Materno = QLineEdit(frameApellido_Materno)
        self.lineEditApellido_Materno.setFrame(True)
        self.lineEditApellido_Materno.setTextMargins(7, 1, 6, 1)
        self.lineEditApellido_Materno.setFixedWidth(245)
        self.lineEditApellido_Materno.setFixedHeight(29)
        self.lineEditApellido_Materno.move(40, 1)

        labelMatricula = QLabel("Matrícula", self)
        labelMatricula.setFont(QFont("MS Shell Dlg 2", 9))
        labelMatricula.setStyleSheet('color:white')
        labelMatricula.move(7, 240)
        frameMatricula = QFrame(self)
        frameMatricula.setFixedWidth(290)
        frameMatricula.setFixedHeight(29)
        frameMatricula.move(60, 240)
        self.lineEditMatricula = QLineEdit(frameMatricula)
        self.lineEditMatricula.setFrame(True)
        self.lineEditMatricula.setTextMargins(7, 1, 6, 1)
        self.lineEditMatricula.setFixedWidth(245)
        self.lineEditMatricula.setFixedHeight(29)
        self.lineEditMatricula.move(40, 1)
        self.lineEditMatricula.setValidator(QIntValidator())
        
        labelEdad = QLabel("Edad", self)
        labelEdad.setFont(QFont("MS Shell Dlg 2", 9))
        labelEdad.setStyleSheet('color:white')
        labelEdad.move(7, 300)
        frameEdad = QFrame(self)
        frameEdad.setFixedWidth(290)
        frameEdad.setFixedHeight(29)
        frameEdad.move(60, 300)
        self.lineEditEdad = QLineEdit(frameEdad)
        self.lineEditEdad.setFrame(True)
        self.lineEditEdad.setTextMargins(7, 1, 6, 1)
        self.lineEditEdad.setFixedWidth(245)
        self.lineEditEdad.setFixedHeight(29)
        self.lineEditEdad.move(40, 1)
        self.lineEditEdad.setValidator(QIntValidator())
        
        labelCalle = QLabel("Calle y Numero", self)
        labelCalle.setFont(QFont("MS Shell Dlg 2", 9))
        labelCalle.setStyleSheet('color:white')
        labelCalle.move(7, 360)
        frameCalle = QFrame(self)
        frameCalle.setFixedWidth(290)
        frameCalle.setFixedHeight(29)
        frameCalle.move(60, 360)
        self.lineEditCalle = QLineEdit(frameCalle)
        self.lineEditCalle.setFrame(True)
        self.lineEditCalle.setTextMargins(7, 1, 6, 1)
        self.lineEditCalle.setFixedWidth(245)
        self.lineEditCalle.setFixedHeight(29)
        self.lineEditCalle.move(40, 1)
        
        
        labelMunicipio = QLabel("Municipio", self)
        labelMunicipio.setFont(QFont("MS Shell Dlg 2", 9))
        labelMunicipio.setStyleSheet('color:white')
        labelMunicipio.move(515, 60)

        self.comboBoxMunicipio = QComboBox(self)
        self.comboBoxMunicipio.addItems(
            ["Apodaca","Cadereyta Jimenez","Escobedo","Garcia","Guadalupe","Juarez","Monterrey",
                "Salinas Victoria","San Nicolas de los Garza","San Pedro Garza Garcia",
                "Santa Catarina","Santiago","Cienega de Flores","General Zuazua","Pesqueria"])
        self.comboBoxMunicipio.setCurrentIndex(-1)
        self.comboBoxMunicipio.setFixedWidth(290)
        self.comboBoxMunicipio.setFixedHeight(29)
        self.comboBoxMunicipio.move(400, 95)
        
        
        labelEstado = QLabel("Estado", self)
        labelEstado.setFont(QFont("MS Shell Dlg 2", 9))
        labelEstado.setStyleSheet('color:white')
        labelEstado.move(515, 150)
        self.comboBoxEstado= QComboBox(self)
        self.comboBoxEstado.addItems(["Nuevo Leon"])
        self.comboBoxEstado.setCurrentIndex(-1)
        self.comboBoxEstado.setFixedWidth(290)
        self.comboBoxEstado.setFixedHeight(29)
        self.comboBoxEstado.move(400, 175)
        
        
        labelBeca = QLabel("BECA %",self)
        labelBeca.setFont(QFont("MS Shell Dlg 2", 9))
        labelBeca.setStyleSheet('color:white')
        labelBeca.move(515,240)
        self.radio_cero = QRadioButton('0%',self)
        self.radio_cero.setStyleSheet('color:white')
        self.radio_cero.move(400,270)
        self.radio_25 = QRadioButton('25%',self)
        self.radio_25.setStyleSheet('color:white')
        self.radio_25.move(470,270)
        self.radio_50 = QRadioButton('50%',self)
        self.radio_50.setStyleSheet('color:white')
        self.radio_50.move(540,270)
        self.radio_cien = QRadioButton('100%',self)
        self.radio_cien.setStyleSheet('color:white')
        self.radio_cien.move(610,270)
        
        
        self.Programacionbox = QCheckBox('Progra',self)
        self.Programacionbox.move(380,340)
        self.Programacionbox.setFont(QFont("MS Shell Dlg 2", 9))
        self.Programacionbox.setStyleSheet('color:white')
        label_macion= QLabel("macion", self)
        label_macion.setFont(QFont("MS Shell Dlg 2", 9))
        label_macion.setStyleSheet('color:white')
        label_macion.move(434,340)
        
        self.Contabilidadbox = QCheckBox('Contabilidad',self)
        self.Contabilidadbox.move(500,340)
        self.Contabilidadbox.setFont(QFont("MS Shell Dlg 2", 9))
        self.Contabilidadbox.setStyleSheet('color:white')
        
        self.boxEstadistica = QCheckBox('Estadistica',self)
        self.boxEstadistica.move(610,340)
        self.boxEstadistica.setFont(QFont("MS Shell Dlg 2", 9))
        self.boxEstadistica.setStyleSheet('color:white')
        
        
        self.Basebox = QCheckBox('Base de Datos',self)
        self.Basebox.move(380,370)
        self.Basebox.setFont(QFont("MS Shell Dlg 2", 9))
        self.Basebox.setStyleSheet('color:white')
        
        
        self.Investigacionbox = QCheckBox('Investigación',self)
        self.Investigacionbox.move(500,370)
        self.Investigacionbox.setFont(QFont("MS Shell Dlg 2", 9))
        self.Investigacionbox.setStyleSheet('color:white')
        Investigacion_label = QLabel("de Operaciones", self)
        Investigacion_label.move(595, 370)
        Investigacion_label.setFont(QFont("MS Shell Dlg 2", 9))
        Investigacion_label.setStyleSheet('color:white')
        
                        
if __name__ == '__main__':   
    import sys
    aplicacion = QApplication(sys.argv)
    fuente = QFont()
    fuente.setPointSize(11)
    aplicacion.setFont(fuente)
    window = Ventana_principal()
    window.show()
    sys.exit(aplicacion.exec_())
