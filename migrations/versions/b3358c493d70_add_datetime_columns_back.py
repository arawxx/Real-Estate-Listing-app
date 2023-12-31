"""add datetime columns back

Revision ID: b3358c493d70
Revises: 03dd06c09573
Create Date: 2023-07-08 11:58:41.072032

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = 'b3358c493d70'
down_revision = '03dd06c09573'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('listings', sa.Column('created_at', sa.DateTime(timezone=True), nullable=False))
    op.add_column('listings', sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False))
    op.add_column('users', sa.Column('date_of_birth', sa.DateTime(timezone=True), nullable=True))
    op.add_column('users', sa.Column('created_at', sa.DateTime(timezone=True), nullable=False))
    op.add_column('users', sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'updated_at')
    op.drop_column('users', 'created_at')
    op.drop_column('users', 'date_of_birth')
    op.drop_column('listings', 'updated_at')
    op.drop_column('listings', 'created_at')
    # ### end Alembic commands ###
