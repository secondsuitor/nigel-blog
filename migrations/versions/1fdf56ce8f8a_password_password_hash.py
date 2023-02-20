"""password > password_hash

Revision ID: 1fdf56ce8f8a
Revises: 35591ee881f8
Create Date: 2023-02-19 13:05:09.754556

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1fdf56ce8f8a'
down_revision = '35591ee881f8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password_hash', sa.String(length=128), nullable=True))
        batch_op.drop_column('password_')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password_', sa.VARCHAR(length=128), nullable=True))
        batch_op.drop_column('password_hash')

    # ### end Alembic commands ###