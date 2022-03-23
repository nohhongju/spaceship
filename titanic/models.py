from icecream import ic

from context.domains import Dataset
from context.models import Model


class SpaceshipModel(object):
    model = Model()
    dataset = Dataset()

    def preprocess(self, train_fname, test_fname):
        this = self.dataset
        that = self.model
        this.train = that.new_dframe(fname=train_fname)
        this.test = that.new_dframe(test_fname)
        this.id = this.test['PassengerId']  # 문제
        this.label = this.train['Transported']  # 정답
        self.df_info(this)
        return this

    @staticmethod
    def df_info(this):
        [ic(f'{i.info()}') for i in [this.train, this.test]]
        ic(this.train.head(3))
        ic(this.test.head(3))

    @staticmethod
    def null_check(this):
        [ic(f'{i.isnull().sum()}') for i in [this.train, this.test]]

    @staticmethod
    def id_info(this):
        ic(f'9. id 의 타입  {type(this.id)}')
        ic(f'10. id 의 상위 3개 {this.id[:3]}')

    @staticmethod
    def drop_feature(this, *feature) -> object:
        pass

    @staticmethod
    def HomePlanet_ordinal(this) -> object:
        return this

    @staticmethod
    def CryoSleep_ordinal(this) -> object:
        return this

    @staticmethod
    def Cabin_ordinal(this) -> object:
        return this

    @staticmethod
    def Destination_ordinal(this) -> object:
        return this

    @staticmethod
    def Age_ordinal(this) -> object:
        return this

    @staticmethod
    def VIP_ordinal(this) -> object:
        return this

    @staticmethod
    def RoomService_ordinal(this) -> object:
        return this

    @staticmethod
    def FoodCourt_ordinal(this) -> object:
        return this

    @staticmethod
    def ShoppingMall_ordinal(this) -> object:
        return this

    @staticmethod
    def Spa_ordinal(this) -> object:
        return this

    @staticmethod
    def VRDeck_ordinal(this) -> object:
        return this

    @staticmethod
    def Name_ordinal(this) -> object:
        return this

    @staticmethod
    def Transported_ordinal(this) -> object:
        return this

