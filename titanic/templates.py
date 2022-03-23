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
        self.drawShoppingMall(this)
        # self.draw_embarked(this)

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
        labels = [-1, 0, 1, 2, 3, 4, 5]
        bins = [-1, 0, 1, 10, 100, 500, 1000, np.Inf]
        this['Spa'] = pd.cut(this['Spas'], bins, labels=labels, right=False)
        print(this['Spa'])
        print(this['Spa'].value_counts())
        '''this['Spa'] = pd.qcut(this['Spas'], 3)
        print(this['Spa'])
        print(this['Spa'].value_counts())'''
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
        labels = [-1, 0, 1, 2, 3, 4, 5, 6]
        bins = [-1, 0, 1, 10, 50, 100, 500, 900, np.Inf]
        this['ShoppingMall'] = pd.cut(this['ShoppingMalls'], bins, labels=labels, right=False)
        print(this['ShoppingMall'])
        print(this['ShoppingMall'].value_counts())
        # this['ShoppingMall'] = pd.qcut(this['ShoppingMalls'], 2)
        # print(this['ShoppingMall'])
        # print(this['ShoppingMall'].value_counts())
        a = pd.crosstab(this['ShoppingMall'], this['Transported'], margins=True)
        ic(a)
        '''
           ic| a: Transported   False  True   All
           ShoppingMall                   
           -1                    94   114   208
           0                    2242  3345  5587
           1-9                  374   127   501
           10-49                382    91   473
           50-99                181    54   235
           100-499              528   163   691
           500-899              311   239   550
           900~                 203   245   448
           All                  4315  4378  8693
        '''