"""empty message

Revision ID: 65896658e6a7
Revises: 54597d3ab5e3
Create Date: 2017-03-18 13:29:00.831000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '65896658e6a7'
down_revision = '54597d3ab5e3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cms_role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('desc', sa.String(length=100), nullable=True),
    sa.Column('power', sa.Integer(), nullable=True),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('cms_user_role',
    sa.Column('cms_role_id', sa.Integer(), nullable=False),
    sa.Column('cms_user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['cms_role_id'], ['cms_role.id'], ),
    sa.ForeignKeyConstraint(['cms_user_id'], ['cms_user.id'], ),
    sa.PrimaryKeyConstraint('cms_role_id', 'cms_user_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cms_user_role')
    op.drop_table('cms_role')
    # ### end Alembic commands ###
