"""empty message

Revision ID: c6c6b8c5c746
Revises: 656d83239fb6
Create Date: 2017-04-04 14:44:17.282000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c6c6b8c5c746'
down_revision = '656d83239fb6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comment', sa.Column('origin_comment_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'comment', 'comment', ['origin_comment_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'comment', type_='foreignkey')
    op.drop_column('comment', 'origin_comment_id')
    # ### end Alembic commands ###
