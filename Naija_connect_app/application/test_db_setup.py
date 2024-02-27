""" This module was created for testing the database setup """

from application import db, create_app
from application.models import User, Post

app = create_app()

with app.app_context():
    db.create_all()
    user1 = User(username='Faatai', email='vick@demo.com', password='password', state='Edo')
    db.session.add(user1)
    user2 = User(username='Vickyy', email='vicky@demo.com', password='password', state='Ibadan')
    db.session.add(user2)
    db.session.commit()

    post1 = Post(title="Blog post 1", content='My first post', user_id=user1.id)
    db.session.add(post1)
    post2 = Post(title="Blog post 2", content='My second post', user_id=user1.id)
    db.session.add(post2)
    db.session.commit()

    print(user1.post)
    print(user2.post)
    print(post1.author)
    print(post2.author)
    print(Post.query.all())
    print(post1.content)