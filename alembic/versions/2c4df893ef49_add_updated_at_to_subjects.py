"""add updated-at to subjects

Revision ID: 2c4df893ef49
Revises: 
Create Date: 2021-03-27 20:39:22.997192

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2c4df893ef49'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('subjects', sa.Column('updated_at', sa.DateTime(), nullable=True))
    op.create_index(op.f('ix_subjects_updated_at'), 'subjects', ['updated_at'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_subjects_updated_at'), table_name='subjects')
    op.drop_column('subjects', 'updated_at')
    # ### end Alembic commands ###
