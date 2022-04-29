"""empty message

Revision ID: fb9850923279
Revises: ea099073183c
Create Date: 2022-04-27 22:13:04.614167

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fb9850923279'
down_revision = 'ea099073183c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_index('ix_users_email')
        batch_op.create_index(batch_op.f('ix_users_email'), ['email'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_users_email'))
        batch_op.create_index('ix_users_email', ['email'], unique=False)

    # ### end Alembic commands ###