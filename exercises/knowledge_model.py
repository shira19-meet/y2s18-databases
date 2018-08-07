from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Knowledge(Base):
    __tablename__ = 'knowledge'
    id = Column(Integer, primary_key=True)
    tv_show = Column(String)
    season = Column(Integer)
    rate = Column(Integer)

    def __repr__(self):
        return "If you want to watch a tv show you should look up {} " \
                "that has {} seasons We gave this show a rating of {}" \
                " out of 10".format(self.tv_show,self,season,self.rate)

    #def __init__(self,id, netflix ,tv_show, episode)
    # Create a table with 4 columns
    # The first column will be the primary key
    # The second column should be a string representing
    # the name of the Wiki article that you're referencing
    # The third column will be a string representing the 
    # topic of the article. The last column will be
    # an integer, representing your rating of the article.
k=Knowledge(tv_show="a", season=1 , rate=1)
print(k)