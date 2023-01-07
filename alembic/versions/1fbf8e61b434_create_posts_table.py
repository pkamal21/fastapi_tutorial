"""create posts table

Revision ID: 1fbf8e61b434
Revises: 
Create Date: 2023-01-07 19:31:48.000779

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1fbf8e61b434'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("posts", sa.Column("id", sa.Integer, nullable=False, primary_key=True),
                             sa.Column("title", sa.String(), nullable=False))


def downgrade() -> None:
    op.drop_table("posts")
