"""add content column to posts table

Revision ID: 74e1bee55a71
Revises: 1fbf8e61b434
Create Date: 2023-01-07 19:43:35.449301

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '74e1bee55a71'
down_revision = '1fbf8e61b434'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))


def downgrade() -> None:
    op.drop_column("posts", "content")
