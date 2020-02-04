class Article:
    '''
    Article class to define article objects
    '''

    def __init__(self,id,author,url,image,date,content):
        self.id = id
        self.author = author
        self.url = url
        self.image = image
        self.date = date
        self.content = content
