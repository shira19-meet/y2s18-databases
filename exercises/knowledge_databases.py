from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(tv_show, season, rate):
    article_object = Knowledge(
        tv_show=tv_show,
        season=season,
        rate=rate)
    session.add(article_object)
    session.commit()

add_article("Stranger Things", 2, 10)
add_article("Pretty Little Liar",7 , 9)
add_article("The Vampire Diaries", 8, 10)
add_article("13 Reasons Why", 2, 5)
add_article("Riverdale", 2, 9)

def query_all_articles():
    articles = session.query(
       Knowledge).all()
    return articles

# print(query_all_articles())

def query_article_by_topic(tv):
    article = session.query(
        Knowledge).filter_by(
        tv_show=tv ).first()
    return article  

fav_tv_show = query_article_by_topic("Stranger Things")
print(fav_tv_show)

def delete_article_by_topic(tv):
    article = session.query(
        Knowledge).filter_by(
        tv_show=tv ).delete()
    session.commit()

delete_article_by_topic("Stranger Things")
print(query_all_articles())

def delete_all_articles():
    article = session.query(
        Knowledge).delete()
    session.commit()

# delete_all_articles()
# print(query_all_articles())


def edit_article_rating(rating, topic):
    article = session.query(
        knowledge). filter_by(
        tv_show= topic).all()

        for i in article:
            i.rating=rating
            session.commit()

    



