"""empty message

Revision ID: b76a20b8f88d
Revises: d41ce2b746e5
Create Date: 2022-04-28 19:05:11.351767

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b76a20b8f88d'
down_revision = 'd41ce2b746e5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('medicines', schema=None) as batch_op:
        batch_op.drop_constraint('fk_medicines_user_id_users', type_='foreignkey')
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('medicines', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.INTEGER(), nullable=False))
        batch_op.create_foreign_key('fk_medicines_user_id_users', 'users', ['user_id'], ['id'])

    # ### end Alembic commands ###