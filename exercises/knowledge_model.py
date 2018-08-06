from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Knowledge(Base):
    __tablename__ = 'knowledge'
    id = Column(Integer, primary_key=True)
    tv_show = Column(String)
    Stranger_Things = Column(String)
    rate = Column(Integer)
    def __repr__(self):
        return ("If you want to watch a tv show' you should look up Stranger Things on Netflix. We gave this show a rating of 10 out of 10: {}").format
        (self,id,tv_show, Stranger_Things,rate)

    #def __init__(self,id, netflix ,tv_show, episode)
    # Create a table with 4 columns
    # The first column will be the primary key
    # The second column should be a string representing
    # the name of the Wiki article that you're referencing
    # The third column will be a string representing the 
    # topic of the article. The last column will be
    # an integer, representing your rating of the article.

        #self.id = id
        #self.netflix = netflix
        #self.tv_show = tv_show
        #self.episode = episode