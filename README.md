# base-image-reconciler
Application to reconcile Container Base Image

https://www.digitalocean.com/community/tutorials/how-to-structure-a-large-flask-application-with-flask-blueprints-and-flask-sqlalchemy

https://medium.com/@metacosmos/protect-flask-apis-with-openid-connect-using-flask-pyoidc-3576d9408e46

```buildoutcfg
export FLASK_APP=app
export FLASK_ENV=development
flask run
```
```
.
└── flask_app
    ├── app
    │   ├── extensions.py
    │   ├── __init__.py
    │   ├── main
    │   │   ├── __init__.py
    │   │   └── routes.py
    │   ├── models
    │   │   ├── post.py
    │   │   └── question.py
    │   ├── posts
    │   │   ├── __init__.py
    │   │   └── routes.py
    │   ├── questions
    │   │   ├── __init__.py
    │   │   └── routes.py
    │   └── templates
    │       ├── base.html
    │       ├── index.html
    │       ├── posts
    │       │   ├── categories.html
    │       │   └── index.html
    │       └── questions
    │           └── index.html
    ├── app.db
    └── config.py
```