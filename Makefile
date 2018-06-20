pyui:
	pyuic5 -o ./ui/ui_yglian.py ./skin/yglian.ui

app:
	py2applet --make-setup main.py

build:
	python3 setup.py py2app