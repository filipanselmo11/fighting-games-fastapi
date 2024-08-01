"""Create personagens table

Revision ID: 995895e0e8d0
Revises: 
Create Date: 2024-08-01 14:01:54.790591

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '995895e0e8d0'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('personagens',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('nome', sa.String(), nullable=False),
    sa.Column('img', sa.String(), nullable=False),
    sa.Column('descricao', sa.String(), nullable=False),
    sa.Column('jogo', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('personagens')
    # ### end Alembic commands ###
