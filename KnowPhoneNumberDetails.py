from PyQt5.QtWidgets  import *
import phonenumbers
from phonenumbers import timezone
from phonenumbers import geocoder,carrier
import sys
class MainWindow(QWidget):
    def __init__(self):
        self.phoneNumberDetails=""
        QWidget.__init__(self)
        self.setWindowTitle("Get to know the phoneNumber:")
        grid_layout=QGridLayout()
        label=QLabel("Enter PhoneNumber:")
        grid_layout.addWidget(label,10,10)
        self.lineEdit=QLineEdit()
        self.lineEdit.setPlaceholderText("Enter the phoneNumber you whant to know more about:")
        button=QPushButton("Phone Number Details")
        button.clicked.connect(self.get_phone_Details)
        self.textarea=QPlainTextEdit()
        self.textarea.setReadOnly(True)
        self.textarea.setMinimumWidth(550)
        self.textarea.setMinimumHeight(300)
        self.textarea.setWordWrapMode(True)
        grid_layout.addWidget(self.textarea,12,10)
        grid_layout.addWidget(button,12,12)
        grid_layout.addWidget(self.lineEdit,10,12)
        self.setStyleSheet("Background-color:yellow")
        self.setLayout(grid_layout)
    def get_phone_Details(self):
            try:
               self.phoneNumber=self.lineEdit.text()
               phoneNumber=phonenumbers.parse(self.phoneNumber)
               timeZone=timezone.time_zones_for_number(phoneNumber)
               #Phone number network Provider .
               Carrier=carrier.name_for_number(phoneNumber,'en')
               #Phone number Region .
               Location_of_phone_number=geocoder.description_for_number(phoneNumber,'en')
               self.textarea.insertPlainText("Phone number TimeZone:"+str(timeZone))
               self.textarea.appendPlainText(str(phoneNumber))
               self.textarea.appendPlainText(str("Phone Number Network Provider:"+Carrier))
               self.textarea.appendPlainText(str("phone Number Location:"+Location_of_phone_number))

            except phonenumbers.phonenumberutil.NumberParseException:
                alert=QMessageBox()
                alert.setWindowTitle("NumberParseException")
                alert.setText("What you have entered is not event a phoneNumber,Please enter the right phone number")
                alert.exec_()
            
            
        

app=QApplication(sys.argv)
mainwindow=MainWindow()
mainwindow.show()
app.exec_()











