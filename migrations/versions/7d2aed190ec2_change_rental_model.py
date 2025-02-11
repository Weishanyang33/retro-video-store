"""change rental model.

Revision ID: 7d2aed190ec2
Revises: cd303e62d63a
Create Date: 2021-05-18 20:03:22.356812

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7d2aed190ec2'
down_revision = 'cd303e62d63a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('rental', sa.Column('customer_id', sa.Integer(), nullable=False))
    op.add_column('rental', sa.Column('video_id', sa.Integer(), nullable=False))
    op.drop_constraint('rental_rental_video_id_fkey', 'rental', type_='foreignkey')
    op.drop_constraint('rental_rental_customer_id_fkey', 'rental', type_='foreignkey')
    op.create_foreign_key(None, 'rental', 'customer', ['customer_id'], ['customer_id'])
    op.create_foreign_key(None, 'rental', 'video', ['video_id'], ['video_id'])
    op.drop_column('rental', 'rental_video_id')
    op.drop_column('rental', 'rental_customer_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('rental', sa.Column('rental_customer_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.add_column('rental', sa.Column('rental_video_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'rental', type_='foreignkey')
    op.drop_constraint(None, 'rental', type_='foreignkey')
    op.create_foreign_key('rental_rental_customer_id_fkey', 'rental', 'customer', ['rental_customer_id'], ['customer_id'])
    op.create_foreign_key('rental_rental_video_id_fkey', 'rental', 'video', ['rental_video_id'], ['video_id'])
    op.drop_column('rental', 'video_id')
    op.drop_column('rental', 'customer_id')
    # ### end Alembic commands ###
