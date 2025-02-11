"""update customer video and rental model.

Revision ID: cd303e62d63a
Revises: 2d899c069eba
Create Date: 2021-05-18 18:31:25.373769

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cd303e62d63a'
down_revision = '2d899c069eba'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('customer', sa.Column('videos_checked_out_count', sa.Integer(), nullable=True))
    op.add_column('rental', sa.Column('due_date', sa.DateTime(), nullable=True))
    op.add_column('video', sa.Column('available_inventory', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('video', 'available_inventory')
    op.drop_column('rental', 'due_date')
    op.drop_column('customer', 'videos_checked_out_count')
    # ### end Alembic commands ###
