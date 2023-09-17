from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QTextEdit
from PyQt5.QtCore import Qt
import sys
import random
'''
可视化猜数字游戏：
1.有四个数字，
2.如果位置和数字正确则显示绿色，如果位置不对但是数字正确则显示黄色，如果位置和数字都不对则显示红色，
3.有四次机会
4.直接输入即可
'''
class GuessNumberGame(QWidget):
    def __init__(self):
        super().__init__()
        self.answer = str(random.randint(1000, 9999))
        self.attempts = 4
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()
        self.label = QLabel("请输入你的猜测（四位数）：")
        self.textEdit = QTextEdit()
        self.textEdit.setFixedHeight(30)
        # self.textEdit.setFixedWidth(200)
        self.button = QPushButton("提交")
        self.resultLabel = QLabel()
        self.attemptsLabel = QLabel("剩余尝试次数：4")
        self.historyLabel = QLabel("历史结果：")

        self.historyTextEdit = QTextEdit()
        self.historyTextEdit.setFixedHeight(85)
        self.restartButton = QPushButton("重新开始")

        self.button.clicked.connect(self.check_guess)
        self.restartButton.clicked.connect(self.restart_game)

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.textEdit)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.resultLabel)
        self.layout.addWidget(self.attemptsLabel)
        self.layout.addWidget(self.historyLabel)
        self.layout.addWidget(self.historyTextEdit)
        self.layout.addWidget(self.restartButton)

        self.setLayout(self.layout)

    def check_guess(self):
        guess = self.textEdit.toPlainText()
        if len(guess) != 4:
            self.resultLabel.setText("请输入四位数")
            return
        colors = []
        for g, a in zip(guess, self.answer):
            if g == a:
                colors.append("<font color='green'>{}</font>".format(g))
            elif g in self.answer:
                colors.append("<font color='orange'>{}</font>".format(g))
            else:
                colors.append("<font color='red'>{}</font>".format(g))
        result = ''.join(colors)
        self.resultLabel.setText(result)
        self.historyTextEdit.append(result)
        if guess == self.answer:
            self.resultLabel.setText("<font color='green'>恭喜你，猜对了！</font>")
        else:
            self.attempts -= 1
            self.attemptsLabel.setText("剩余尝试次数：" + str(self.attempts))
            if self.attempts == 0:
                self.resultLabel.setText("<font color='red'>很遗憾，你没有机会了。正确答案是 " + self.answer + "</font>")

    def restart_game(self):
        self.answer = str(random.randint(1000, 9999))
        self.attempts = 4
        self.attemptsLabel.setText("剩余尝试次数：4")
        self.resultLabel.clear()
        self.historyTextEdit.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GuessNumberGame()
    ex.show()
    sys.exit(app.exec_())