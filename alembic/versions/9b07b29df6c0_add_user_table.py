"""Add user table

Revision ID: 9b07b29df6c0
Revises: 74e1bee55a71
Create Date: 2023-01-07 19:47:12.161113

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9b07b29df6c0'
down_revision = '74e1bee55a71'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("users", sa.Column("id", sa.Integer(), primary_key=True),
                             sa.Column("email", sa.String(), nullable=False),
                             sa.Column("password", sa.String(), nullable=False),
                             sa.Column("created_at", sa.TIMESTAMP(timezone=True),
                                        server_default=sa.text("now()"), nullable=False),
                             sa.PrimaryKeyConstraint("id"),
                             sa.UniqueConstraint("email")
                        )


def downgrade() -> None:
    op.drop_table("users")
    pass
