"""add last few columns to posts table

Revision ID: 126a3140dc84
Revises: 7207eb70ec48
Create Date: 2023-01-04 11:46:21.035017

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '126a3140dc84'
down_revision = '7207eb70ec48'
branch_labels = None
depends_on = None


def upgrade() -> None:
		op.add_column('posts', sa.Column(
			'published', sa.Boolean(), nullable=False, server_default='TRUE'))
		op.add_column('posts', sa.Column(
			'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')
		))
		pass 


def downgrade() -> None:
		op.drop_column('posts', 'published')
		op.drop_column('posts', 'created_at')
		pass
