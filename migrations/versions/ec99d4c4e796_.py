"""empty message

Revision ID: ec99d4c4e796
Revises: 8f73d6552213
Create Date: 2017-03-22 17:57:57.297000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ec99d4c4e796'
down_revision = '8f73d6552213'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('front_user',
    sa.Column('id', sa.String(length=100), nullable=False),
    sa.Column('username', sa.String(length=100), nullable=False),
    sa.Column('_password', sa.String(length=100), nullable=False),
    sa.Column('telephone', sa.String(length=11), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('is_live', sa.Boolean(), nullable=True),
    sa.Column('lask_login_time', sa.DateTime(), nullable=True),
    sa.Column('qq', sa.String(length=15), nullable=True),
    sa.Column('relname', sa.String(length=20), nullable=True),
    sa.Column('gender', sa.Integer(), nullable=True),
    sa.Column('signature', sa.String(length=100), nullable=True),
    sa.Column('bbs_points', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('front_user')
    # ### end Alembic commands ###
