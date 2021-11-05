"""empty message

Revision ID: a884f604b15f
Revises: 2807edd385a2
Create Date: 2021-11-05 23:27:02.107779

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a884f604b15f'
down_revision = '2807edd385a2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('incomes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('type', sa.Enum('work', 'capital', name='incometype'), nullable=False),
    sa.Column('subtype', sa.String(length=250), nullable=False),
    sa.Column('currency', sa.Enum('UYU', 'USD', name='currencytype'), nullable=False),
    sa.Column('description', sa.String(length=250), nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('amount', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('outgoings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('type', sa.Enum('Entertainment', 'Food', 'Home', 'Life', 'Transport', 'Vacations', 'Services', name='outgoingtype'), nullable=False),
    sa.Column('subtype', sa.String(length=250), nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('currency', sa.Enum('UYU', 'USD', name='currencytype'), nullable=False),
    sa.Column('amount', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=250), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('user', sa.Column('lastname', sa.String(length=250), nullable=False))
    op.add_column('user', sa.Column('name', sa.String(length=250), nullable=False))
    op.drop_constraint('user_email_key', 'user', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('user_email_key', 'user', ['email'])
    op.drop_column('user', 'name')
    op.drop_column('user', 'lastname')
    op.drop_table('outgoings')
    op.drop_table('incomes')
    # ### end Alembic commands ###