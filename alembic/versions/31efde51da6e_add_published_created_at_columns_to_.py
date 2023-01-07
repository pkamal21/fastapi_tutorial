"""add published, created_at columns to posts

Revision ID: 31efde51da6e
Revises: 8a40bed60d7d
Create Date: 2023-01-07 19:57:56.229932

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '31efde51da6e'
down_revision = '8a40bed60d7d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("published", sa.Boolean(), nullable=False, server_default='TRUE'))
    op.add_column("posts", sa.Column("created_at", sa.TIMESTAMP(timezone=True),
                                        server_default=sa.text("now()"), nullable=False))


def downgrade() -> None:
    op.drop_column("posts", "published")
    op.drop_column("posts", "created_at")
