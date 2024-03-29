"""empty message

Revision ID: 85f6b3ac18f9
Revises: 
Create Date: 2019-07-05 04:49:25.779128

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '85f6b3ac18f9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('customers')
    op.drop_table('contactid')
    op.drop_table('contact')
    op.drop_table('con')
    op.drop_table('customer_orders')
    op.drop_table('Contactus')
    op.drop_table('regtable')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('regtable',
    sa.Column('userid', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('username', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('email', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('pwd', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('user_created_on', mysql.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('userid'),
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    op.create_table('Contactus',
    sa.Column('profile_id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('lastname', mysql.VARCHAR(length=20), nullable=False),
    sa.Column('firstname', mysql.VARCHAR(length=15), nullable=False),
    sa.Column('email', mysql.VARCHAR(length=250), nullable=True),
    sa.PrimaryKeyConstraint('profile_id'),
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    op.create_table('customer_orders',
    sa.Column('custord_id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('custord_date', mysql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('custord_amt', mysql.FLOAT(), nullable=False),
    sa.Column('custord_status', mysql.TINYINT(display_width=4), server_default=sa.text("'0'"), autoincrement=False, nullable=False, comment='=1 if paid, 0 if not paid'),
    sa.Column('custord_custid', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('custord_id'),
    comment='This table stores the orders made by the customers',
    mysql_comment='This table stores the orders made by the customers',
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    op.create_table('con',
    sa.Column('con_id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('cont_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('con_id'),
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    op.create_table('contact',
    sa.Column('profile_id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('firstname', mysql.VARCHAR(length=15), nullable=False),
    sa.Column('email', mysql.VARCHAR(length=250), nullable=True),
    sa.Column('message', mysql.VARCHAR(length=250), nullable=True),
    sa.PrimaryKeyConstraint('profile_id'),
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    op.create_table('contactid',
    sa.Column('contact_id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.PrimaryKeyConstraint('contact_id'),
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    op.create_table('customers',
    sa.Column('cust_id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('cust_fname', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('cust_lname', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('cust_dob', sa.DATE(), nullable=False),
    sa.Column('cust_phone', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('cust_city', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('stat', mysql.ENUM('active', 'inactive'), nullable=True),
    sa.Column('cust_regdate', mysql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('cust_pickup', mysql.TIMESTAMP(), server_default=sa.text("'0000-00-00 00:00:00'"), nullable=False),
    sa.PrimaryKeyConstraint('cust_id'),
    comment='This table stores the information about our customers',
    mysql_comment='This table stores the information about our customers',
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###
