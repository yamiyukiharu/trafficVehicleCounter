import os

# os.system('pyside2-rcc -o icons_rc.py ./qt/icons/icons.qrc')
os.system('pyside2-uic -g python -o ./qt/Ui_Form.py ./qt/form.ui')