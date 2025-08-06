import enum
from sqlalchemy.dialects.postgresql import ENUM

class EnumCompanyTier(str, enum.Enum):
    tier_1 = "1"
    tier_2 = "2"
    tier_3 = "3"

pg_tier_enum: ENUM = ENUM(
    '1', '2', '3',
    name='enum_company_tier',
    schema='core',
    create_type=False
)

class EnumInterviewFeedback(str, enum.Enum):
    waiting = "waiting"
    strong_yes = "strong_yes"
    lean_yes = "lean_yes"
    neutral = "neutral"
    hold = "hold"
    lean_no = "lean_no"
    strong_no = "strong_no"
    eliminated = "eliminated"
    red_flag = "red_flag"

pg_feedback_enum: ENUM = ENUM(
    'waiting', 'strong_yes', 'lean_yes', 'neutral',
    'hold', 'lean_no', 'strong_no', 'eliminated', 'red_flag',
    name='enum_interview_feedback',
    schema='core',
    create_type=False
)

class EnumApplicationStatus(str, enum.Enum):
    applied = "applied"
    shortlisted = "shortlisted"
    assessment = "assessment"
    phone_screen = "phone_screen"
    interview = "interview"
    hr = "hr"
    offered = "offered"
    accepted = "accepted"
    rejected = "rejected"
    ghosted = "ghosted"

pg_status_enum: ENUM = ENUM(
    'applied', 'shortlisted', 'assessment', 'phone_screen',
    'interview', 'hr', 'offered', 'accepted', 'rejected',
    'ghosted',
    name='enum_application_status',
    schema='core',
    create_type=False
)