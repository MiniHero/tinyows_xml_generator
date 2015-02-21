from PyQt4.QtCore import *
from PyQt4.QtGui import *

import resources_rc

class Plugin:
    def __init__(self, iface):
        self.iface = iface

    def initGui(self):
        self.action = QAction(QIcon(":/tinyows_xml_generator/icons/logo"), "Generate Tinyows xml config file", self.iface.mainWindow())
        QObject.connect(self.action, SIGNAL("triggered()"), self.run)

        if hasattr(self.iface, "addPluginToWebMenu"):
            self.iface.addWebToolBarIcon(self.action)
            self.iface.addPluginToWebMenu("Tinyows XML Generator", self.action)
        else:
            self.iface.addToolBarIcon(self.action)
            self.iface.addPluginToMenu("Tinyows XML Generator", self.action)

    def unload(self):
        if hasattr(self.iface, "removePluginWebMenu"):
            self.iface.removeWebToolBarIcon(self.action)
            self.iface.removePluginWebMenu("Tinyows XML Generator", self.action)
        else:
            self.iface.removeToolBarIcon(self.action)
            self.iface.removePluginMenu("Tinyows XML Generator", self.action)

    def run(self):
        from tinyowsxmlgenerator import TinyowsXmlGenerator
        dialog = TinyowsXmlGenerator(self.iface, self.iface.mainWindow())
        dialog.show()
        dialog.exec_()
