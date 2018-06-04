pyui:
	pyuic5 -o helloworld.py helloworld.uipip

app:
	py2applet --make-setup main.py

build:
	python3 setup.py py2app