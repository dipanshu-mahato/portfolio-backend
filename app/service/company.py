from app.model.company import Company
from app.dto.company import CompanyCreate, CompanyUpdate
from app.service.base import Base

company = Base[Company, CompanyCreate, CompanyUpdate](Company)