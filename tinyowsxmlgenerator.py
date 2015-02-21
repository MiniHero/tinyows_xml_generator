from PyQt4.QtCore import *
from PyQt4.QtGui import *

from qgis.core import *
from qgis.gui import *

from .ui.interface import Ui_TinyowsXmlGenerator

_toUtf8 = lambda s: unicode(s).encode('utf8')


class TinyowsXmlGenerator(QDialog, Ui_TinyowsXmlGenerator):

    def __init__(self, iface, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.iface = iface
        self.canvas = self.iface.mapCanvas()
        self.legend = self.iface.legendInterface()

        QObject.connect( self.btnChooseFile, SIGNAL("clicked()"), self.selectXmlConfigFile )

    def selectXmlConfigFile(self):
        # retrieve the last used map file path
        settings = QSettings()
        lastUsedFile = settings.value("/rt_mapserver_exporter/lastUsedFile", "", type=str)

        # ask for choosing where to store the map file
        filename = QFileDialog.getSaveFileName(self, "Select where to save the xml config file", lastUsedFile, "XmlFile (*.xml)")
        if filename == "":
            return

        # store the last used map file path
        settings.setValue("/rt_mapserver_exporter/lastUsedFile", filename)
        # update the displayd path
        self.txtXmlConfigFilePath.setText( filename )

    def accept(self):
        # check user inputs
        if self.txtXmlConfigFilePath.text() == "":
            QMessageBox.warning(self, "Tinyows xml generator", "xml output path is required")
            return
        
#         if(self.txtTinyowsOnlineResource.text() == ""):
#         if(self.txtTinyowsSchemaDir.text() == ""):
#         if(self.txtTinyowsLog.text() == ""):
#         if(self.txtTinyowsLogLevel.text() == ""):
#         if(self.txtTinyowsDegreePrecision.text() == ""):
#         if(self.txtTinyowsMeterPrecision.text() == ""):
#         if(self.txtTinyowsDisplayBbox.text() == ""):
#         if(self.txtTinyowsEstimatedExtent.text() == ""):
#         if(self.txtTinyowsCheckSchema.text() == ""):
#         if(self.txtTinyowsCheckValidGeom.text() == ""):
#         if(self.txtTinyowsEncoding.text() == ""):
#         if(self.txtTinyowsExposePk.text() == ""):
#         if(self.txtTinyowsWfsDefaultVersion.text() == ""):
#             
#         
#         if(self.txtTinyowsWfsDefaultVersion.text() == ""):
#         if(self.txtTinyowsWfsDefaultVersion.text() == ""):
#         if(self.txtTinyowsWfsDefaultVersion.text() == ""):
#         if(self.txtTinyowsWfsDefaultVersion.text() == ""):
#         if(self.txtTinyowsWfsDefaultVersion.text() == ""):
#         if(self.txtTinyowsWfsDefaultVersion.text() == ""):
#             
#             
#         if(self.txtTinyowsWfsDefaultVersion.text() == ""):
#         if(self.txtTinyowsWfsDefaultVersion.text() == ""):
#         if(self.txtTinyowsWfsDefaultVersion.text() == ""):
#         if(self.txtTinyowsWfsDefaultVersion.text() == ""):
#         if(self.txtTinyowsWfsDefaultVersion.text() == ""):
#         
#         
#         if(self.txtTinyowsWfsDefaultVersion.text() == ""):
#         if(self.txtTinyowsWfsDefaultVersion.text() == ""):
#             
#         
#         if(self.txtTinyowsWfsDefaultVersion.text() == ""):
#         if(self.txtTinyowsWfsDefaultVersion.text() == ""):
#         if(self.txtTinyowsWfsDefaultVersion.text() == ""):
#         if(self.txtTinyowsWfsDefaultVersion.text() == ""):
#         if(self.txtTinyowsWfsDefaultVersion.text() == ""):
#         if(self.txtTinyowsWfsDefaultVersion.text() == ""):
#         if(self.txtTinyowsWfsDefaultVersion.text() == ""):
#         if(self.txtTinyowsWfsDefaultVersion.text() == ""):
#         if(self.txtTinyowsWfsDefaultVersion.text() == ""):
#         if(self.txtTinyowsWfsDefaultVersion.text() == ""):
#         if(self.txtTinyowsWfsDefaultVersion.text() == ""):
#         if(self.txtTinyowsWfsDefaultVersion.text() == ""):
#         if(self.txtTinyowsWfsDefaultVersion.text() == ""):
#         if(self.txtTinyowsWfsDefaultVersion.text() == ""):
#         if(self.txtTinyowsWfsDefaultVersion.text() == ""):
