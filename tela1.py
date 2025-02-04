import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QComboBox, QVBoxLayout, QHBoxLayout


class FinalizarVenda(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Finalizar Venda")
        self.setGeometry(100, 100, 500, 400)

        layout = QVBoxLayout()

        # Campos de valores
        layout.addWidget(QLabel("Total da Venda:"))
        self.total_venda = QLineEdit()
        layout.addWidget(self.total_venda)

        layout.addWidget(QLabel("Desconto:"))
        self.desconto = QLineEdit()
        layout.addWidget(self.desconto)

        layout.addWidget(QLabel("Acréscimo:"))
        self.acrescimo = QLineEdit()
        layout.addWidget(self.acrescimo)

        layout.addWidget(QLabel("Total Líquido:"))
        self.total_liquido = QLineEdit()
        layout.addWidget(self.total_liquido)

        layout.addWidget(QLabel("Troco:"))
        self.troco = QLineEdit()
        layout.addWidget(self.troco)

        # Informações do cliente e vendedor
        layout.addWidget(QLabel("Cliente: 1 - CONSUMIDOR FINAL"))
        layout.addWidget(QLabel("Vendedor: 999 - SYNDATA"))

        # Forma de pagamento
        layout.addWidget(QLabel("Forma de Pagamento:"))
        self.forma_pagamento = QComboBox()
        self.forma_pagamento.addItems(["1-DINHEIRO", "2-CARTÃO", "3-PIX"])
        layout.addWidget(self.forma_pagamento)

        # Botões de ação (linha única)
        hbox_botoes = QHBoxLayout()
        self.btn_sair = QPushButton("Sair (Esc)")
        self.btn_cupom = QPushButton("Cupom Fiscal (F6)")
        self.btn_pedido = QPushButton("Pedido de Venda (F7)")
        self.btn_nfc_online = QPushButton("NFC-e Online (F8)")
        self.btn_nfc_offline = QPushButton("NFC-e Offline (F9)")

        hbox_botoes.addWidget(self.btn_sair)
        hbox_botoes.addWidget(self.btn_cupom)
        hbox_botoes.addWidget(self.btn_pedido)
        hbox_botoes.addWidget(self.btn_nfc_online)
        hbox_botoes.addWidget(self.btn_nfc_offline)

        layout.addLayout(hbox_botoes)

        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FinalizarVenda()
    window.show()
    sys.exit(app.exec_())
