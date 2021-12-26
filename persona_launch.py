from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6 import *
from PySide6 import QtCore
import sys
from persona5_login import Ui_loginWidget
from final_main import Ui_personaApp

class loginApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.main = Ui_loginWidget()
        self.main.setupUi(self)
        self.loginButton = self.main.loginButton
        self.mask_image= self.main.image
        self.password = self.main.password
        self.password.setFont(QFont("p5hatty", 26))
        
        self.close_button = self.main.closeButton
        self.minimize_button = self.main.closeButton_2
        self.hideTitleBar()

        self.loginButton.clicked.connect(self.frameTimer)
        self.close_button.clicked.connect(lambda: self.close())
        self.minimize_button.clicked.connect(lambda: self.showMinimized())
        
        self.setMaximumSize(self.width(), self.height())
        self.setMinimumSize(self.width(), self.height())
        
        self.main.image.setPixmap(QPixmap("images/logo.png"))
        
    def frameTimer(self):
        self.timer = QTimer(self)
        self.loadingFramesTimer()
        self.UIFramesTimer()
        self.changeUIColorTimer()
    
    def loadingFramesTimer(self):
        int_arg_1 = 100
        
        self.timer.singleShot(int_arg_1, lambda: self.mask_image.setPixmap(
            QPixmap(u"images\mask_2.png")))
        self.timer.singleShot(int_arg_1 * 2, lambda: self.mask_image.setPixmap(
            QPixmap(u"images\mask_3.png")))
        self.timer.singleShot(int_arg_1 * 4, lambda: self.mask_image.setPixmap(
            QPixmap(u"images\mask_2.png")))
        self.timer.singleShot(int_arg_1 * 6, lambda: self.mask_image.setPixmap(
            QPixmap(u"images\mask_3.png")))
        self.timer.singleShot(int_arg_1 * 8, lambda: self.mask_image.setPixmap(
            QPixmap(u"images\mask_2.png")))
        self.timer.singleShot(int_arg_1 * 10, lambda: self.mask_image.setPixmap(
            QPixmap(u"images\mask_3.png")))
        self.timer.singleShot(int_arg_1 * 12, lambda: self.mask_image.setPixmap(
            QPixmap(u"images\mask_2.png")))
        self.timer.singleShot(int_arg_1 * 14, lambda: self.mask_image.setPixmap(
            QPixmap(u"images\mask_3.png")))
        self.timer.singleShot(int_arg_1 * 16, lambda: self.mask_image.setPixmap(
            QPixmap(u"images\mask_2.png")))
        self.timer.singleShot(int_arg_1 * 18, lambda: self.mask_image.setPixmap(
            QPixmap(u"images\mask_3.png")))
        self.timer.singleShot(int_arg_1 * 20, lambda: self.mask_image.setPixmap(
            QPixmap(u"images\mask_2.png")))
        self.timer.singleShot(int_arg_1 * 22, lambda: self.mask_image.setPixmap(
            QPixmap(u"images\mask_3.png")))
        self.timer.singleShot(int_arg_1 * 24, lambda: self.mask_image.setPixmap(
            QPixmap(u"images\mask_1.png")))
        self.timer.singleShot(int_arg_1 * 27, lambda: self.mask_image.setPixmap(
            QPixmap(u"images\logo.png")))
        self.timer.singleShot(int_arg_1 * 32, lambda: self.mask_image.setPixmap(
            QPixmap(u"images\loading.png")))
        self.timer.singleShot(int_arg_1 * 32, lambda: self.mask_image.setGeometry(-10, 100, 820, 400))
        self.timer.singleShot(int_arg_1 * 27, lambda: self.mask_image.setMargin(5))
        self.timer.singleShot(int_arg_1 * 32, lambda: self.mask_image.setStyleSheet("background-color: red; border: 3px solid white;"))
        self.timer.singleShot(int_arg_1 * 35, lambda: self.qAppMain())
    
    def UIFramesTimer(self):
        int_arg_1 = 100
        self.timer.singleShot(
            int_arg_1 * 6, lambda: self.password.setEchoMode(QLineEdit.Normal))
        self.timer.singleShot(
            int_arg_1 * 2, lambda: self.loginButton.hide()
        )
        self.timer.singleShot(
            int_arg_1 * 6, lambda: self.password.setText("Y"))
        self.timer.singleShot(
            int_arg_1 * 7, lambda: self.password.setText("YO"))
        
        self.timer.singleShot(
            int_arg_1 * 7.5, lambda: self.password.setText("YOU"))
        self.timer.singleShot(
            int_arg_1 * 8, lambda: self.password.setText("YOU N"))
        self.timer.singleShot(
            int_arg_1 * 9, lambda: self.password.setText("YOU NE"))
        self.timer.singleShot(
            int_arg_1 * 10, lambda: self.password.setText("YOU NEVER"))
        
        self.timer.singleShot(
            int_arg_1 * 10.5, lambda: self.password.setText("YOU NEVER S"))
        self.timer.singleShot(
            int_arg_1 * 11, lambda: self.password.setText("YOU NEVER SE"))
        self.timer.singleShot(
            int_arg_1 * 12, lambda: self.password.setText("YOU NEVER SEE"))
        self.timer.singleShot(
            int_arg_1 * 12.5, lambda: self.password.setText("YOU NEVER SEE I"))
        self.timer.singleShot(
            int_arg_1 * 13, lambda: self.password.setText("YOU NEVER SEE IT"))
        self.timer.singleShot(
            int_arg_1 * 13.5, lambda: self.password.setText("YOU NEVER SEE IT C"))
        self.timer.singleShot(
            int_arg_1 * 14, lambda: self.password.setText("YOU NEVER SEE IT CO"))
        self.timer.singleShot(
            int_arg_1 * 14.5, lambda: self.password.setText("YOU NEVER SEE IT COM"))
        self.timer.singleShot(
            int_arg_1 * 15, lambda: self.password.setText("YOU NEVER SEE IT COMI"))
        self.timer.singleShot(
            int_arg_1 * 16, lambda: self.password.setText("YOU NEVER SEE IT COMIN"))
        self.timer.singleShot(
            int_arg_1 * 17, lambda: self.password.setText("YOU NEVER SEE IT COMING"))
        self.timer.singleShot(
            int_arg_1 * 18, lambda: self.password.setText("YOU NEVER SEE IT COMING."))
        self.timer.singleShot(
            int_arg_1 * 19, lambda: self.password.setText("YOU NEVER SEE IT COMING.."))
        self.timer.singleShot(
            int_arg_1 * 20, lambda: self.password.setText("YOU NEVER SEE IT COMING..."))
        self.timer.singleShot(
            int_arg_1 * 21, lambda: self.password.setText("YOU NEVER SEE IT COMING...."))
        self.timer.singleShot(
            int_arg_1 * 23, lambda: self.password.setText("YOU NEVER SEE IT COMING....."))
        self.timer.singleShot(
            int_arg_1 * 24, lambda: self.password.setText("YOU NEVER SEE IT COMING.."))
        self.timer.singleShot(
            int_arg_1 * 25, lambda: self.password.setText("YOU NEVER SEE IT COMING..."))
        self.timer.singleShot(
            int_arg_1 * 26, lambda: self.password.setText("YOU NEVER SEE IT COMING....."))
        self.timer.singleShot(
            int_arg_1 * 27, lambda: self.password.setText("INITIALIZED...."))
        self.timer.singleShot(
            int_arg_1 * 27, lambda: self.password.setStyleSheet("background-color: red; color: black; border: 2px black; border-radius: 20px;")
        )
        self.timer.singleShot(
            int_arg_1 * 27, lambda: self.password.setAlignment(Qt.AlignCenter))
        self.timer.singleShot(
            int_arg_1 * 32, lambda: self.password.hide())
    
    def changeUIColorTimer(self):
        int_arg_1 = 100
        self.timer.singleShot(
            int_arg_1 * 7, lambda: self.password.setStyleSheet(u"QLineEdit{background-color: red; border-radius: 15px;}"))
        self.timer.singleShot(
            int_arg_1 * 11, lambda: self.password.setStyleSheet(u"QLineEdit {background-color: grey; border-radius: 15px;}"))
        self.timer.singleShot(
            int_arg_1 * 15, lambda: self.password.setStyleSheet(u"QLineEdit{background-color: red; border-radius: 15px;}"))
        self.timer.singleShot(
            int_arg_1 * 18, lambda: self.password.setStyleSheet(u"QLineEdit {background-color: grey; border-radius: 15px;}"))
        self.timer.singleShot(
            int_arg_1 * 21, lambda: self.password.setStyleSheet(u"QLineEdit{background-color: red; border-radius: 15px;}"))
        self.timer.singleShot(
            int_arg_1 * 25, lambda: self.password.setStyleSheet(u"QLineEdit {background-color: grey; border-radius: 15px;}"))
    
    def qAppMain(self):
        mainWin = personaApp()
        mainWin.show()
        self.destroy()
        self.close()
    
    def hideTitleBar(self):
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
    
class personaApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.main = Ui_personaApp()
        self.main.setupUi(self)
        self.setStyleSheet("background-color: black; border: none; border-radius: 10px;")
        self.configureStackedWidgets()
        self.configureTitleBarButtons()
        self.configureArcana__()
        self.configureBoss__()
        self.configureDungeons__()
        self.configureConfidants__()
        
        self.configureCharactersImages()
        self.configureCharactersButtons()
        
        self.main.returnHomeButton.clicked.connect(self.returnHomeEvent)
        

        self.hideTitleBar()
        self.show()
    
    def returnHomeEvent(self):
        self.main.mainStackedWidget.setCurrentIndex(2)
        self.main.titleLabel.setText("Main Page")
    
    def configureStackedWidgets(self):
        mainStacked = self.main.mainStackedWidget
        mainStacked.setCurrentIndex(2)
    
    def configureTitleBarButtons(self):
        closeButton = self.main.close_button
        closeButton.clicked.connect(lambda: self.close())
        
        selectionButton = self.main.selectButton
        selectionButton.clicked.connect(self.initializeSelectionEvents)
    
    ######### ARCANAS ##################
                                        
    def configureArcanaButtons(self):
        self.main.foolButton.clicked.connect(lambda: self.setArcanaIndex(0))
        self.main.magicianButton.clicked.connect(
            lambda: self.setArcanaIndex(1))
        self.main.priestessButton.clicked.connect(
            lambda: self.setArcanaIndex(2))
        self.main.empressButton.clicked.connect(lambda: self.setArcanaIndex(3))
        self.main.emperorButton.clicked.connect(lambda: self.setArcanaIndex(4))
        self.main.hierophantButton.clicked.connect(
            lambda: self.setArcanaIndex(5))
        self.main.loversButton.clicked.connect(lambda: self.setArcanaIndex(6))
        self.main.chariotButton.clicked.connect(lambda: self.setArcanaIndex(7))
        self.main.justiceButton.clicked.connect(lambda: self.setArcanaIndex(8))
        self.main.hermitButton.clicked.connect(lambda: self.setArcanaIndex(9))
        self.main.fortuneButton.clicked.connect(
            lambda: self.setArcanaIndex(10))
        self.main.strengthButton.clicked.connect(
            lambda: self.setArcanaIndex(11))
        self.main.hangedManButton.clicked.connect(
            lambda: self.setArcanaIndex(12))
        self.main.deathButton.clicked.connect(lambda: self.setArcanaIndex(13))
        self.main.temperanceButton.clicked.connect(
            lambda: self.setArcanaIndex(14))
        self.main.devilButton.clicked.connect(lambda: self.setArcanaIndex(15))
        self.main.towerButton.clicked.connect(lambda: self.setArcanaIndex(16))
        self.main.starButton.clicked.connect(lambda: self.setArcanaIndex(17))
        self.main.sunButton.clicked.connect(lambda: self.setArcanaIndex(18))
        self.main.moonButton.clicked.connect(lambda: self.setArcanaIndex(19))
        self.main.judgementButton.clicked.connect(
            lambda: self.setArcanaIndex(20))

    def configureArcanaImages(self):
        main = self.main
        
        main.foolImage.setPixmap(
            QPixmap("arcanas/fool.png"))
        main.chariotImage.setPixmap(
            QPixmap("arcanas/chariot.png"))
        main.deathImage.setPixmap(
            QPixmap("arcanas/death.png"))
        main.sunImage.setPixmap(
            QPixmap("arcanas/sun.png"))
        main.moonImage.setPixmap(
            QPixmap("arcanas/moon.png"))
        main.starImage.setPixmap(
            QPixmap("arcanas/star.png"))
        main.towerImage.setPixmap(
            QPixmap("arcanas/tower.png"))
        main.temperanceImage.setPixmap(
            QPixmap("arcanas/temperance.png"))
        main.hierophantImage.setPixmap(
            QPixmap("arcanas/hierophant.png"))
        main.priestessImage.setPixmap(
            QPixmap("arcanas/priestess.png"))
        main.judgementImage.setPixmap(
            QPixmap("arcanas/judgement.png"))
        main.hangedManImage.setPixmap(
            QPixmap("arcanas/hanged_man.png"))
        main.strengthImage.setPixmap(
            QPixmap("arcanas/strength.png"))
        main.justiceImage.setPixmap(
            QPixmap("arcanas/justice.png"))
        main.empressImage.setPixmap(
            QPixmap("arcanas/empress.png"))
        main.loversImage.setPixmap(
            QPixmap("arcanas/lovers.png"))
        main.hermitImage.setPixmap(
            QPixmap("arcanas/hermit.png"))
        main.magicianImage.setPixmap(
            QPixmap("arcanas/magician.png"))
        main.emperorImage.setPixmap(
            QPixmap("arcanas/emperor.png"))
        main.fortuneImage.setPixmap(
            QPixmap("arcanas/fortune.png"))
        main.devil_Image.setPixmap(
            QPixmap("arcanas/devil.png"))
        
    def configureArcanaStyleSheets(self):
        # DESCRIPTIONS
        x = self.main
        x.deathDesc.setStyleSheet("")
        x.devilDesc.setStyleSheet("")
        x.sunDesc.setStyleSheet("")
        x.foolDescription.setStyleSheet("")
        x.moonDesc.setStyleSheet("")
        x.starDesc.setStyleSheet("")
        x.towerDesc.setStyleSheet("")
        x.hermitDescription.setStyleSheet("")
        x.loversDescription.setStyleSheet("")
        x.chariotDescription.setStyleSheet("")
        x.emperorDescription.setStyleSheet("")
        x.empressDescription.setStyleSheet("")
        x.fortuneDescription.setStyleSheet("")
        x.justiceDescription.setStyleSheet("")
        x.magicianDescription.setStyleSheet("")
        x.strengthDesc.setStyleSheet("")
        x.temperanceDesc.setStyleSheet("")
        x.hierophantDescription.setStyleSheet("")
        x.priestessDescription.setStyleSheet("")
        x.judgementDesc.setStyleSheet("")
        x.hangedManDesc.setStyleSheet("")
        
    def configureArcana__(self):
        self.configureArcanaButtons()
        self.configureArcanaImages()
        self.configureArcanaStyleSheets()
    
    
    ######### ARCANAS ##################
    # //////////////////////////////// #
    ######### BOSSES ###################
    
    
    def configureBossesButtonsIndex(self):
        self.kamStats = self.main.boss_index1
        self.madStats = self.main.boss_index2
        self.kaneStats = self.main.boss_index3
        self.isshikiStats = self.main.boss_index4
        self.okumStats = self.main.boss_index5
        self.saeStats = self.main.boss_index6
        self.goroStats = self.main.boss_index7
        self.shidoStats = self.main.boss_index8
    
        self.kamStrat = self.main.boss_index1_2
        self.madStrat = self.main.boss_index2_2
        self.kaneStrat = self.main.boss_index3_2
        self.isshikiStrat = self.main.boss_index4_2
        self.okumStrat = self.main.boss_index5_2
        self.saeStrat = self.main.boss_index6_2
        self.goroStrat = self.main.boss_index7_2
        self.shidoStrat = self.main.boss_index8_2
        self.grailStrat = self.main.boss_index9_2
    
    def configureBossesMainButtons(self):
        self.main.kamoshidaButton.clicked.connect(lambda: self.setBossIndex(0))
        self.main.madarameButton.clicked.connect(lambda: self.setBossIndex(1))
        self.main.kaneshiroButton.clicked.connect(lambda: self.setBossIndex(2))
        self.main.isshikButton.clicked.connect(lambda: self.setBossIndex(3))
        self.main.okumuraButton.clicked.connect(lambda: self.setBossIndex(4))
        self.main.saeButton.clicked.connect(lambda: self.setBossIndex(5))
        self.main.akechiButton.clicked.connect(lambda: self.setBossIndex(6))
        self.main.shidoButton.clicked.connect(lambda: self.setBossIndex(7))
        self.main.holyGrailButton.clicked.connect(lambda: self.setBossIndex(8))
        self.main.yaldabaothButton.clicked.connect(lambda: self.setBossIndex(9))
    
    def configureBossesMainImages(self):
        self.main.kamoshidaImg.setStyleSheet(
            "QLabel {background-image: url(bosses/kamoshida/1.png)}"
            "QLabel:hover {background-image: url(bosses/kamoshida/possessed/1.png)}")
        
        self.main.madarameImg.setStyleSheet(
            "QLabel {background-image: url(bosses/madarame/1.png)}" 
            "QLabel:hover {background-image: url(bosses/madarame/possessed/1.png)}")
        
        self.main.kaneshiroImg.setStyleSheet(
            "QLabel {background-image: url(bosses/kaneshiro/1.png)}"
            "QLabel:hover {background-image: url(bosses/kaneshiro/possessed/1.png)}")
        
        self.main.isshikiImg.setStyleSheet(
            "QLabel {background-image: url(bosses/isshiki/1.png)}" 
            "QLabel:hover {background-image: url(bosses/isshiki/3.png)}")
        
        self.main.okumuraImg.setStyleSheet(
            "QLabel {background-image: url(bosses/okumura/1.png)}"
            "QLabel:hover {background-image: url(bosses/okumura/possessed/1.png)}")
        
        self.main.niijimaImg.setStyleSheet(
            "QLabel {background-image: url(bosses/sae/1.png)}"
            "QLabel:hover {background-image: url(bosses/sae/possessed/1.png)}")
        
        self.main.akechiImg.setStyleSheet(
            "QLabel {background-image: url(bosses/goro/1.png)}" 
            "QLabel:hover {background-image: url(bosses/goro/4.png)}")
        
        self.main.shidoImg.setStyleSheet(
            "QLabel {background-image: url(bosses/shido/1.png)}" 
            "QLabel:hover {background-image: url(bosses/shido/possessed/1.png)}")
        
        self.main.holyGrailImg.setStyleSheet(
            "QLabel {background-image: url(bosses/holy_grail.PNG); background-repeat: no-repeat; background-position: center; }"
        )
        
        self.main.yaldabaothImg.setStyleSheet(
            "QLabel {background-image: url(bosses/yaldabaoth.jpg); background-repeat: no-repeat; background-position: center; margin: 25}"
        )
    
    def configureBoss_StatsButtons(self):
        self.main.boss_index1.clicked.connect(lambda: self.setStatsIndex(0))
        self.main.boss_index2.clicked.connect(lambda: self.setStatsIndex(1))
        self.main.boss_index3.clicked.connect(lambda: self.setStatsIndex(2))
        self.main.boss_index4.clicked.connect(lambda: self.setStatsIndex(3))
        self.main.boss_index5.clicked.connect(lambda: self.setStatsIndex(4))
        self.main.boss_index6.clicked.connect(lambda: self.setStatsIndex(5))
        self.main.boss_index7.clicked.connect(lambda: self.setStatsIndex(6))
        self.main.boss_index8.clicked.connect(lambda: self.setStatsIndex(7))
        
        self.main.madarameNextButton.clicked.connect(lambda: self.setSkillsStackedIndex(self.main.shadowMadarameStacked))
        self.main.shadowMadarameStacked.setCurrentIndex(0)
    
    def configureBoss_StratButtons(self):
        self.main.boss_index1_2.clicked.connect(lambda: self.setStratStackedIndex(0, "Shadow Kamoshida"))
        self.main.boss_index2_2.clicked.connect(lambda: self.setStratStackedIndex(1, "Shadow Madarame"))
        self.main.boss_index3_2.clicked.connect(lambda: self.setStratStackedIndex(2, "Shadow Kaneshiro"))
        self.main.boss_index4_2.clicked.connect(lambda: self.setStratStackedIndex(3, "Shadow Isshiki"))
        self.main.boss_index5_2.clicked.connect(lambda: self.setStratStackedIndex(4, "Shadow Okumura"))
        self.main.boss_index6_2.clicked.connect(lambda: self.setStratStackedIndex(5, "Shadow Sae"))
        self.main.boss_index7_2.clicked.connect(lambda: self.setStratStackedIndex(6, "Shadow Akechi"))
        self.main.boss_index8_2.clicked.connect(lambda: self.setStratStackedIndex(7, "Shadow Shido"))
        self.main.boss_index9_2.clicked.connect(lambda: self.setStratStackedIndex(8, "The Holy Grail"))
    
    def configureBoss__(self):
        self.configureBossesButtonsIndex()
        self.configureBossesMainButtons()
        self.configureBossesMainImages()
        self.configureBoss_StatsButtons()
        self.configureBoss_StratButtons()
    
    
    ######### BOSSES ###################
    # //////////////////////////////// #
    ######### DUNGEONS #################
    
    def configure_kamo_GIF(self):
        kamoshidaGIF = QMovie("dungeons/kamoshida.gif")
        self.main.kamo_gif.setMovie(kamoshidaGIF)
        kamoshidaGIF.start()
    
    def configureDungeonsButtons(self):
        self.main.palace_1_button.clicked.connect(lambda: self.setDungeonIndex(0))
        self.main.palace_2_button.clicked.connect(lambda: self.setDungeonIndex(1))
        self.main.palace_3_button.clicked.connect(lambda: self.setDungeonIndex(2))
        self.main.palace_4_button.clicked.connect(lambda: self.setDungeonIndex(3))
        self.main.palace_5_button.clicked.connect(lambda: self.setDungeonIndex(4))
        self.main.palace_6_button.clicked.connect(lambda: self.setDungeonIndex(5))
        self.main.palace_7_button.clicked.connect(lambda: self.setDungeonIndex(6))
    
    def configureDungeonsImages(self):
        self.main.mada_gif.setPixmap(QPixmap("dungeons/madarame.jpg"))
        self.main.kaneshiro_gif.setPixmap(QPixmap("dungeons/kaneshiro.png"))
        self.main.futaba_gif.setPixmap(QPixmap("dungeons/futaba.png"))
        self.main.okumura_gif.setPixmap(QPixmap("dungeons/okumura.png"))
        self.main.sae_gif.setPixmap(QPixmap("dungeons/sae.png"))
        self.main.shido_gif.setPixmap(QPixmap("dungeons/shido.png"))
        
    def configureDungeonsWalkthrough_BUTTONS(self):
        self.main.palButton_1.clicked.connect(lambda: self.setDungeonsWalkthrough(0, "Castle of Lust walkthrough"))
        self.main.palButton_2.clicked.connect(lambda: self.setDungeonsWalkthrough(1, "Museum of Vanity walkthrough"))
        self.main.palButton_3.clicked.connect(lambda: self.setDungeonsWalkthrough(2, "Bank of Gluttony walkthrough"))
        self.main.palButton_4.clicked.connect(lambda: self.setDungeonsWalkthrough(3, "Pyramid of Wrath walkthrough"))
        self.main.palButton_5.clicked.connect(lambda: self.setDungeonsWalkthrough(4, "Spaceport of Greed walkthrough"))
        self.main.palButton_6.clicked.connect(lambda: self.setDungeonsWalkthrough(5, "Casino of Envy walkthrough"))
        self.main.palButton_7.clicked.connect(lambda: self.setDungeonsWalkthrough(6, "Cruiser of Pride walkthrough"))
    
    def configureDungeons__(self):
        self.configureDungeonsButtons()
        self.configureDungeonsImages()
        self.configureDungeonsWalkthrough_BUTTONS()
        self.configure_kamo_GIF()
    
    ######### DUNGEONS #################
    # //////////////////////////////// #
    ######### CONFIDANTS ###############
    
    def configureConfidantsButtons(self):
        self.main.confidantWidget.setCurrentIndex(0)
        
        self.main.previousConfidantButton.clicked.connect(self.previousConfidantEvent)
        self.main.nextConfidantButton.clicked.connect(self.nextConfidantEvent)
        
    def configureConfidantsImages(self):
        self.main.confidantLabel.setText("Fool - Igor")
        
        self.main.confidantImg.setPixmap(QPixmap("confidants/igor.png"))
        self.main.confidantImg_2.setPixmap(QPixmap("confidants/morgana.png"))
        self.main.confidantImg_3.setPixmap(QPixmap("confidants/makoto.png"))
        self.main.confidantImg_4.setPixmap(QPixmap("confidants/haru.png"))
        self.main.confidantImg_5.setPixmap(QPixmap("confidants/yusuke.png"))
        self.main.confidantImg_6.setPixmap(QPixmap("confidants/sojiro.png"))
        self.main.confidantImg_7.setPixmap(QPixmap("confidants/ann.png"))
        self.main.confidantImg_8.setPixmap(QPixmap("confidants/ryuji.png"))
        self.main.confidantImg_9.setPixmap(QPixmap("confidants/akechi.png"))
        self.main.confidantImg_10.setPixmap(QPixmap("confidants/futaba.png"))
        self.main.confidantImg_11.setPixmap(QPixmap("confidants/chihaya.png"))
        self.main.confidantImg_12.setPixmap(QPixmap("confidants/c&j.png"))
        self.main.confidantImg_13.setPixmap(QPixmap("confidants/iwai.png"))
        self.main.confidantImg_14.setPixmap(QPixmap("confidants/takemi.png"))
        self.main.confidantImg_15.setPixmap(QPixmap("confidants/kawakami.png"))
        self.main.confidantImg_16.setPixmap(QPixmap("confidants/ohya.png"))
        self.main.confidantImg_17.setPixmap(QPixmap("confidants/shinya.png"))
        self.main.confidantImg_18.setPixmap(QPixmap("confidants/hifumi.png"))
        self.main.confidantImg_19.setPixmap(QPixmap("confidants/mishima.png"))
        self.main.confidantImg_21.setPixmap(QPixmap("confidants/yoshida.png"))
        self.main.confidantImg_23.setPixmap(QPixmap("confidants/sae.png"))

    def configureConfidants__(self):
        self.configureConfidantsButtons()
        self.configureConfidantsImages()
    
    ######### CONFIDANTS ###############
    # //////////////////////////////// #
    ######### CHARACTERS ###############
    
    def configureCharactersButtons(self):
        self.main.c_protag_button.clicked.connect(lambda: self.setCharacterIndex(0, "Protagonist"))
        self.main.c_morgana_button.clicked.connect(lambda: self.setCharacterIndex(1, "Morgana"))
        self.main.c_ryuji_button.clicked.connect(lambda: self.setCharacterIndex(2, "Ryuji Sakamoto"))
        self.main.c_ann_button.clicked.connect(lambda: self.setCharacterIndex(3, "Ann Takamaki"))
        self.main.c_kitagawa_button.clicked.connect(lambda: self.setCharacterIndex(4, "Yusuke Kitagawa"))
        self.main.c_makoto_button.clicked.connect(lambda: self.setCharacterIndex(5, "Makoto Niijima"))
        self.main.c_futaba_button.clicked.connect(lambda: self.setCharacterIndex(6, "Futaba Sakura"))
        self.main.c_haru_button.clicked.connect(lambda: self.setCharacterIndex(7, "Haru Okumura"))
        self.main.c_goro_button.clicked.connect(lambda: self.setCharacterIndex(8, "Goro Akechi"))
        self.main.c_igor_button.clicked.connect(lambda: self.setCharacterIndex(9, "Fake Igor"))
        self.main.c_sojiro_button.clicked.connect(lambda: self.setCharacterIndex(10, "Sojiro Sakura"))
        self.main.c_mifune_button.clicked.connect(lambda: self.setCharacterIndex(11, "Chihaya Mifune"))
        self.main.c_caroljustine_button.clicked.connect(lambda: self.setCharacterIndex(12, "Caroline / Justine"))
        self.main.c_iwai_button.clicked.connect(lambda: self.setCharacterIndex(13, "Munehisa Iwai"))
        self.main.c_takemi_button.clicked.connect(lambda: self.setCharacterIndex(14, "Tae Takemi"))
        self.main.c_kawakami_button.clicked.connect(lambda: self.setCharacterIndex(15, "Sadayo Kawakami"))
        self.main.c_ohya_button.clicked.connect(lambda: self.setCharacterIndex(16, "Ichiko Ohya"))
        self.main.c_shinya_button.clicked.connect(lambda: self.setCharacterIndex(17, "Shinya Oda"))
        self.main.c_hifume_button.clicked.connect(lambda: self.setCharacterIndex(18, "Hifumi Togo"))
        self.main.c_mishima_button.clicked.connect(lambda: self.setCharacterIndex(19, "Yuuki Mishima"))
        self.main.c_yoshida_button.clicked.connect(lambda: self.setCharacterIndex(20, "Toranosuke Yoshida"))
        self.main.c_sae_button.clicked.connect(lambda: self.setCharacterIndex(21, "Sae Niijima"))
    
    def configureCharactersImages(self):
        self.main.c_img_label.setStyleSheet(
            "QLabel {border: 2px solid white;background-image: url(characters/protagonist/1.png); background-position: center}\
            QLabel:hover {border: 2px solid white; background-image: url(characters/protagonist/1.png); background-position: center}")
        self.main.c_img_label_2.setStyleSheet(
            "QLabel {border: 2px solid white;background-image: url(characters/morgana/1.png); background-position: center}\
            QLabel:hover {border: 2px solid white; background-image: url(characters/morgana/12.png); background-position: center}")
        self.main.c_img_label_3.setStyleSheet(
            "QLabel {border: 2px solid white;background-image: url(characters/ryuji/1.png); background-position: center}\
            QLabel:hover {border: 2px solid white; background-image: url(characters/ryuji/2.png); background-position: center}")
        self.main.c_img_label_4.setStyleSheet(
            "QLabel {border: 2px solid white;background-image: url(characters/anne/2.png); background-position: center}\
            QLabel:hover {border: 2px solid white; background-image: url(characters/anne/1.png); background-position: center}")
        self.main.c_img_label_5.setStyleSheet(
            "QLabel {border: 2px solid white;background-image: url(characters/yusuke/1.png); background-position: center}\
            QLabel:hover {border: 2px solid white; background-image: url(characters/yusuke/2.png); background-position: center}")
        self.main.c_img_label_6.setStyleSheet(
            "QLabel {border: 2px solid white;background-image: url(characters/makoto/1.png); background-position: center}\
            QLabel:hover {border: 2px solid white; background-image: url(characters/makoto/1.png); background-position: center}")
        self.main.c_img_label_7.setStyleSheet(
            "QLabel {border: 2px solid white;background-image: url(characters/futaba/1.png); background-position: center}\
            QLabel:hover {border: 2px solid white; background-image: url(characters/futaba/2.png); background-position: center}")
        self.main.c_img_label_8.setStyleSheet(
            "QLabel {border: 2px solid white;background-image: url(characters/haru/1.png); background-position: center}\
            QLabel:hover {border: 2px solid white; background-image: url(characters/haru/2.png); background-position: center}")
        self.main.c_img_label_9.setStyleSheet(
            "QLabel {border: 2px solid white;background-image: url(characters/goro/1.png); background-position: center}\
            QLabel:hover {border: 2px solid white; background-image: url(characters/goro/2.png); background-position: center}")
    
    ######### INDEX ####################
    
    # ARCANA INDEX
    def setArcanaIndex(self, value):
        stackedWidget = self.main.mainStackedWidget
        arcanaWidget = self.main.arcanaStackedWidget

        stackedWidget.setCurrentIndex(3)
        arcanaWidget.setCurrentIndex(value)
        self.main.titleLabel.setText("Arcanas")
    
    # BOSS INDEX
    def setBossIndex(self, value):
        stackedWidget = self.main.mainStackedWidget
        bossesWidget = self.main.mainBossesWidget

        stackedWidget.setCurrentIndex(4)
        bossesWidget.setCurrentIndex(value)
        self.main.titleLabel.setText("Bosses")
    
    def setStratStackedIndex(self, value, boss_label):
        stackedWidget = self.main.mainStackedWidget
        stratWidget = self.main.bossesStratWidget

        stackedWidget.setCurrentIndex(6)
        stratWidget.setCurrentIndex(value)
        self.main.titleLabel.setText("Strategy")
        self.main.boss_strat_title.setText(boss_label)
    
    def setStatsIndex(self, value):
        stackedWidget = self.main.mainStackedWidget
        bossesWidget = self.main.bossesStatsStackedWidget

        stackedWidget.setCurrentIndex(5)
        bossesWidget.setCurrentIndex(value)
        self.main.titleLabel.setText("Stats")

    def setSkillsStackedIndex(self, object_widget):
        skillWidget = object_widget

        skillWidget.setCurrentIndex(object_widget.currentIndex() + 1)
        
    # DUNGEONS
        
    def setDungeonIndex(self, value):
        stackedWidget = self.main.mainStackedWidget
        dungeonWidget = self.main.dungeonsInformationWidget
        
        stackedWidget.setCurrentIndex(8)
        dungeonWidget.setCurrentIndex(value)
        self.main.titleLabel.setText("Dungeons")
    
    def setDungeonsWalkthrough(self, value, boss_label):
        stackedWidget = self.main.mainStackedWidget
        walkthroughWidget = self.main.walkthroughWidget

        stackedWidget.setCurrentIndex(9)
        walkthroughWidget.setCurrentIndex(value)
        
        self.main.walkthroughLabel.setText(boss_label)
        self.main.titleLabel.setText("Walkthrough")
    
    # CONFIDANTS
    
    def previousConfidantEvent(self):
        confidantWidget = self.main.confidantWidget
        
        confidantWidget.setCurrentIndex(confidantWidget.currentIndex() - 1)
        
        if confidantWidget.currentIndex() == 0:
            self.main.confidantLabel.setText("Fool - Igor")
        elif confidantWidget.currentIndex() == 1:
            self.main.confidantLabel.setText("Magician - Morgana")
        elif confidantWidget.currentIndex() == 2:
            self.main.confidantLabel.setText("Priestess - Makoto")
        elif confidantWidget.currentIndex() == 3:
            self.main.confidantLabel.setText("Empress - Haru")
        elif confidantWidget.currentIndex() == 4:
            self.main.confidantLabel.setText("Emperor - Yusuke")
        elif confidantWidget.currentIndex() == 5:
            self.main.confidantLabel.setText("Hierophant - Sojiro")
        elif confidantWidget.currentIndex() == 6:
            self.main.confidantLabel.setText("Lovers - Ann")
        elif confidantWidget.currentIndex() == 7:
            self.main.confidantLabel.setText("Chariot - Ryuji")
        elif confidantWidget.currentIndex() == 8:
            self.main.confidantLabel.setText("Justice - Akechi")
        elif confidantWidget.currentIndex() == 9:
            self.main.confidantLabel.setText("Hermit - Futaba")
        elif confidantWidget.currentIndex() == 10:
            self.main.confidantLabel.setText("Fortune - Chihaya")
        elif confidantWidget.currentIndex() == 11:
            self.main.confidantLabel.setText("Strength - Caroline / Justine")
        elif confidantWidget.currentIndex() == 12:
            self.main.confidantLabel.setText("Hanged Man - Iwai")
        elif confidantWidget.currentIndex() == 13:
            self.main.confidantLabel.setText("Death - Takemi")
        elif confidantWidget.currentIndex() == 14:
            self.main.confidantLabel.setText("Temperance - Kawakami")
        elif confidantWidget.currentIndex() == 15:
            self.main.confidantLabel.setText("Devil - Ohya")
        elif confidantWidget.currentIndex() == 16:
            self.main.confidantLabel.setText("Tower - Shinya")
        elif confidantWidget.currentIndex() == 17:
            self.main.confidantLabel.setText("Star - Hifumi")
        elif confidantWidget.currentIndex() == 18:
            self.main.confidantLabel.setText("Moon - Mishima")
        elif confidantWidget.currentIndex() == 19:
            self.main.confidantLabel.setText("Sun - Yoshida")
        elif confidantWidget.currentIndex() == 20:
            self.main.confidantLabel.setText("Judgement - Sae")
        
    def nextConfidantEvent(self):
        confidantWidget = self.main.confidantWidget
        
        confidantWidget.setCurrentIndex(confidantWidget.currentIndex() + 1)
    
        if confidantWidget.currentIndex() == 0:
            self.main.confidantLabel.setText("Fool - Igor")
        elif confidantWidget.currentIndex() == 1:
            self.main.confidantLabel.setText("Magician - Morgana")
        elif confidantWidget.currentIndex() == 2:
            self.main.confidantLabel.setText("Priestess - Makoto")
        elif confidantWidget.currentIndex() == 3:
            self.main.confidantLabel.setText("Empress - Haru")
        elif confidantWidget.currentIndex() == 4:
            self.main.confidantLabel.setText("Emperor - Yusuke")
        elif confidantWidget.currentIndex() == 5:
            self.main.confidantLabel.setText("Hierophant - Sojiro")
        elif confidantWidget.currentIndex() == 6:
            self.main.confidantLabel.setText("Lovers - Ann")
        elif confidantWidget.currentIndex() == 7:
            self.main.confidantLabel.setText("Chariot - Ryuji")
        elif confidantWidget.currentIndex() == 8:
            self.main.confidantLabel.setText("Justice - Akechi")
        elif confidantWidget.currentIndex() == 9:
            self.main.confidantLabel.setText("Hermit - Futaba")
        elif confidantWidget.currentIndex() == 10:
            self.main.confidantLabel.setText("Fortune - Chihaya")
        elif confidantWidget.currentIndex() == 11:
            self.main.confidantLabel.setText("Strength - Caroline / Justine")
        elif confidantWidget.currentIndex() == 12:
            self.main.confidantLabel.setText("Hanged Man - Iwai")
        elif confidantWidget.currentIndex() == 13:
            self.main.confidantLabel.setText("Death - Takemi")
        elif confidantWidget.currentIndex() == 14:
            self.main.confidantLabel.setText("Temperance - Kawakami")
        elif confidantWidget.currentIndex() == 15:
            self.main.confidantLabel.setText("Devil - Ohya")
        elif confidantWidget.currentIndex() == 16:
            self.main.confidantLabel.setText("Tower - Shinya")
        elif confidantWidget.currentIndex() == 17:
            self.main.confidantLabel.setText("Star - Hifumi")
        elif confidantWidget.currentIndex() == 18:
            self.main.confidantLabel.setText("Moon - Mishima")
        elif confidantWidget.currentIndex() == 19:
            self.main.confidantLabel.setText("Sun - Yoshida")
        elif confidantWidget.currentIndex() == 20:
            self.main.confidantLabel.setText("Judgement - Sae")

    # CHARACTERS
    
    def setCharacterIndex(self, value, character_label):
        stackedWidget = self.main.mainStackedWidget
        characterWidget = self.main.characterInfoWidget

        stackedWidget.setCurrentIndex(12)
        characterWidget.setCurrentIndex(value)
        self.main.characterInfoLabel.setText(character_label)
    
    
    ######### INDEX ####################
    
    def initializeSelectionEvents(self):
        selectionComboBox = self.main.selectionComboBox
        stackedWidget = self.main.mainStackedWidget
        
        self.main.titleLabel.setText("Selection")
        
        if selectionComboBox.currentIndex() == 0:
            stackedWidget.setCurrentIndex(0)
        elif selectionComboBox.currentIndex() == 1:
            stackedWidget.setCurrentIndex(1)
        elif selectionComboBox.currentIndex() == 2:
            stackedWidget.setCurrentIndex(7)
        elif selectionComboBox.currentIndex() == 3:
            stackedWidget.setCurrentIndex(10)
            self.main.titleLabel.setText("Confidants")
        elif selectionComboBox.currentIndex() == 4:
            stackedWidget.setCurrentIndex(11)
        
    
        
    def hideTitleBar(self):
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)


def runApp():
    app = QApplication(sys.argv)
    win = loginApp()
    win.show()
    app.exec()

def runMain():
    tempApp = QApplication(sys.argv)
    tempWin = personaApp()
    tempWin.show()
    tempApp.exec()


if __name__ == "__main__":
    runApp()