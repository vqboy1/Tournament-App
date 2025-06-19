from PyQt6 import uic, QtWidgets
from functions import get_teams, get_net, delete_numeration, add_numeration
from mainApp import Ui_Form


class Ui(QtWidgets.QDialog, Ui_Form):
    def __init__(self):
        super(Ui, self).__init__()
        self.setupUi(self)
        self.btn.clicked.connect(self.btnPressed)
        self.btn_tab2.clicked.connect(self.btnPressedTab2)
        self.btn_tab3.clicked.connect(self.btnPressedTab3)

    def btnPressed(self):
        players = [i for i in self.textEdit_players.toPlainText().split()]
        number = self.spinBox.value()
        teams = get_teams(players, number)
        self.textEdit_teams.setPlainText(teams)
        return

    def btnPressedTab2(self):
        teams_tab2 = [i for i in self.textEdit_teams_tab2.toPlainText().split('\n') if 'TEAM' in i]
        net = get_net(teams_tab2)
        self.textEdit_net_tab2.setPlainText(net)
        return

    def btnPressedTab3(self):
        players = [i for i in self.textEdit_input_tab3.toPlainText().split('\n') if len(i) != 0]
        if self.radioButton_1.isChecked():
            result = delete_numeration(players)
        else:
            result = add_numeration(players)
        self.textEdit_output_tab3.setPlainText(result)
        return


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = Ui()
    w.show()
    sys.exit(app.exec())
