import numpy as np
import pandas as pd

from context.domains import Dataset
from context.models import Model
from icecream import ic
import matplotlib.pyplot as plt
import seaborn as sns


class SpaceshipTemplate:
    model = Model()
    dataset = Dataset()

    def __init__(self, fname):
        self.entity = self.model.new_model(fname)
        this = self.entity
        # ic(f'트레인의 타입: {type(this)}')
        # ic(f'트레인의 컬럼: {this.columns}')
        # ic(f'트레인의 상위5행: {this.head()}')
        # ic(f'트레인의 하위5행: {this.tail()}')

    def visualize(self):
        this = self.entity
        # self.drawVRDeck(this)
        # self.drawSpa(this)
        # self.drawShoppingMall(this)
        # self.drawFoodCourt(this)
        # self.drawRoomService(this)
        # self.drawVIP(this)
        # self.drawAge(this)
        # self.drawDestination(this)
        # self.drawCabin(this)
        # self.drawCryoSleep(this)
        # self.drawHomePlanet(this)

    @staticmethod
    def drawVRDeck(this) -> None:
        this['VRDeck'] = this['VRDeck'].fillna(-0.5)
        labels = [-1, 0, 1, 2, 3, 4]
        bins = [-1, 0, 1, 10, 100, 1000, np.Inf]
        this['VRDecks'] = pd.cut(this['VRDeck'], bins, labels=labels, right=False)
        print(this['VRDecks'].value_counts())
        a = pd.crosstab(this['VRDecks'], this['Transported'], margins=True)
        ic(a)
        '''
        VR사용횟수
        ic| a: Transported  False  True  VR이용인원
            VRDecks                       
               NULL            90    98   188
               0             2044  3451  5495
               1-9            296   183   479
               10-99          439   236   675
               100-999        900   335  1235
               1000~          546    75   621
               All           4315  4378  8693
        '''

    @staticmethod
    def drawSpa(this) -> None:
        this['Spas'] = this['Spa'].fillna(-0.5)
        # this['Spa'] = pd.qcut(this['Spas'], 3)
        labels = [-1, 0, 1, 2, 3, 4, 5]
        bins = [-1, 0, 1, 10, 100, 500, 1000, np.Inf]
        this['Spa'] = pd.cut(this['Spas'], bins, labels=labels, right=False)
        print(this['Spa'])
        print(this['Spa'].value_counts())
        a = pd.crosstab(this['Spa'], this['Transported'], margins=True)
        ic(a)
        '''
        ic| a: Transported  False  True  spa이용인원
            Spa                           
            NULL              92    91   183
            0               1921  3403  5324
            1-9              313   213   526
            10-99            446   258   704
            100-499          529   237   766
            500-999          455   106   561
            1000~            559    70   629
            All             4315  4378  8693
        '''

    @staticmethod
    def drawShoppingMall(this) -> None:
        this['ShoppingMalls'] = this['ShoppingMall'].fillna(-0.5)
        # this['ShoppingMall'] = pd.qcut(this['ShoppingMalls'], 2)
        labels = [-1, 0, 1, 2, 3, 4, 5, 6]
        bins = [-1, 0, 1, 10, 50, 100, 500, 900, np.Inf]
        this['ShoppingMall'] = pd.cut(this['ShoppingMalls'], bins, labels=labels, right=False)
        print(this['ShoppingMall'])
        print('*'*100)
        print(this['ShoppingMall'].value_counts())
        a = pd.crosstab(this['ShoppingMall'], this['Transported'], margins=True)
        ic(a)
        '''
           ic| a: Transported   False  True   All
           ShoppingMall                   
           NULL                  94   114   208
           0                   2242  3345  5587
           1-9                  374   127   501
           10-49                382    91   473
           50-99                181    54   235
           100-499              528   163   691
           500-899              311   239   550
           900~                 203   245   448
           All                 4315  4378  8693
        '''

    @staticmethod
    def drawFoodCourt(this) -> None:
        this['FoodCourt'] = this['FoodCourt'].fillna(-0.5)
        # this['FoodCourt'] = pd.qcut(this['FoodCourt'], 3)
        labels = [-1, 0, 1, 2, 3, 4, 5, 6]
        bins = [-1, 0, 1, 10, 100, 300, 700, 1500, np.Inf]
        this['FoodCourt'] = pd.cut(this['FoodCourt'], bins, labels=labels, right=False)
        print(this['FoodCourt'])
        print('*'*100)
        print(this['FoodCourt'].value_counts())
        a = pd.crosstab(this['FoodCourt'], this['Transported'], margins=True)
        ic(a)

        '''
        ic| a: Transported  False  True   All
           FoodCourt                     
               NULL           84    99   183
               0             2232  3224  5456
               1-9           341    95   436
               10-99         452   124   576
               100-299       301   102   403
               300-699       325   142   467
               700-1499      304   208   512
               1500~         276   384   660
               All           4315  4378  8693
        '''

    @staticmethod
    def drawRoomService(this) -> None:
        this['RoomService'] = this['RoomService'].fillna(-0.5)
        # this['RoomService'] = pd.qcut(this['RoomService'], 3)
        labels = [-1, 0, 1, 2, 3, 4, 5, 6]
        bins = [-1, 0, 1, 10, 50, 300, 700, 1200, np.Inf]
        this['RoomService'] = pd.cut(this['RoomService'], bins, labels=labels, right=False)
        print(this['RoomService'])
        print('*' * 100)
        print(this['RoomService'].value_counts())
        a = pd.crosstab(this['RoomService'], this['Transported'], margins=True)
        ic(a)
        '''
        ic| a: Transported  False  True   All
               RoomService                   
               NULL           98    83   181
               0             2045  3532  5577
               1-9           268   154   422
               10-49         257   146   403
               50-299        399   213   612
               300-699       445   120   565
               700-1199      381    76   457
               1200~         422    54   476
               All           4315  4378  8693
        '''

    @staticmethod
    def drawVIP(this) -> None:
        this['VIP'] = this['VIP'].fillna(3)
        print(this['VIP'])
        print('*' * 100)
        print(this['VIP'].value_counts())
        a = pd.crosstab(this['VIP'], this['Transported'], margins=True)
        ic(a)

        '''
        ic| a: Transported  False  True   All
               VIP                           
               False         4093  4198  8291
               True           123    76   199
               NULL            99   104   203
               All           4315  4378  8693
        '''

    @staticmethod
    def drawAge(this) -> None:
        this['Age'] = this['Age'].fillna(-0.5)
        bins = [-1, 0, 6, 12, 18, 26, 39, 60, np.inf]
        labels = ['Unknown', 'Baby', 'Child', 'Teenager', 'Student', 'Young Adult', 'Adult', 'Senior']
        this['Age'] = pd.cut(this['Age'], bins, labels=labels, right=False)
        print(this['Age'])
        print('*' * 100)
        print(this['Age'].value_counts())
        a = pd.crosstab(this['Age'], this['Transported'], margins=True)
        ic(a)
        '''
        ic| a: Transported  False  True   All
               Age                           
               Unknown         89    90   179
               Baby           121   378   499
               Child          109   157   266
               Teenager       342   438   780
               Student       1274  1077  2351
               Young Adult   1370  1251  2621
               Adult          875   868  1743
               Senior         135   119   254
               All           4315  4378  8693
        '''

    @staticmethod
    def drawDestination(this) -> None:
        this['Destination'] = this['Destination'].fillna(3)
        print(this['Destination'])
        print('*' * 100)
        print(this['Destination'].value_counts())
        a = pd.crosstab(this['Destination'], this['Transported'], margins=True)
        ic(a)

        '''
        ic| a: Transported    False  True   All
               Destination                     
               NULL              90    92   182
               55 Cancri e      702  1098  1800
               PSO J318.5-22    395   401   796
               TRAPPIST-1e     3128  2787  5915
               All             4315  4378  8693
        '''

    @staticmethod
    def drawCabin(this) -> None:
        pass

    @staticmethod
    def drawCryoSleep(this) -> None:
        this['CryoSleep'] = this['CryoSleep'].fillna(3)
        print(this['CryoSleep'])
        print('*' * 100)
        print(this['CryoSleep'].value_counts())
        a = pd.crosstab(this['CryoSleep'], this['Transported'], margins=True)
        ic(a)

        '''
        ic| a: Transported  False  True   All
               CryoSleep                     
               False         3650  1789  5439
               True           554  2483  3037
               NULL           111   106   217
               All           4315  4378  8693
        '''

    @staticmethod
    def drawHomePlanet(this) -> None:
        this['HomePlanet'] = this['HomePlanet'].fillna(3)
        print(this['HomePlanet'])
        print('*' * 100)
        print(this['HomePlanet'].value_counts())
        a = pd.crosstab(this['HomePlanet'], this['Transported'], margins=True)
        ic(a)

        '''
        ic| a: Transported  False  True   All
               HomePlanet                    
               NULL            98   103   201
               Earth         2651  1951  4602
               Europa         727  1404  2131
               Mars           839   920  1759
               All           4315  4378  8693

        '''