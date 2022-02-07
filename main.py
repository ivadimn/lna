from PyQt6.QtWidgets import QApplication
from PyQt6 import QtSql


from ui.MainWindow import MainWindow

app = QApplication([])
window = MainWindow()
window.show()

conn = QtSql.QSqlDatabase.addDatabase("QSQLITE")
conn.setDatabaseName("lna.db")
conn.open()
query = QtSql.QSqlQuery()

query.exec("Select name From org_units;")
query.first()
while query.isValid():
    print(query.value(0))
    query.next()

conn.close()
app.exec()





