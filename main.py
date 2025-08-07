from PyQt6 import uic, QtWidgets
from functions import *
from mainApp import Ui_Form


class Ui(QtWidgets.QDialog, Ui_Form):
    def __init__(self):
        super(Ui, self).__init__()
        self.setupUi(self)
        self.btn.clicked.connect(self.btnPressed)
        self.btn_tab2.clicked.connect(self.btnPressedTab2)
        self.btn_tab3.clicked.connect(self.btnPressedTab3)
        self.btn_numeration.clicked.connect(self.btnPressedUtilitiesTab1)
        self.btn_style.clicked.connect(self.btnPressedStyle)
        self.btn_matches_from_groups.clicked.connect(self.btnPressedGetMatches)
        self.setStyleSheet(get_style_properties(get_style()))

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
        team_names = [i for i in self.textEdit_teams_tab3.toPlainText().split('\n') if len(i) > 2 and '@' not in i]
        number = self.spinBox_2.value()
        groups = get_groups(team_names, number)
        self.textEdit_groups_tab3.setPlainText(groups)
        return

    def btnPressedUtilitiesTab1(self):
        players = [i for i in self.textEdit_input_utilities_tab1.toPlainText().split('\n') if len(i) != 0]
        players = [i.replace('.', '. ') for i in players]
        if self.radioButton.isChecked():
            result = delete_numeration(players)
        else:
            result = add_numeration(players)
        self.textEdit_output_utilities_tab1.setPlainText(result)
        return

    def btnPressedGetMatches(self):
        text = self.textEdit_groups_uti_tab2.toPlainText()
        result = groups_into_matches(text)
        self.textEdit_matches_uti_tab2.setPlainText(result)
        return

    def btnPressedStyle(self):
        picked_style = str(self.comboBox_style.currentText())
        if picked_style == 'Dark Blue':
            self.setStyleSheet(get_style_properties('dark-blue'))
            save_style('dark-blue')
        elif picked_style == 'Dark Orange':
            self.setStyleSheet(get_style_properties('dark-orange'))
            save_style('dark-orange')
        else:
            self.setStyleSheet('')
            save_style('none')
        return


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = Ui()
    w.show()
    sys.exit(app.exec())
