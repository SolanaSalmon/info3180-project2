"""empty message

Revision ID: 564125341545
Revises: e4475a3c9e71
Create Date: 2016-03-31 22:53:00.158868

"""

# revision identifiers, used by Alembic.
revision = '564125341545'
down_revision = 'e4475a3c9e71'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('wishes', sa.Column('thumbnail', sa.String(length=255), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('wishes', 'thumbnail')
    ### end Alembic commands ###
