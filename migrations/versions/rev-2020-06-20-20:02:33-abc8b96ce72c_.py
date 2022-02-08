"""empty message

Revision ID: abc8b96ce72c
Revises: 9540464e9b57
Create Date: 2020-06-20 20:02:33.984247

"""

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = 'abc8b96ce72c'
down_revision = '9540464e9b57'


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('custom_forms', 'name',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('custom_forms', 'name',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###