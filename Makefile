pyui:
	pyuic5 -o ./ui/ui_remix.py ./skin/remix.ui

app:
	py2applet --make-setup main.py

build:
	python3 setup.py py2app