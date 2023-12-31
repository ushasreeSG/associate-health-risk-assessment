"""final_version

Revision ID: 19607203d2d4
Revises: 70820378e527
Create Date: 2023-10-13 22:16:11.620545

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '19607203d2d4'
down_revision = '70820378e527'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('recommendation', sa.Column('consequence', sa.String(length=512), nullable=False), schema='application')
    op.add_column('recommendation', sa.Column('recommendation_id', sa.Integer(), nullable=False), schema='application')
    op.create_unique_constraint(None, 'recommendation', ['recommendation_id'], schema='application')
    op.create_unique_constraint(None, 'recommendation', ['consequence'], schema='application')
    op.drop_constraint('recommendation_combination_id_fkey', 'recommendation', schema='application', type_='foreignkey')
    op.drop_column('recommendation', 'combination_id', schema='application')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('recommendation', sa.Column('combination_id', postgresql.UUID(), autoincrement=False, nullable=True), schema='application')
    op.create_foreign_key('recommendation_combination_id_fkey', 'recommendation', 'combinations', ['combination_id'], ['id'], source_schema='application', referent_schema='application')
    op.drop_constraint(None, 'recommendation', schema='application', type_='unique')
    op.drop_constraint(None, 'recommendation', schema='application', type_='unique')
    op.drop_column('recommendation', 'recommendation_id', schema='application')
    op.drop_column('recommendation', 'consequence', schema='application')
    # ### end Alembic commands ###
