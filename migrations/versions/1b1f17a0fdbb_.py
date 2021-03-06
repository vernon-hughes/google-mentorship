"""empty message

Revision ID: 1b1f17a0fdbb
Revises: a0391fc47e2b
Create Date: 2022-04-28 23:16:32.161504

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1b1f17a0fdbb'
down_revision = 'a0391fc47e2b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('medicines', schema=None) as batch_op:
        batch_op.alter_column('cycle_id',
               existing_type=sa.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('medicines', schema=None) as batch_op:
        batch_op.alter_column('cycle_id',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###
