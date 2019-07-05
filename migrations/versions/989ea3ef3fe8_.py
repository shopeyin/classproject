"""empty message

Revision ID: 989ea3ef3fe8
Revises: 85f6b3ac18f9
Create Date: 2019-07-05 05:05:55.511560

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '989ea3ef3fe8'
down_revision = '85f6b3ac18f9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('userprofile', sa.Column('surname', sa.String(length=255), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('userprofile', 'surname')
    # ### end Alembic commands ###
