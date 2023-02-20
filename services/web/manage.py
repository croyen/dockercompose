import click
from flask.cli import FlaskGroup

from project import app, db, User


cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command("seed_db")
def seed_db():
    db.session.add(User(email="michael@mherman.org"))
    db.session.commit()


@cli.command("adduser_db")
@click.argument('email')
def add_db(email):
    db.session.add(User(email=email))
    db.session.commit()


if __name__ == "__main__":
    cli()
