from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
user = Table('user', pre_meta,
    Column('uid', Integer, primary_key=True, nullable=False),
    Column('firstname', String),
    Column('nickname', String),
    Column('lastname', String),
    Column('email', String),
    Column('pwdhash', String),
    Column('something', String),
    Column('role', SmallInteger),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['user'].columns['nickname'].drop()
    pre_meta.tables['user'].columns['something'].drop()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['user'].columns['nickname'].create()
    pre_meta.tables['user'].columns['something'].create()
