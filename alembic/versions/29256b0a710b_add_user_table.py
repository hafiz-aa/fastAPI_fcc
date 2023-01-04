"""add user table

Revision ID: 29256b0a710b
Revises: c7df8ee2636c
Create Date: 2023-01-04 11:01:35.622905

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '29256b0a710b'
down_revision = 'c7df8ee2636c'
branch_labels = None
depends_on = None


def upgrade() -> None:
	op.create_table(
		'users',
		sa.Column('id', sa.Integer(), nullable=False),
		sa.Column('email', sa.String(), nullable=False),
		sa.Column('password', sa.String(), nullable=False),
		sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
		sa.PrimaryKeyConstraint('id'),
		sa.UniqueConstraint('email')
		)
	pass


def downgrade() -> None:
		op.drop_table('users')
		pass
