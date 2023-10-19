"""Renaming students to scholars

Revision ID: acb88236dd35
Revises: 791279dd0760
Create Date: 2023-10-20 00:16:45.812104

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'acb88236dd35'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')