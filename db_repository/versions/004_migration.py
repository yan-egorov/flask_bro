from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
user = Table('user', post_meta,
    Column('uid', Integer, primary_key=True, nullable=False),
    Column('firstname', String(length=100)),
    Column('nickname', String(length=64)),
    Column('lastname', String(length=100)),
    Column('email', String(length=120)),
    Column('pwdhash', String(length=54)),
    Column('something', String(length=2000)),
    Column('role', SmallInteger, default=ColumnDefault(0)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['user'].columns['nickname'].create()
    post_meta.tables['user'].columns['something'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['user'].columns['nickname'].drop()
    post_meta.tables['user'].columns['something'].drop()
