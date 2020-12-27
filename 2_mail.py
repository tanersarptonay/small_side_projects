import sys
import os
from PyQt5.QtWidgets import QWidget,QApplication,QLabel,QPushButton,QVBoxLayout,QHBoxLayout,QTextEdit,QFileDialog,QLineEdit,QGridLayout, QDialog
from PyQt5.QtWidgets import qApp,QAction,QMainWindow

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Login_Window(QDialog):

    def __init__(self):
        super().__init__()

        self.init_ui()


    def init_ui(self):

        self.label1 = QLabel("E-Mail:")
        self.label2 = QLabel("Password:")
        self.email = QLineEdit()
        self.password = QLineEdit()
        self.login_button = QPushButton("Login")
        self.exit_button = QPushButton("Exit")

        grid_button = QGridLayout()

        grid_button.addWidget(self.login_button, 0, 0)
        grid_button.addWidget(self.exit_button, 0 , 1)

        grid = QGridLayout()

        grid.addWidget(self.label1, 0, 0)
        grid.addWidget(self.label2, 1, 0)
        grid.addWidget(self.email, 0, 1)
        grid.addWidget(self.password, 1, 1)
        grid.addLayout(grid_button, 2, 0, 1, 2)

        h_box = QHBoxLayout()

        h_box.addStretch()
        h_box.addLayout(grid)
        h_box.addStretch()

        v_box = QVBoxLayout()

        v_box.addStretch()
        v_box.addLayout(h_box)
        v_box.addStretch()

        self.setLayout(v_box)



class Mail_Window(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()


    def init_ui(self):
        self.text_area = QTextEdit()
        self.label1 = QLabel("To whom:")
        self.label2 = QLabel("Subject:")
        self.whom = QLineEdit()
        self.subject = QLineEdit()

        grid = QGridLayout()

        grid.addWidget(self.label1, 0, 0)
        grid.addWidget(self.whom, 0, 1)
        grid.addWidget(self.label2, 1, 0)
        grid.addWidget(self.subject, 1, 1)
        grid.addWidget(self.text_area, 2, 0, 1, 2)
        grid.setRowStretch(0, 1)
        grid.setRowStretch(1, 3)
        grid.setRowStretch(2, 3)

        self.setLayout(grid)



class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.start_login_window()


    def start_login_window(self):
        self.login_window = Login_Window()

        self.setWindowTitle("Login")

        self.setCentralWidget(self.login_window)

        self.login_window.login_button.clicked.connect(self.start_mail_window)

        self.login_window.exit_button.clicked.connect(self.exiter)

        self.show()


    def start_mail_window(self):

        self.email_adress = self.login_window.email.text()
        self.password_code = self.login_window.password.text()

        self.mail_window = Mail_Window()

        self.setWindowTitle("SarpMail")

        self.setCentralWidget(self.mail_window)

        menubar = self.menuBar()

        open_file = QAction("Open File", self)
        janitor = QAction("Clean", self)
        send = QAction("Send", self)

        menubar.addAction(open_file)
        menubar.addAction(send)
        menubar.addAction(janitor)

        open_file.triggered.connect(self.func_open)
        janitor.triggered.connect(self.func_janitor)
        send.triggered.connect(self.mail_sender)

        self.show()


    def exiter(self):
        qApp.quit()


    def func_open(self):
        file_name = QFileDialog.getOpenFileName(self, "Open File", os.getenv("Desktop"))

        with open(file_name[0], "r", encoding="utf-8") as file:
            self.mail_window.text_area.setText(file.read())


    def func_janitor(self):
        self.mail_window.text_area.clear()


    def mail_sender(self):
        message = MIMEMultipart()

        message["From"] = self.email_adress

        message["To"] = self.mail_window.whom.text()

        message["Subject"] = self.mail_window.subject.text()

        text = self.mail_window.text_area.toPlainText()

        body = MIMEText(text, "plain")

        message.attach(body)


        mail = smtplib.SMTP("smtp.gmail.com", 587)

        mail.ehlo()

        mail.starttls()

        mail.login(self.email_adress, self.password_code)

        mail.sendmail(message["From"], message["To"],  message.as_string())

        print("Your mail has been sent to {}".format(self.mail_window.whom.text()))

        mail.close()





def run():
    app = QApplication(sys.argv)

    lo = MainWindow()

    sys.exit(app.exec_())

run()