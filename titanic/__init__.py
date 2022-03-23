from titanic.models import SpaceshipModel
from titanic.templates import SpaceshipTemplate

if __name__ == '__main__':
    while 1:
        menu = input('1.템플릿 2.전처리')
        if menu == '1':
            print(' ####1.템플릿#### ')
            template = SpaceshipTemplate(fname='train.csv')
            template.visualize()
            break
        elif menu == '2':
            print(' ####2.전처리#### ')
            model = SpaceshipModel()
            model.preprocess(train_fname='train.csv', test_fname='test.csv')
            break
        else:
            break