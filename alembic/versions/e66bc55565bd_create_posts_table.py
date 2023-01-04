"""create posts table

Revision ID: e66bc55565bd
Revises: 
Create Date: 2023-01-04 09:55:43.105628

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e66bc55565bd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
      'posts', 
      sa.Column('id', sa.Integer(), nullable = False, primary_key = True),
      sa.Column('title', sa.String(), nullable = False))
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
