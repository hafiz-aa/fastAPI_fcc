"""add foreign-key to posts table

Revision ID: 7207eb70ec48
Revises: 29256b0a710b
Create Date: 2023-01-04 11:23:43.765976

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7207eb70ec48'
down_revision = '29256b0a710b'
branch_labels = None
depends_on = None


def upgrade() -> None:
	op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
	op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users", local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")

	pass


def downgrade() -> None:
	op.drop_constraint('post_users_fk', table_name="posts")
	op.drop_column('posts', 'owner_id')
	pass
