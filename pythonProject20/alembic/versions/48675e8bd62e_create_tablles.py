"""create tablles

Revision ID: 48675e8bd62e
Revises: 
Create Date: 2023-07-26 19:56:48.761660

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '48675e8bd62e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts',
                    sa.Column('id', sa.Integer(),  autoincrement=False, nullable=False),
                    sa.Column('title', sa.String(), nullable=False),
                    sa.Column('content', sa.String(), nullable=False),
                    sa.Column('created', sa.TIMESTAMP(),nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )


def downgrade() -> None:
    op.drop_table('posts')
