# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mapfileexportdlg.ui'
#
# Created: Sat Feb 21 10:53:35 2015
#      by: PyQt4 UI code generator 4.11.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_TinyowsXmlGenerator(object):
    def setupUi(self, TinyowsXmlGenerator):
        TinyowsXmlGenerator.setObjectName(_fromUtf8("TinyowsXmlGenerator"))
        TinyowsXmlGenerator.resize(729, 606)
        TinyowsXmlGenerator.setSizeGripEnabled(True)
        self.gridLayout = QtGui.QGridLayout(TinyowsXmlGenerator)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.buttonBox = QtGui.QDialogButtonBox(TinyowsXmlGenerator)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Help|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 2)
        self.tabWidget = QtGui.QTabWidget(TinyowsXmlGenerator)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout_3 = QtGui.QGridLayout(self.tab)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_5 = QtGui.QLabel(self.tab)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_3.addWidget(self.label_5, 1, 2, 1, 1)
        self.label_15 = QtGui.QLabel(self.tab)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.gridLayout_3.addWidget(self.label_15, 6, 2, 1, 1)
        self.label_4 = QtGui.QLabel(self.tab)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_3.addWidget(self.label_4, 1, 0, 1, 1)
        self.txtTinyowsLogLevel_2 = QtGui.QLineEdit(self.tab)
        self.txtTinyowsLogLevel_2.setObjectName(_fromUtf8("txtTinyowsLogLevel_2"))
        self.gridLayout_3.addWidget(self.txtTinyowsLogLevel_2, 2, 3, 1, 1)
        self.txtTinyowsOnlineResource = QtGui.QLineEdit(self.tab)
        self.txtTinyowsOnlineResource.setObjectName(_fromUtf8("txtTinyowsOnlineResource"))
        self.gridLayout_3.addWidget(self.txtTinyowsOnlineResource, 1, 1, 1, 1)
        self.txtTinyowsLog = QtGui.QLineEdit(self.tab)
        self.txtTinyowsLog.setObjectName(_fromUtf8("txtTinyowsLog"))
        self.gridLayout_3.addWidget(self.txtTinyowsLog, 2, 1, 1, 1)
        self.txtXmlConfigFilePath = QtGui.QLineEdit(self.tab)
        self.txtXmlConfigFilePath.setText(_fromUtf8(""))
        self.txtXmlConfigFilePath.setObjectName(_fromUtf8("txtXmlConfigFilePath"))
        self.gridLayout_3.addWidget(self.txtXmlConfigFilePath, 0, 1, 1, 1)
        self.txtTinyowsCheckValidGeom = QtGui.QLineEdit(self.tab)
        self.txtTinyowsCheckValidGeom.setObjectName(_fromUtf8("txtTinyowsCheckValidGeom"))
        self.gridLayout_3.addWidget(self.txtTinyowsCheckValidGeom, 5, 3, 1, 1)
        self.txtTinyowsCheckSchema = QtGui.QLineEdit(self.tab)
        self.txtTinyowsCheckSchema.setObjectName(_fromUtf8("txtTinyowsCheckSchema"))
        self.gridLayout_3.addWidget(self.txtTinyowsCheckSchema, 5, 1, 1, 1)
        self.label_9 = QtGui.QLabel(self.tab)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_3.addWidget(self.label_9, 3, 2, 1, 1)
        self.txtTinyowsEstimatedExtent = QtGui.QLineEdit(self.tab)
        self.txtTinyowsEstimatedExtent.setObjectName(_fromUtf8("txtTinyowsEstimatedExtent"))
        self.gridLayout_3.addWidget(self.txtTinyowsEstimatedExtent, 4, 3, 1, 1)
        self.txtTinyowsMeterPrecision = QtGui.QLineEdit(self.tab)
        self.txtTinyowsMeterPrecision.setObjectName(_fromUtf8("txtTinyowsMeterPrecision"))
        self.gridLayout_3.addWidget(self.txtTinyowsMeterPrecision, 3, 3, 1, 1)
        self.txtTinyowsLogLevel = QtGui.QLabel(self.tab)
        self.txtTinyowsLogLevel.setObjectName(_fromUtf8("txtTinyowsLogLevel"))
        self.gridLayout_3.addWidget(self.txtTinyowsLogLevel, 2, 2, 1, 1)
        self.txtTinyowsDegreePrecision = QtGui.QLineEdit(self.tab)
        self.txtTinyowsDegreePrecision.setObjectName(_fromUtf8("txtTinyowsDegreePrecision"))
        self.gridLayout_3.addWidget(self.txtTinyowsDegreePrecision, 3, 1, 1, 1)
        self.txtTinyowsExposePk = QtGui.QLineEdit(self.tab)
        self.txtTinyowsExposePk.setObjectName(_fromUtf8("txtTinyowsExposePk"))
        self.gridLayout_3.addWidget(self.txtTinyowsExposePk, 6, 3, 1, 1)
        self.label_12 = QtGui.QLabel(self.tab)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout_3.addWidget(self.label_12, 5, 0, 1, 1)
        self.txtTinyowsEncoding = QtGui.QLineEdit(self.tab)
        self.txtTinyowsEncoding.setObjectName(_fromUtf8("txtTinyowsEncoding"))
        self.gridLayout_3.addWidget(self.txtTinyowsEncoding, 6, 1, 1, 1)
        self.label_16 = QtGui.QLabel(self.tab)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.gridLayout_3.addWidget(self.label_16, 7, 0, 1, 1)
        self.label_14 = QtGui.QLabel(self.tab)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout_3.addWidget(self.label_14, 6, 0, 1, 1)
        self.label_11 = QtGui.QLabel(self.tab)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout_3.addWidget(self.label_11, 4, 2, 1, 1)
        self.label_6 = QtGui.QLabel(self.tab)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_3.addWidget(self.label_6, 2, 0, 1, 1)
        self.label = QtGui.QLabel(self.tab)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.txtTinyowsSchemaDir = QtGui.QLineEdit(self.tab)
        self.txtTinyowsSchemaDir.setObjectName(_fromUtf8("txtTinyowsSchemaDir"))
        self.gridLayout_3.addWidget(self.txtTinyowsSchemaDir, 1, 3, 1, 1)
        self.label_8 = QtGui.QLabel(self.tab)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_3.addWidget(self.label_8, 3, 0, 1, 1)
        self.label_10 = QtGui.QLabel(self.tab)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_3.addWidget(self.label_10, 4, 0, 1, 1)
        self.label_13 = QtGui.QLabel(self.tab)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.gridLayout_3.addWidget(self.label_13, 5, 2, 1, 1)
        self.txtTinyowsWfsDefaultVersion = QtGui.QLineEdit(self.tab)
        self.txtTinyowsWfsDefaultVersion.setObjectName(_fromUtf8("txtTinyowsWfsDefaultVersion"))
        self.gridLayout_3.addWidget(self.txtTinyowsWfsDefaultVersion, 7, 1, 1, 1)
        self.txtTinyowsDisplayBbox = QtGui.QLineEdit(self.tab)
        self.txtTinyowsDisplayBbox.setObjectName(_fromUtf8("txtTinyowsDisplayBbox"))
        self.gridLayout_3.addWidget(self.txtTinyowsDisplayBbox, 4, 1, 1, 1)
        self.btnChooseFile = QtGui.QToolButton(self.tab)
        self.btnChooseFile.setObjectName(_fromUtf8("btnChooseFile"))
        self.gridLayout_3.addWidget(self.btnChooseFile, 0, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 150, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem, 8, 1, 1, 1)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayout_7 = QtGui.QGridLayout(self.tab_2)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.txtPostgresPassword = QtGui.QLineEdit(self.tab_2)
        self.txtPostgresPassword.setObjectName(_fromUtf8("txtPostgresPassword"))
        self.gridLayout_7.addWidget(self.txtPostgresPassword, 1, 1, 1, 1)
        self.txtPostgresUser = QtGui.QLineEdit(self.tab_2)
        self.txtPostgresUser.setObjectName(_fromUtf8("txtPostgresUser"))
        self.gridLayout_7.addWidget(self.txtPostgresUser, 0, 3, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 300, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.gridLayout_7.addItem(spacerItem1, 3, 0, 1, 3)
        self.label_2 = QtGui.QLabel(self.tab_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_7.addWidget(self.label_2, 0, 0, 1, 1)
        self.txtPostgresDbname = QtGui.QLineEdit(self.tab_2)
        self.txtPostgresDbname.setObjectName(_fromUtf8("txtPostgresDbname"))
        self.gridLayout_7.addWidget(self.txtPostgresDbname, 1, 3, 1, 1)
        self.label_17 = QtGui.QLabel(self.tab_2)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.gridLayout_7.addWidget(self.label_17, 1, 2, 1, 1)
        self.label_7 = QtGui.QLabel(self.tab_2)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_7.addWidget(self.label_7, 1, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.tab_2)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_7.addWidget(self.label_3, 0, 2, 1, 1)
        self.txtPostgresHost = QtGui.QLineEdit(self.tab_2)
        self.txtPostgresHost.setObjectName(_fromUtf8("txtPostgresHost"))
        self.gridLayout_7.addWidget(self.txtPostgresHost, 0, 1, 1, 1)
        self.label_18 = QtGui.QLabel(self.tab_2)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.gridLayout_7.addWidget(self.label_18, 2, 0, 1, 1)
        self.label_19 = QtGui.QLabel(self.tab_2)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.gridLayout_7.addWidget(self.label_19, 2, 2, 1, 1)
        self.txtPostgresPort = QtGui.QLineEdit(self.tab_2)
        self.txtPostgresPort.setObjectName(_fromUtf8("txtPostgresPort"))
        self.gridLayout_7.addWidget(self.txtPostgresPort, 2, 1, 1, 1)
        self.txtPostgresEncoding = QtGui.QLineEdit(self.tab_2)
        self.txtPostgresEncoding.setObjectName(_fromUtf8("txtPostgresEncoding"))
        self.gridLayout_7.addWidget(self.txtPostgresEncoding, 2, 3, 1, 1)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.gridLayout_8 = QtGui.QGridLayout(self.tab_3)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.txtMetadataAccessConstraints = QtGui.QLineEdit(self.tab_3)
        self.txtMetadataAccessConstraints.setObjectName(_fromUtf8("txtMetadataAccessConstraints"))
        self.gridLayout_8.addWidget(self.txtMetadataAccessConstraints, 5, 1, 1, 1)
        self.label_24 = QtGui.QLabel(self.tab_3)
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.gridLayout_8.addWidget(self.label_24, 5, 0, 1, 1)
        self.txtMetadataName = QtGui.QLineEdit(self.tab_3)
        self.txtMetadataName.setObjectName(_fromUtf8("txtMetadataName"))
        self.gridLayout_8.addWidget(self.txtMetadataName, 3, 1, 1, 1)
        self.txtMetadataTitle = QtGui.QLineEdit(self.tab_3)
        self.txtMetadataTitle.setObjectName(_fromUtf8("txtMetadataTitle"))
        self.gridLayout_8.addWidget(self.txtMetadataTitle, 3, 3, 1, 1)
        self.label_22 = QtGui.QLabel(self.tab_3)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.gridLayout_8.addWidget(self.label_22, 4, 0, 1, 1)
        self.txtMetadataKeywords = QtGui.QLineEdit(self.tab_3)
        self.txtMetadataKeywords.setObjectName(_fromUtf8("txtMetadataKeywords"))
        self.gridLayout_8.addWidget(self.txtMetadataKeywords, 4, 1, 1, 1)
        self.label_23 = QtGui.QLabel(self.tab_3)
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.gridLayout_8.addWidget(self.label_23, 4, 2, 1, 1)
        self.txtMetadataFees = QtGui.QLineEdit(self.tab_3)
        self.txtMetadataFees.setObjectName(_fromUtf8("txtMetadataFees"))
        self.gridLayout_8.addWidget(self.txtMetadataFees, 4, 3, 1, 1)
        self.label_20 = QtGui.QLabel(self.tab_3)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.gridLayout_8.addWidget(self.label_20, 3, 0, 1, 1)
        self.label_21 = QtGui.QLabel(self.tab_3)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.gridLayout_8.addWidget(self.label_21, 3, 2, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 300, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.gridLayout_8.addItem(spacerItem2, 6, 1, 1, 1)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.gridLayout_81 = QtGui.QGridLayout(self.tab_4)
        self.gridLayout_81.setObjectName(_fromUtf8("gridLayout_81"))
        self.txtLimitsFeatures = QtGui.QLineEdit(self.tab_4)
        self.txtLimitsFeatures.setObjectName(_fromUtf8("txtLimitsFeatures"))
        self.gridLayout_81.addWidget(self.txtLimitsFeatures, 3, 1, 1, 1)
        self.txtLimitsGeobbox = QtGui.QLineEdit(self.tab_4)
        self.txtLimitsGeobbox.setObjectName(_fromUtf8("txtLimitsGeobbox"))
        self.gridLayout_81.addWidget(self.txtLimitsGeobbox, 3, 3, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(20, 400, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.gridLayout_81.addItem(spacerItem3, 4, 1, 1, 1)
        self.features = QtGui.QLabel(self.tab_4)
        self.features.setObjectName(_fromUtf8("features"))
        self.gridLayout_81.addWidget(self.features, 3, 0, 1, 1)
        self.label_211 = QtGui.QLabel(self.tab_4)
        self.label_211.setObjectName(_fromUtf8("label_211"))
        self.gridLayout_81.addWidget(self.label_211, 3, 2, 1, 1)
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.gridLayout_31 = QtGui.QGridLayout(self.tab_5)
        self.gridLayout_31.setObjectName(_fromUtf8("gridLayout_31"))
        self.txtContactHoursOfService = QtGui.QLineEdit(self.tab_5)
        self.txtContactHoursOfService.setObjectName(_fromUtf8("txtContactHoursOfService"))
        self.gridLayout_31.addWidget(self.txtContactHoursOfService, 6, 3, 1, 1)
        self.txtContactCountry = QtGui.QLineEdit(self.tab_5)
        self.txtContactCountry.setObjectName(_fromUtf8("txtContactCountry"))
        self.gridLayout_31.addWidget(self.txtContactCountry, 6, 1, 1, 1)
        self.txtContactFax = QtGui.QLineEdit(self.tab_5)
        self.txtContactFax.setObjectName(_fromUtf8("txtContactFax"))
        self.gridLayout_31.addWidget(self.txtContactFax, 3, 1, 1, 1)
        self.label_131 = QtGui.QLabel(self.tab_5)
        self.label_131.setObjectName(_fromUtf8("label_131"))
        self.gridLayout_31.addWidget(self.label_131, 4, 2, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(20, 170, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.gridLayout_31.addItem(spacerItem4, 8, 1, 1, 1)
        self.txtContactContactInstructions = QtGui.QLineEdit(self.tab_5)
        self.txtContactContactInstructions.setObjectName(_fromUtf8("txtContactContactInstructions"))
        self.gridLayout_31.addWidget(self.txtContactContactInstructions, 7, 1, 1, 1)
        self.label_26 = QtGui.QLabel(self.tab_5)
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.gridLayout_31.addWidget(self.label_26, 7, 0, 1, 1)
        self.label_81 = QtGui.QLabel(self.tab_5)
        self.label_81.setObjectName(_fromUtf8("label_81"))
        self.gridLayout_31.addWidget(self.label_81, 2, 0, 1, 1)
        self.txtContactPostcode = QtGui.QLineEdit(self.tab_5)
        self.txtContactPostcode.setObjectName(_fromUtf8("txtContactPostcode"))
        self.gridLayout_31.addWidget(self.txtContactPostcode, 4, 3, 1, 1)
        self.txtContactIndividualName = QtGui.QLineEdit(self.tab_5)
        self.txtContactIndividualName.setObjectName(_fromUtf8("txtContactIndividualName"))
        self.gridLayout_31.addWidget(self.txtContactIndividualName, 1, 3, 1, 1)
        self.label_41 = QtGui.QLabel(self.tab_5)
        self.label_41.setObjectName(_fromUtf8("label_41"))
        self.gridLayout_31.addWidget(self.label_41, 0, 0, 1, 1)
        self.txtContactOnlineResource = QtGui.QLineEdit(self.tab_5)
        self.txtContactOnlineResource.setObjectName(_fromUtf8("txtContactOnlineResource"))
        self.gridLayout_31.addWidget(self.txtContactOnlineResource, 3, 3, 1, 1)
        self.txtContactAdministrativeArea = QtGui.QLineEdit(self.tab_5)
        self.txtContactAdministrativeArea.setObjectName(_fromUtf8("txtContactAdministrativeArea"))
        self.gridLayout_31.addWidget(self.txtContactAdministrativeArea, 5, 3, 1, 1)
        self.label_161 = QtGui.QLabel(self.tab_5)
        self.label_161.setObjectName(_fromUtf8("label_161"))
        self.gridLayout_31.addWidget(self.label_161, 6, 0, 1, 1)
        self.label_111 = QtGui.QLabel(self.tab_5)
        self.label_111.setObjectName(_fromUtf8("label_111"))
        self.gridLayout_31.addWidget(self.label_111, 3, 2, 1, 1)
        self.label_61 = QtGui.QLabel(self.tab_5)
        self.label_61.setObjectName(_fromUtf8("label_61"))
        self.gridLayout_31.addWidget(self.label_61, 1, 0, 1, 1)
        self.txtContactPosition = QtGui.QLineEdit(self.tab_5)
        self.txtContactPosition.setObjectName(_fromUtf8("txtContactPosition"))
        self.gridLayout_31.addWidget(self.txtContactPosition, 2, 1, 1, 1)
        self.txtContactAddress = QtGui.QLineEdit(self.tab_5)
        self.txtContactAddress.setObjectName(_fromUtf8("txtContactAddress"))
        self.gridLayout_31.addWidget(self.txtContactAddress, 4, 1, 1, 1)
        self.txtTinyowsLogLevel1 = QtGui.QLabel(self.tab_5)
        self.txtTinyowsLogLevel1.setObjectName(_fromUtf8("txtTinyowsLogLevel1"))
        self.gridLayout_31.addWidget(self.txtTinyowsLogLevel1, 1, 2, 1, 1)
        self.label_151 = QtGui.QLabel(self.tab_5)
        self.label_151.setObjectName(_fromUtf8("label_151"))
        self.gridLayout_31.addWidget(self.label_151, 5, 2, 1, 1)
        self.txtContactEmail = QtGui.QLineEdit(self.tab_5)
        self.txtContactEmail.setObjectName(_fromUtf8("txtContactEmail"))
        self.gridLayout_31.addWidget(self.txtContactEmail, 1, 1, 1, 1)
        self.label_101 = QtGui.QLabel(self.tab_5)
        self.label_101.setObjectName(_fromUtf8("label_101"))
        self.gridLayout_31.addWidget(self.label_101, 3, 0, 1, 1)
        self.label_141 = QtGui.QLabel(self.tab_5)
        self.label_141.setObjectName(_fromUtf8("label_141"))
        self.gridLayout_31.addWidget(self.label_141, 5, 0, 1, 1)
        self.txtContactName = QtGui.QLineEdit(self.tab_5)
        self.txtContactName.setObjectName(_fromUtf8("txtContactName"))
        self.gridLayout_31.addWidget(self.txtContactName, 0, 1, 1, 1)
        self.txtContactPosition_2 = QtGui.QLineEdit(self.tab_5)
        self.txtContactPosition_2.setObjectName(_fromUtf8("txtContactPosition_2"))
        self.gridLayout_31.addWidget(self.txtContactPosition_2, 2, 3, 1, 1)
        self.label_121 = QtGui.QLabel(self.tab_5)
        self.label_121.setObjectName(_fromUtf8("label_121"))
        self.gridLayout_31.addWidget(self.label_121, 4, 0, 1, 1)
        self.txtContactCity = QtGui.QLineEdit(self.tab_5)
        self.txtContactCity.setObjectName(_fromUtf8("txtContactCity"))
        self.gridLayout_31.addWidget(self.txtContactCity, 5, 1, 1, 1)
        self.label_91 = QtGui.QLabel(self.tab_5)
        self.label_91.setObjectName(_fromUtf8("label_91"))
        self.gridLayout_31.addWidget(self.label_91, 2, 2, 1, 1)
        self.label_51 = QtGui.QLabel(self.tab_5)
        self.label_51.setObjectName(_fromUtf8("label_51"))
        self.gridLayout_31.addWidget(self.label_51, 0, 2, 1, 1)
        self.txtContactSite = QtGui.QLineEdit(self.tab_5)
        self.txtContactSite.setObjectName(_fromUtf8("txtContactSite"))
        self.gridLayout_31.addWidget(self.txtContactSite, 0, 3, 1, 1)
        self.label_25 = QtGui.QLabel(self.tab_5)
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.gridLayout_31.addWidget(self.label_25, 6, 2, 1, 1)
        self.tabWidget.addTab(self.tab_5, _fromUtf8(""))
        self.tab_6 = QtGui.QWidget()
        self.tab_6.setObjectName(_fromUtf8("tab_6"))
        self.gridLayout_32 = QtGui.QGridLayout(self.tab_6)
        self.gridLayout_32.setObjectName(_fromUtf8("gridLayout_32"))
        self.txtContactHoursOfService1 = QtGui.QLineEdit(self.tab_6)
        self.txtContactHoursOfService1.setObjectName(_fromUtf8("txtContactHoursOfService1"))
        self.gridLayout_32.addWidget(self.txtContactHoursOfService1, 6, 3, 1, 1)
        self.txtContactCountry1 = QtGui.QLineEdit(self.tab_6)
        self.txtContactCountry1.setObjectName(_fromUtf8("txtContactCountry1"))
        self.gridLayout_32.addWidget(self.txtContactCountry1, 6, 1, 1, 1)
        self.txtContactFax1 = QtGui.QLineEdit(self.tab_6)
        self.txtContactFax1.setObjectName(_fromUtf8("txtContactFax1"))
        self.gridLayout_32.addWidget(self.txtContactFax1, 3, 1, 1, 1)
        self.label_132 = QtGui.QLabel(self.tab_6)
        self.label_132.setObjectName(_fromUtf8("label_132"))
        self.gridLayout_32.addWidget(self.label_132, 4, 2, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(20, 170, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.gridLayout_32.addItem(spacerItem5, 8, 1, 1, 1)
        self.txtContactContactInstructions1 = QtGui.QLineEdit(self.tab_6)
        self.txtContactContactInstructions1.setObjectName(_fromUtf8("txtContactContactInstructions1"))
        self.gridLayout_32.addWidget(self.txtContactContactInstructions1, 7, 1, 1, 1)
        self.label_261 = QtGui.QLabel(self.tab_6)
        self.label_261.setObjectName(_fromUtf8("label_261"))
        self.gridLayout_32.addWidget(self.label_261, 7, 0, 1, 1)
        self.label_82 = QtGui.QLabel(self.tab_6)
        self.label_82.setObjectName(_fromUtf8("label_82"))
        self.gridLayout_32.addWidget(self.label_82, 2, 0, 1, 1)
        self.txtContactPostcode1 = QtGui.QLineEdit(self.tab_6)
        self.txtContactPostcode1.setObjectName(_fromUtf8("txtContactPostcode1"))
        self.gridLayout_32.addWidget(self.txtContactPostcode1, 4, 3, 1, 1)
        self.txtContactIndividualName1 = QtGui.QLineEdit(self.tab_6)
        self.txtContactIndividualName1.setObjectName(_fromUtf8("txtContactIndividualName1"))
        self.gridLayout_32.addWidget(self.txtContactIndividualName1, 1, 3, 1, 1)
        self.label_42 = QtGui.QLabel(self.tab_6)
        self.label_42.setObjectName(_fromUtf8("label_42"))
        self.gridLayout_32.addWidget(self.label_42, 0, 0, 1, 1)
        self.txtContactOnlineResource1 = QtGui.QLineEdit(self.tab_6)
        self.txtContactOnlineResource1.setObjectName(_fromUtf8("txtContactOnlineResource1"))
        self.gridLayout_32.addWidget(self.txtContactOnlineResource1, 3, 3, 1, 1)
        self.txtContactAdministrativeArea1 = QtGui.QLineEdit(self.tab_6)
        self.txtContactAdministrativeArea1.setObjectName(_fromUtf8("txtContactAdministrativeArea1"))
        self.gridLayout_32.addWidget(self.txtContactAdministrativeArea1, 5, 3, 1, 1)
        self.label_162 = QtGui.QLabel(self.tab_6)
        self.label_162.setObjectName(_fromUtf8("label_162"))
        self.gridLayout_32.addWidget(self.label_162, 6, 0, 1, 1)
        self.label_112 = QtGui.QLabel(self.tab_6)
        self.label_112.setObjectName(_fromUtf8("label_112"))
        self.gridLayout_32.addWidget(self.label_112, 3, 2, 1, 1)
        self.label_62 = QtGui.QLabel(self.tab_6)
        self.label_62.setObjectName(_fromUtf8("label_62"))
        self.gridLayout_32.addWidget(self.label_62, 1, 0, 1, 1)
        self.txtContactPosition1 = QtGui.QLineEdit(self.tab_6)
        self.txtContactPosition1.setObjectName(_fromUtf8("txtContactPosition1"))
        self.gridLayout_32.addWidget(self.txtContactPosition1, 2, 1, 1, 1)
        self.txtContactAddress1 = QtGui.QLineEdit(self.tab_6)
        self.txtContactAddress1.setObjectName(_fromUtf8("txtContactAddress1"))
        self.gridLayout_32.addWidget(self.txtContactAddress1, 4, 1, 1, 1)
        self.txtTinyowsLogLevel2 = QtGui.QLabel(self.tab_6)
        self.txtTinyowsLogLevel2.setObjectName(_fromUtf8("txtTinyowsLogLevel2"))
        self.gridLayout_32.addWidget(self.txtTinyowsLogLevel2, 1, 2, 1, 1)
        self.label_152 = QtGui.QLabel(self.tab_6)
        self.label_152.setObjectName(_fromUtf8("label_152"))
        self.gridLayout_32.addWidget(self.label_152, 5, 2, 1, 1)
        self.txtContactEmail1 = QtGui.QLineEdit(self.tab_6)
        self.txtContactEmail1.setObjectName(_fromUtf8("txtContactEmail1"))
        self.gridLayout_32.addWidget(self.txtContactEmail1, 1, 1, 1, 1)
        self.label_102 = QtGui.QLabel(self.tab_6)
        self.label_102.setObjectName(_fromUtf8("label_102"))
        self.gridLayout_32.addWidget(self.label_102, 3, 0, 1, 1)
        self.label_142 = QtGui.QLabel(self.tab_6)
        self.label_142.setObjectName(_fromUtf8("label_142"))
        self.gridLayout_32.addWidget(self.label_142, 5, 0, 1, 1)
        self.txtContactName1 = QtGui.QLineEdit(self.tab_6)
        self.txtContactName1.setObjectName(_fromUtf8("txtContactName1"))
        self.gridLayout_32.addWidget(self.txtContactName1, 0, 1, 1, 1)
        self.txtContactPosition_21 = QtGui.QLineEdit(self.tab_6)
        self.txtContactPosition_21.setObjectName(_fromUtf8("txtContactPosition_21"))
        self.gridLayout_32.addWidget(self.txtContactPosition_21, 2, 3, 1, 1)
        self.label_122 = QtGui.QLabel(self.tab_6)
        self.label_122.setObjectName(_fromUtf8("label_122"))
        self.gridLayout_32.addWidget(self.label_122, 4, 0, 1, 1)
        self.txtContactCity1 = QtGui.QLineEdit(self.tab_6)
        self.txtContactCity1.setObjectName(_fromUtf8("txtContactCity1"))
        self.gridLayout_32.addWidget(self.txtContactCity1, 5, 1, 1, 1)
        self.label_92 = QtGui.QLabel(self.tab_6)
        self.label_92.setObjectName(_fromUtf8("label_92"))
        self.gridLayout_32.addWidget(self.label_92, 2, 2, 1, 1)
        self.label_52 = QtGui.QLabel(self.tab_6)
        self.label_52.setObjectName(_fromUtf8("label_52"))
        self.gridLayout_32.addWidget(self.label_52, 0, 2, 1, 1)
        self.txtContactSite1 = QtGui.QLineEdit(self.tab_6)
        self.txtContactSite1.setObjectName(_fromUtf8("txtContactSite1"))
        self.gridLayout_32.addWidget(self.txtContactSite1, 0, 3, 1, 1)
        self.label_251 = QtGui.QLabel(self.tab_6)
        self.label_251.setObjectName(_fromUtf8("label_251"))
        self.gridLayout_32.addWidget(self.label_251, 6, 2, 1, 1)
        self.tabWidget.addTab(self.tab_6, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 1)
        self.label.setBuddy(self.txtXmlConfigFilePath)

        self.retranslateUi(TinyowsXmlGenerator)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), TinyowsXmlGenerator.reject)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), TinyowsXmlGenerator.accept)
        QtCore.QMetaObject.connectSlotsByName(TinyowsXmlGenerator)
        TinyowsXmlGenerator.setTabOrder(self.txtXmlConfigFilePath, self.txtTinyowsOnlineResource)
        TinyowsXmlGenerator.setTabOrder(self.txtTinyowsOnlineResource, self.txtTinyowsSchemaDir)
        TinyowsXmlGenerator.setTabOrder(self.txtTinyowsSchemaDir, self.txtTinyowsLog)
        TinyowsXmlGenerator.setTabOrder(self.txtTinyowsLog, self.txtTinyowsLogLevel_2)
        TinyowsXmlGenerator.setTabOrder(self.txtTinyowsLogLevel_2, self.txtTinyowsDegreePrecision)
        TinyowsXmlGenerator.setTabOrder(self.txtTinyowsDegreePrecision, self.txtTinyowsMeterPrecision)
        TinyowsXmlGenerator.setTabOrder(self.txtTinyowsMeterPrecision, self.txtTinyowsDisplayBbox)
        TinyowsXmlGenerator.setTabOrder(self.txtTinyowsDisplayBbox, self.txtTinyowsEstimatedExtent)
        TinyowsXmlGenerator.setTabOrder(self.txtTinyowsEstimatedExtent, self.txtTinyowsCheckSchema)
        TinyowsXmlGenerator.setTabOrder(self.txtTinyowsCheckSchema, self.txtTinyowsCheckValidGeom)
        TinyowsXmlGenerator.setTabOrder(self.txtTinyowsCheckValidGeom, self.txtTinyowsEncoding)
        TinyowsXmlGenerator.setTabOrder(self.txtTinyowsEncoding, self.txtTinyowsExposePk)
        TinyowsXmlGenerator.setTabOrder(self.txtTinyowsExposePk, self.txtTinyowsWfsDefaultVersion)
        TinyowsXmlGenerator.setTabOrder(self.txtTinyowsWfsDefaultVersion, self.txtPostgresHost)
        TinyowsXmlGenerator.setTabOrder(self.txtPostgresHost, self.txtPostgresUser)
        TinyowsXmlGenerator.setTabOrder(self.txtPostgresUser, self.txtPostgresPassword)
        TinyowsXmlGenerator.setTabOrder(self.txtPostgresPassword, self.txtPostgresDbname)
        TinyowsXmlGenerator.setTabOrder(self.txtPostgresDbname, self.txtPostgresPort)
        TinyowsXmlGenerator.setTabOrder(self.txtPostgresPort, self.txtPostgresEncoding)
        TinyowsXmlGenerator.setTabOrder(self.txtPostgresEncoding, self.txtMetadataName)
        TinyowsXmlGenerator.setTabOrder(self.txtMetadataName, self.txtMetadataTitle)
        TinyowsXmlGenerator.setTabOrder(self.txtMetadataTitle, self.txtMetadataKeywords)
        TinyowsXmlGenerator.setTabOrder(self.txtMetadataKeywords, self.txtMetadataFees)
        TinyowsXmlGenerator.setTabOrder(self.txtMetadataFees, self.txtMetadataAccessConstraints)
        TinyowsXmlGenerator.setTabOrder(self.txtMetadataAccessConstraints, self.txtLimitsFeatures)
        TinyowsXmlGenerator.setTabOrder(self.txtLimitsFeatures, self.txtLimitsGeobbox)
        TinyowsXmlGenerator.setTabOrder(self.txtLimitsGeobbox, self.txtContactName)
        TinyowsXmlGenerator.setTabOrder(self.txtContactName, self.txtContactSite)
        TinyowsXmlGenerator.setTabOrder(self.txtContactSite, self.txtContactEmail)
        TinyowsXmlGenerator.setTabOrder(self.txtContactEmail, self.txtContactIndividualName)
        TinyowsXmlGenerator.setTabOrder(self.txtContactIndividualName, self.txtContactPosition)
        TinyowsXmlGenerator.setTabOrder(self.txtContactPosition, self.txtContactPosition_2)
        TinyowsXmlGenerator.setTabOrder(self.txtContactPosition_2, self.txtContactFax)
        TinyowsXmlGenerator.setTabOrder(self.txtContactFax, self.txtContactOnlineResource)
        TinyowsXmlGenerator.setTabOrder(self.txtContactOnlineResource, self.txtContactAddress)
        TinyowsXmlGenerator.setTabOrder(self.txtContactAddress, self.txtContactPostcode)
        TinyowsXmlGenerator.setTabOrder(self.txtContactPostcode, self.txtContactCity)
        TinyowsXmlGenerator.setTabOrder(self.txtContactCity, self.txtContactAdministrativeArea)
        TinyowsXmlGenerator.setTabOrder(self.txtContactAdministrativeArea, self.txtContactCountry)
        TinyowsXmlGenerator.setTabOrder(self.txtContactCountry, self.txtContactHoursOfService)
        TinyowsXmlGenerator.setTabOrder(self.txtContactHoursOfService, self.txtContactContactInstructions)
        TinyowsXmlGenerator.setTabOrder(self.txtContactContactInstructions, self.txtContactName)
        TinyowsXmlGenerator.setTabOrder(self.txtContactName, self.txtContactSite)
        TinyowsXmlGenerator.setTabOrder(self.txtContactSite, self.txtContactEmail)
        TinyowsXmlGenerator.setTabOrder(self.txtContactEmail, self.txtContactIndividualName)
        TinyowsXmlGenerator.setTabOrder(self.txtContactIndividualName, self.txtContactPosition)
        TinyowsXmlGenerator.setTabOrder(self.txtContactPosition, self.txtContactPosition_2)
        TinyowsXmlGenerator.setTabOrder(self.txtContactPosition_2, self.txtContactFax)
        TinyowsXmlGenerator.setTabOrder(self.txtContactFax, self.txtContactOnlineResource)
        TinyowsXmlGenerator.setTabOrder(self.txtContactOnlineResource, self.txtContactAddress)
        TinyowsXmlGenerator.setTabOrder(self.txtContactAddress, self.txtContactPostcode)
        TinyowsXmlGenerator.setTabOrder(self.txtContactPostcode, self.txtContactCity)
        TinyowsXmlGenerator.setTabOrder(self.txtContactCity, self.txtContactAdministrativeArea)
        TinyowsXmlGenerator.setTabOrder(self.txtContactAdministrativeArea, self.txtContactCountry)
        TinyowsXmlGenerator.setTabOrder(self.txtContactCountry, self.txtContactHoursOfService)
        TinyowsXmlGenerator.setTabOrder(self.txtContactHoursOfService, self.txtContactContactInstructions)
        TinyowsXmlGenerator.setTabOrder(self.txtContactContactInstructions, self.tabWidget)
        TinyowsXmlGenerator.setTabOrder(self.tabWidget, self.btnChooseFile)

    def retranslateUi(self, TinyowsXmlGenerator):
        TinyowsXmlGenerator.setWindowTitle(_translate("TinyowsXmlGenerator", "TinyOws XML Generator", None))
        self.label_5.setText(_translate("TinyowsXmlGenerator", "schema_dir*", None))
        self.label_15.setText(_translate("TinyowsXmlGenerator", "expose_pk", None))
        self.label_4.setText(_translate("TinyowsXmlGenerator", "online_resource*", None))
        self.txtXmlConfigFilePath.setToolTip(_translate("TinyowsXmlGenerator", "Name for the map file to be created from the QGIS project file", None))
        self.label_9.setText(_translate("TinyowsXmlGenerator", "meter_precision", None))
        self.txtTinyowsLogLevel.setText(_translate("TinyowsXmlGenerator", "log_level", None))
        self.label_12.setText(_translate("TinyowsXmlGenerator", "check_schema", None))
        self.label_16.setText(_translate("TinyowsXmlGenerator", "wfs_default_version", None))
        self.label_14.setText(_translate("TinyowsXmlGenerator", "encoding", None))
        self.label_11.setText(_translate("TinyowsXmlGenerator", "estimated_extent", None))
        self.label_6.setText(_translate("TinyowsXmlGenerator", "log", None))
        self.label.setText(_translate("TinyowsXmlGenerator", "XML config file", None))
        self.label_8.setText(_translate("TinyowsXmlGenerator", "degree_precision", None))
        self.label_10.setText(_translate("TinyowsXmlGenerator", "display_bbox", None))
        self.label_13.setText(_translate("TinyowsXmlGenerator", "check_valid_geom", None))
        self.btnChooseFile.setText(_translate("TinyowsXmlGenerator", "...", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("TinyowsXmlGenerator", "Tinyows", None))
        self.label_2.setText(_translate("TinyowsXmlGenerator", "host", None))
        self.label_17.setText(_translate("TinyowsXmlGenerator", "dbname", None))
        self.label_7.setText(_translate("TinyowsXmlGenerator", "password", None))
        self.label_3.setText(_translate("TinyowsXmlGenerator", "user", None))
        self.label_18.setText(_translate("TinyowsXmlGenerator", "port", None))
        self.label_19.setText(_translate("TinyowsXmlGenerator", "encoding", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("TinyowsXmlGenerator", "Postgresql", None))
        self.label_24.setText(_translate("TinyowsXmlGenerator", "access_constraints", None))
        self.label_22.setText(_translate("TinyowsXmlGenerator", "keywords", None))
        self.label_23.setText(_translate("TinyowsXmlGenerator", "fees", None))
        self.label_20.setText(_translate("TinyowsXmlGenerator", "name*", None))
        self.label_21.setText(_translate("TinyowsXmlGenerator", "title*", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("TinyowsXmlGenerator", "Metadata", None))
        self.features.setText(_translate("TinyowsXmlGenerator", "features", None))
        self.label_211.setText(_translate("TinyowsXmlGenerator", "geobbox", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("TinyowsXmlGenerator", "Limits", None))
        self.label_131.setText(_translate("TinyowsXmlGenerator", "postcode", None))
        self.label_26.setText(_translate("TinyowsXmlGenerator", "contact_instructions", None))
        self.label_81.setText(_translate("TinyowsXmlGenerator", "position", None))
        self.label_41.setText(_translate("TinyowsXmlGenerator", "name*", None))
        self.label_161.setText(_translate("TinyowsXmlGenerator", "country", None))
        self.label_111.setText(_translate("TinyowsXmlGenerator", "online_resource", None))
        self.label_61.setText(_translate("TinyowsXmlGenerator", "email*", None))
        self.txtTinyowsLogLevel1.setText(_translate("TinyowsXmlGenerator", "individual_name", None))
        self.label_151.setText(_translate("TinyowsXmlGenerator", "administrative_area", None))
        self.label_101.setText(_translate("TinyowsXmlGenerator", "fax", None))
        self.label_141.setText(_translate("TinyowsXmlGenerator", "city", None))
        self.label_121.setText(_translate("TinyowsXmlGenerator", "address", None))
        self.label_91.setText(_translate("TinyowsXmlGenerator", "phone", None))
        self.label_51.setText(_translate("TinyowsXmlGenerator", "site*", None))
        self.label_25.setText(_translate("TinyowsXmlGenerator", "hours_of_service", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("TinyowsXmlGenerator", "Contact", None))
        self.label_132.setText(_translate("TinyowsXmlGenerator", "postcode", None))
        self.label_261.setText(_translate("TinyowsXmlGenerator", "contact_instructions", None))
        self.label_82.setText(_translate("TinyowsXmlGenerator", "position", None))
        self.label_42.setText(_translate("TinyowsXmlGenerator", "name*", None))
        self.label_162.setText(_translate("TinyowsXmlGenerator", "country", None))
        self.label_112.setText(_translate("TinyowsXmlGenerator", "online_resource", None))
        self.label_62.setText(_translate("TinyowsXmlGenerator", "email*", None))
        self.txtTinyowsLogLevel2.setText(_translate("TinyowsXmlGenerator", "individual_name", None))
        self.label_152.setText(_translate("TinyowsXmlGenerator", "administrative_area", None))
        self.label_102.setText(_translate("TinyowsXmlGenerator", "fax", None))
        self.label_142.setText(_translate("TinyowsXmlGenerator", "city", None))
        self.label_122.setText(_translate("TinyowsXmlGenerator", "address", None))
        self.label_92.setText(_translate("TinyowsXmlGenerator", "phone", None))
        self.label_52.setText(_translate("TinyowsXmlGenerator", "site*", None))
        self.label_251.setText(_translate("TinyowsXmlGenerator", "hours_of_service", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("TinyowsXmlGenerator", "Layer", None))

