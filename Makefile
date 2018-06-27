pyui:
	pyuic5 -o ./ui/pyui/ui_main.py ./skin/main.ui
	pyrcc5 -o ./ui/pyui/icons_rc.py ./res/icons.qrc
app:
	py2applet --make-setup main.py

build:
	pyinstaller --noconfirm --clean main.py

relse:
	pyinstaller --distpath=out  \
              --workpath=out/build  \
              --hidden-import=cytoolz._signatures\
              --hidden-import=cytoolz.utils\
              --paths=./ui/pyui/\
              --specpath=out  \
              --noconfirm \
              --clean\
              -n Yglian \
              -a\
              -Fw main.py  \
              --icon res/tools.icns\
