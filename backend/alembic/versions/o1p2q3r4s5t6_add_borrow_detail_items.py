# """Tambah tabel borrow_detail_items untuk tracking SN yang dipilih per transaksi.

# Revision ID: o1p2q3r4s5t6
# Revises: n5o6p7q8r9s0
# Create Date: 2026-08-02 10:00:00.000000
# """
# from typing import Sequence, Union
# from alembic import op
# import sqlalchemy as sa


# revision: str = 'o1p2q3r4s5t6'
# down_revision: Union[str, None] = 'n5o6p7q8r9s0'
# branch_labels: Union[str, Sequence[str], None] = None
# depends_on: Union[str, Sequence[str], None] = None


# def upgrade() -> None:
#     op.create_table(
#         'borrow_detail_items',
#         sa.Column('id', sa.BigInteger(), primary_key=True, autoincrement=True),
#         sa.Column('borrow_detail_id', sa.BigInteger(),
#                   sa.ForeignKey('borrow_details.id', ondelete='CASCADE'), nullable=False),
#         sa.Column('inventory_item_id', sa.BigInteger(),
#                   sa.ForeignKey('inventory_items.id', ondelete='RESTRICT'), nullable=False),
#         sa.Column('created_at', sa.DateTime(), server_default=sa.func.now()),
#         sa.UniqueConstraint('borrow_detail_id', 'inventory_item_id',
#                             name='uq_borrow_detail_item'),
#     )


# def downgrade() -> None:
#     op.drop_table('borrow_detail_items')


"""Tambah tabel inventory_items dan borrow_detail_items untuk tracking SN.

Revision ID: o1p2q3r4s5t6
Revises: n5o6p7q8r9s0
Create Date: 2026-08-02 10:00:00.000000
"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa


revision: str = 'o1p2q3r4s5t6'
down_revision: Union[str, None] = 'n5o6p7q8r9s0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # 1. Buat tabel inventory_items (unit fisik per Serial Number)
    op.create_table(
        'inventory_items',
        sa.Column('id', sa.BigInteger(), primary_key=True, autoincrement=True),
        sa.Column('inventory_component_id', sa.BigInteger(),
                  sa.ForeignKey('inventory_components.id', ondelete='CASCADE'), nullable=False),
        sa.Column('serial_number', sa.String(100), nullable=True),
        sa.Column('status_id', sa.BigInteger(),
                  sa.ForeignKey('inventory_status.id', ondelete='RESTRICT'), nullable=False),
        sa.Column('deleted_at', sa.DateTime(), nullable=True),
        sa.Column('created_at', sa.DateTime(), server_default=sa.func.now(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), server_default=sa.func.now(),
                  onupdate=sa.func.now(), nullable=True),
    )

    # 2. Buat tabel borrow_detail_items (tracking SN yang dipinjam)
    op.create_table(
        'borrow_detail_items',
        sa.Column('id', sa.BigInteger(), primary_key=True, autoincrement=True),
        sa.Column('borrow_detail_id', sa.BigInteger(),
                  sa.ForeignKey('borrow_details.id', ondelete='CASCADE'), nullable=False),
        sa.Column('inventory_item_id', sa.BigInteger(),
                  sa.ForeignKey('inventory_items.id', ondelete='RESTRICT'), nullable=False),
        sa.Column('created_at', sa.DateTime(), server_default=sa.func.now(), nullable=True),
        sa.UniqueConstraint('borrow_detail_id', 'inventory_item_id',
                            name='uq_borrow_detail_item'),
    )


def downgrade() -> None:
    op.drop_table('borrow_detail_items')
    op.drop_table('inventory_items')