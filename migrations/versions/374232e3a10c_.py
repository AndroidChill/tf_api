"""empty message

Revision ID: 374232e3a10c
Revises: 
Create Date: 2022-01-04 10:57:36.867268

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '374232e3a10c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('car', sa.Column('test', sa.String(length=10), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('car', 'test')
    # ### end Alembic commands ###
