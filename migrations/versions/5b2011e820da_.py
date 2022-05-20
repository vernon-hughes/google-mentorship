"""empty message

Revision ID: 5b2011e820da
Revises: f40b630c95a0
Create Date: 2022-05-02 11:54:51.082987

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5b2011e820da'
down_revision = 'f40b630c95a0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('patients',
    sa.Column('patient_id', sa.Integer(), nullable=True),
    sa.Column('caretaker_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['caretaker_id'], ['users.id'], name=op.f('fk_patients_caretaker_id_users')),
    sa.ForeignKeyConstraint(['patient_id'], ['users.id'], name=op.f('fk_patients_patient_id_users'))
    )
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('isPatient', sa.Boolean(), nullable=True))
        batch_op.create_index(batch_op.f('ix_users_isPatient'), ['isPatient'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_users_isPatient'))
        batch_op.drop_column('isPatient')

    op.drop_table('patients')
    # ### end Alembic commands ###