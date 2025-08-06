import enum
from sqlalchemy.dialects.postgresql import ENUM

class EnumCompanyTier(str, enum.Enum):
    tier_1 = "1"
    tier_2 = "2"
    tier_3 = "3"

pg_tier_enum = ENUM(
    '1', '2', '3',
    name='enum_company_tier',
    schema='core',
    create_type=False
)

