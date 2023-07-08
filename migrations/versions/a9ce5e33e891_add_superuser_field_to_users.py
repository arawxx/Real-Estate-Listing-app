"""add superuser field to users

Revision ID: a9ce5e33e891
Revises: 59ee3c2ebacf
Create Date: 2023-07-06 10:06:59.972391

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = 'a9ce5e33e891'
down_revision = '59ee3c2ebacf'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('is_superuser', sa.Boolean(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'is_superuser')
    # ### end Alembic commands ###
