"""make_name_nullable

Revision ID: e2a1bf05cd18
Revises: 19607203d2d4
Create Date: 2023-10-14 14:01:06.391957

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e2a1bf05cd18'
down_revision = '19607203d2d4'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'email',
               existing_type=sa.VARCHAR(length=255),
               nullable=True,
               schema='application')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'email',
               existing_type=sa.VARCHAR(length=255),
               nullable=False,
               schema='application')
    # ### end Alembic commands ###