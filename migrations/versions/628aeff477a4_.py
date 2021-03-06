"""empty message

Revision ID: 628aeff477a4
Revises: 086336241d9c
Create Date: 2022-04-28 18:28:58.726781

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '628aeff477a4'
down_revision = '086336241d9c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('_alembic_tmp_medicines')
    with op.batch_alter_table('medicines', schema=None) as batch_op:
        batch_op.add_column(sa.Column('cycle_id', sa.Integer(), nullable=False))
        batch_op.drop_index('ix_medicines_cycle')
        batch_op.drop_constraint('fk_medicines_user_id_users', type_='foreignkey')
        batch_op.create_foreign_key(batch_op.f('fk_medicines_cycle_id_cycles'), 'cycles', ['cycle_id'], ['id'])
        batch_op.drop_column('cycle')
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('medicines', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.INTEGER(), nullable=False))
        batch_op.add_column(sa.Column('cycle', sa.INTEGER(), nullable=True))
        batch_op.drop_constraint(batch_op.f('fk_medicines_cycle_id_cycles'), type_='foreignkey')
        batch_op.create_foreign_key('fk_medicines_user_id_users', 'users', ['user_id'], ['id'])
        batch_op.create_index('ix_medicines_cycle', ['cycle'], unique=False)
        batch_op.drop_column('cycle_id')

    op.create_table('_alembic_tmp_medicines',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=64), nullable=True),
    sa.Column('dose', sa.INTEGER(), nullable=True),
    sa.Column('period', sa.FLOAT(), nullable=True),
    sa.Column('taken', sa.BOOLEAN(), nullable=True),
    sa.Column('user_id', sa.INTEGER(), nullable=False),
    sa.Column('pills', sa.INTEGER(), nullable=True),
    sa.Column('cycle_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['cycle_id'], ['cycles.id'], name='fk_medicines_cycle_id_cycles'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='fk_medicines_user_id_users'),
    sa.PrimaryKeyConstraint('id', name='pk_medicines')
    )
    # ### end Alembic commands ###
