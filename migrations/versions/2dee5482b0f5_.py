"""empty message

Revision ID: 2dee5482b0f5
Revises: c4a9d1172b35
Create Date: 2017-04-08 16:07:27.929000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2dee5482b0f5'
down_revision = 'c4a9d1172b35'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('front_user', sa.Column('avatar', sa.String(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('front_user', 'avatar')
    # ### end Alembic commands ###
