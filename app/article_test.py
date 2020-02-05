import unittest
from models import articlezzz
Article = article.Article

class ArticleTest(unittest.TestCase):
    '''
    Test class to test the behaviours of the Article class
    '''

    def setUp(self):
        '''
        Set up method that will run before every test
        '''

        self.new_article = Article(1234, 'KTN', 'Writer', 'https://klsjhskljf.img', '2020-02-02T16:02:46Z', 'Yeah, this is it')


    def test_instance(self):
                self.assertTrue(isinstance(self.new_article, Article))



if __name__ == '__main__':
    unittest.main()