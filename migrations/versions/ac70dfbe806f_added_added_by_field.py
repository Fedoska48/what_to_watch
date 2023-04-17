"""added added_by field

Revision ID: ac70dfbe806f
Revises: 
Create Date: 2023-04-17 21:08:52.030204

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ac70dfbe806f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('opinion', schema=None) as batch_op:
        batch_op.add_column(sa.Column('added_by', sa.String(length=64), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('opinion', schema=None) as batch_op:
        batch_op.drop_column('added_by')

    # ### end Alembic commands ###