"""empty message

Revision ID: 5ba1b48c72dc
Revises: e4dc99b28337
Create Date: 2021-06-16 00:20:46.059800

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5ba1b48c72dc'
down_revision = 'e4dc99b28337'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('etudiants', sa.Column('matricule', sa.String(), nullable=False))
    op.create_unique_constraint(None, 'etudiants', ['matricule'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'etudiants', type_='unique')
    op.drop_column('etudiants', 'matricule')
    # ### end Alembic commands ###