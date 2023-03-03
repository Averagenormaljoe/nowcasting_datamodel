"""empty message

Revision ID: 155dcbad36df
Revises: 4d245e892640
Create Date: 2023-03-03 10:26:15.127508

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "155dcbad36df"
down_revision = "4d245e892640"
branch_labels = None
depends_on = None


def upgrade(): # noqa
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("metric_value", sa.Column("time_of_day", sa.Time(), nullable=True))
    # ### end Alembic commands ###


def downgrade(): # noqa
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("metric_value", "time_of_day")
    # ### end Alembic commands ###
