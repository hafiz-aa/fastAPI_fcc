"""add content column to posts table

Revision ID: c7df8ee2636c
Revises: e66bc55565bd
Create Date: 2023-01-04 10:38:14.608035

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c7df8ee2636c'
down_revision = 'e66bc55565bd'
branch_labels = None
depends_on = None


def upgrade() -> None:
	op.add_column('posts', sa.Column('content', sa.String(), nullable = False))
	pass


def downgrade() -> None:
	op.drop_column('posts', 'content')
	pass
