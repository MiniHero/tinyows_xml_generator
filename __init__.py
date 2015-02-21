def name():
	return "Tinyows XMl Generator"

def description():
	return "Generate Tinyows xml config file"

def author():
	return "Yuchuan Zhou"

def icon():
	return "icons/logo.png"

def version():
	return "0.1"

def qgisMinimumVersion():
	return "2.0"

def classFactory(iface):
	from .plugin import Plugin
	return Plugin(iface)

