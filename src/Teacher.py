from PyQt5.QtSql import QSqlQueryModel
from PyQt5.QtCore import QObject, pyqtSlot
from PyQt5.QtWidgets import (
    QTableView,
    QWidget,
    QMessageBox,
    QDialog,
    QLabel,
    QLineEdit,
    QTextEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout
)


class TeacherModel(QSqlQueryModel):

    def __init__(self, parent: QObject | None = ...) -> None:
        super().__init__(parent)
        sql = '''
            select id, full_name, phone, email, comment
            from teachers;
        '''
        self.setQuery(sql)


class TeacherView(QTableView):

    def __init__(self, parent: QWidget | None = ...) -> None:
        super().__init__(parent)
        model = TeacherModel(self)
        self.setModel(model)

    @pyqtSlot()
    def add(self):
        dialog = TeacherDialog(self)
        dialog.exec()

    @pyqtSlot()
    def update(self):
        QMessageBox.information(self, "Учитель", "Редактироваие")

    @pyqtSlot()
    def delete(self):
        QMessageBox.information(self, "Учитель", "Удаление")


class TeacherDialog(QDialog):

    def __init__(self, parent: QWidget | None = ...) -> None:
        super().__init__(parent)

        full_name_lbl = QLabel("&ФИО", parent=self)
        self.__full_name_edit = QLineEdit(parent=self)
        full_name_lbl.setBuddy(self.__full_name_edit)

        phone_lbl = QLabel("&Телефон", parent=self)
        self.__phone_edit = QLineEdit(parent=self)
        phone_lbl.setBuddy(self.__phone_edit)

        email_lbl = QLabel("&Email", parent=self)
        self.__email_edit = QLineEdit(parent=self)
        email_lbl.setBuddy(self.__email_edit)

        comment_lbl = QLabel("&Примечание", parent=self)
        self.__comment_edit = QTextEdit(parent=self)
        comment_lbl.setBuddy(self.__comment_edit)

        ok_btn = QPushButton("ОК", parent=self)
        cancel_btn = QPushButton("Отмена", parent=self)

        layout = QVBoxLayout()
        layout.addWidget(full_name_lbl)
        layout.addWidget(self.__full_name_edit)
        layout.addWidget(phone_lbl)
        layout.addWidget(self.__phone_edit)
        layout.addWidget(email_lbl)
        layout.addWidget(self.__email_edit)
        layout.addWidget(comment_lbl)
        layout.addWidget(self.__comment_edit)

        btn_layout = QHBoxLayout()
        btn_layout.addWidget(ok_btn)
        btn_layout.addWidget(cancel_btn)
        layout.addLayout(btn_layout)

        self.setLayout(layout)

        ok_btn.clicked.connect(self.finish)
        cancel_btn.clicked.connect(self.reject)

    @pyqtSlot()
    def finish(self):
        if self.full_name is None:
            return
        self.accept()

    @property
    def full_name(self):
        result = self.__full_name_edit.text().strip()
        return None if result == '' else result

    @property
    def phone(self):
        result = self.__phone_edit.text().strip()
        return None if result == '' else result

    @property
    def email(self):
        result = self.__email_edit.text().strip()
        return None if result == '' else result

    @property
    def comment(self):
        result = self.__comment_edit.toPlainText().strip()
        return None if result == '' else result
