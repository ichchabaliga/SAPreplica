
DROP database IF EXISTS sapreplica;
create database if not exists sapreplica;
use sapreplica;
CREATE TABLE if not exists BVOR (
    IntercompanyNo VARCHAR(10) NOT NULL ,
    CompanyCode VARCHAR(6) NOT NULL,
    FiscalYear YEAR NOT NULL,
    DocumentNo VARCHAR(10) NOT NULL,
    PRIMARY KEY (IntercompanyNo, CompanyCode, DocumentNo, FiscalYear)

);
CREATE INDEX index_name ON BVOR(CompanyCode, DocumentNo, FiscalYear);


CREATE TABLE if not exists BKPF (
    CompanyCode VARCHAR(6) NOT NULL,
    DocumentNo VARCHAR(10) NOT NULL,
    FiscalYear YEAR NOT NULL,
    PRIMARY KEY (CompanyCode, DocumentNo, FiscalYear),
    FOREIGN KEY (CompanyCode, DocumentNo, FiscalYear) REFERENCES BVOR(CompanyCode, DocumentNo, FiscalYear)

);

CREATE TABLE if not exists BSEG (
    CompanyCode VARCHAR(6) NOT NULL,
    DocumentNo VARCHAR(10) NOT NULL,
    FiscalYear YEAR(4) NOT NULL,
    LineItem INT(3) NOT NULL,
    PRIMARY KEY (CompanyCode, DocumentNo, FiscalYear, LineItem),
    FOREIGN KEY (CompanyCode, DocumentNo, FiscalYear) REFERENCES BKPF(CompanyCode, DocumentNo, FiscalYear)
);


CREATE TABLE if not exists BSEC (
    CompanyCode VARCHAR(6) NOT NULL,
    DocumentNo VARCHAR(10) NOT NULL,
    FiscalYear YEAR(4) NOT NULL,
    LineItem INT(3) NOT NULL,
    PRIMARY KEY (CompanyCode, DocumentNo, FiscalYear, LineItem),
FOREIGN KEY (CompanyCode, DocumentNo, FiscalYear) REFERENCES BKPF(CompanyCode, DocumentNo, FiscalYear)
);

CREATE TABLE if not exists BSET (
    CompanyCode VARCHAR(6) NOT NULL,
    DocumentNo VARCHAR(10) NOT NULL,
    FiscalYear YEAR(4) NOT NULL,
    LineItem INT(3) NOT NULL,
    PRIMARY KEY (CompanyCode, DocumentNo, FiscalYear, LineItem),
FOREIGN KEY (CompanyCode, DocumentNo, FiscalYear) REFERENCES BKPF(CompanyCode, DocumentNo, FiscalYear)
);


CREATE TABLE if not exists BSAD (
    CompanyCode VARCHAR(6) NOT NULL,
    CustomerNo VARCHAR(10) NOT NULL,
    SpecialGLTrans CHAR(4),
    SpecialGLInd CHAR(4),
    ClearingDate DATE,
    ClearingDoc VARCHAR(10),
    AllocationNo VARCHAR(10),
    FiscalYear YEAR(4) NOT NULL,
    DocumentNo VARCHAR(10) NOT NULL,
    LineItem INT(3) NOT NULL,
    PRIMARY KEY (CompanyCode, CustomerNo, FiscalYear, DocumentNo, LineItem),
FOREIGN KEY (CompanyCode, DocumentNo, FiscalYear, LineItem) REFERENCES BSEG(CompanyCode, DocumentNo, FiscalYear, LineItem)
);


CREATE TABLE if not exists BSID (
    CompanyCode VARCHAR(6) NOT NULL,
    CustomerNo VARCHAR(10) NOT NULL,
    SpecialGLTrans CHAR(4),
    SpecialGLInd CHAR(4),
    ClearingDate DATE,
    ClearingDoc VARCHAR(10),
    AllocationNo VARCHAR(10),
    FiscalYear YEAR(4) NOT NULL,
    DocumentNo VARCHAR(10) NOT NULL,
    LineItem INT(3) NOT NULL,
    PRIMARY KEY (CompanyCode, FiscalYear, DocumentNo, CustomerNo,LineItem),
FOREIGN KEY (CompanyCode, DocumentNo, FiscalYear,LineItem) REFERENCES BSEG(CompanyCode, DocumentNo, FiscalYear,LineItem)


);

CREATE TABLE if not exists BSIS (
    GLAccount VARCHAR(10) NOT NULL,
    CompanyCode VARCHAR(6) NOT NULL,
    ClearingDate DATE,
    ClearingDoc VARCHAR(10),
    AllocationNo VARCHAR(10),
    FiscalYear YEAR NOT NULL,
    DocumentNo VARCHAR(10) NOT NULL,
    LineItem INT(3) NOT NULL,
    PRIMARY KEY (GLAccount, CompanyCode, FiscalYear,LineItem),
FOREIGN KEY (CompanyCode, DocumentNo, FiscalYear, LineItem) REFERENCES BSEG(CompanyCode, DocumentNo, FiscalYear, LineItem)

);

CREATE TABLE if not exists BSAS (
    GLAccount VARCHAR(10) NOT NULL,
    CompanyCode VARCHAR(6) NOT NULL,
    ClearingDate DATE,
    ClearingDoc VARCHAR(10),
    AllocationNo VARCHAR(10),
    FiscalYear YEAR(4) NOT NULL,
    DocumentNo VARCHAR(10) NOT NULL,
	LineItem INT(3) NOT NULL,
    PRIMARY KEY (GLAccount, CompanyCode, FiscalYear, DocumentNo, LineItem ),
FOREIGN KEY (CompanyCode, DocumentNo, FiscalYear, LineItem) REFERENCES BSEG(CompanyCode, DocumentNo, FiscalYear, LineItem)

);

CREATE TABLE if not exists BSAK (
    CompanyCode VARCHAR(6) NOT NULL,
    Vendor VARCHAR(10) NOT NULL,
    SpecialGLTrans CHAR(4),
    SpecialGLInd CHAR(4),
    ClearingDate DATE,
    ClearingDoc VARCHAR(10),
    AllocationNo VARCHAR(10),
    FiscalYear YEAR NOT NULL,
    DocumentNo VARCHAR(10) NOT NULL,
    LineItem INT NOT NULL,
    PRIMARY KEY (CompanyCode, FiscalYear, DocumentNo, LineItem),
FOREIGN KEY (CompanyCode, DocumentNo, FiscalYear,LineItem) REFERENCES BSEG(CompanyCode, DocumentNo, FiscalYear, LineItem)


);

CREATE TABLE if not exists PAYR (
    PayingCompany VARCHAR(4) NOT NULL,
    HouseBank VARCHAR(5) NOT NULL,
    Account DECIMAL(15,2),
    PaymentMethod CHAR(15) NOT NULL,
    CheckNo VARCHAR(10),
    PRIMARY KEY (PayingCompany, PaymentMethod, HouseBank)
);

CREATE TABLE if not exists BSIP (
    CompanyCode VARCHAR(6) NOT NULL,
    Vendor VARCHAR(10) NOT NULL,
    Currency CHAR(3) NOT NULL,
    DocumentDate DATE NOT NULL,
    ReferenceDoc VARCHAR(10),
    Amount DECIMAL(15,2),
    DocumentNo VARCHAR(10) NOT NULL,
    FiscalYear YEAR(4) NOT NULL,
    LineItem INT NOT NULL,
    PRIMARY KEY (CompanyCode, FiscalYear, DocumentNo, LineItem),
FOREIGN KEY (CompanyCode, DocumentNo, FiscalYear) REFERENCES BKPF(CompanyCode, DocumentNo, FiscalYear)

);
-- Error Code: 3734. Failed to add the foreign key constraint. Missing column 'LineItem' for constraint 'bsip_ibfk_1' in the referenced table 'BKPF'
-- Error Code: 3734. Failed to add the foreign key constraint. Missing column 'CompanyCode' for constraint 'lfb1_ibfk_1' in the referenced table 'LFA1'


CREATE TABLE if not exists BSIK (
    CompanyCode VARCHAR(6) NOT NULL,
    Vendor VARCHAR(10) NOT NULL,
    SpecialGLTrans CHAR(4),
    SpecialGLInd CHAR(4),
    ClearingDate DATE,
    ClearingDoc VARCHAR(10),
    AllocationNo VARCHAR(10),
    FiscalYear YEAR(4) NOT NULL,
    DocumentNo VARCHAR(10) NOT NULL,
    LineItem INT NOT NULL,
    PRIMARY KEY (CompanyCode, FiscalYear, DocumentNo,LineItem),
FOREIGN KEY (CompanyCode, DocumentNo, FiscalYear,LineItem) REFERENCES BSEG(CompanyCode, DocumentNo, FiscalYear,LineItem)


);




CREATE TABLE if not exists LFC1 (
    VendorNo VARCHAR(10) NOT NULL,
    CompanyCode VARCHAR(6) NOT NULL,
    FiscalYear YEAR(4) NOT NULL,
    PRIMARY KEY (VendorNo, CompanyCode, FiscalYear)
);

CREATE TABLE if not exists KNC1 (
    CustomerNo VARCHAR(10) NOT NULL,
    CompanyCode VARCHAR(6) NOT NULL,
    FiscalYear YEAR(4) NOT NULL,
    PRIMARY KEY (CustomerNo, CompanyCode, FiscalYear)
);



CREATE TABLE LFA1 (
    VendorNo VARCHAR(10) NOT NULL PRIMARY KEY
);

CREATE TABLE LFM1 (
    VendorNo VARCHAR(10) NOT NULL,
    PurchOrg VARCHAR(4) NOT NULL,
    PRIMARY KEY (VendorNo, PurchOrg),
FOREIGN KEY (VendorNo) REFERENCES LFA1(VendorNo)

   

);

CREATE TABLE LFM2 (
    VendorNo VARCHAR(10) NOT NULL,
    PurchOrg VARCHAR(4) NOT NULL,
    Subrange VARCHAR(6),
    Plant VARCHAR(4) NOT NULL,
    PRIMARY KEY (VendorNo, PurchOrg, Plant),
FOREIGN KEY (VendorNo) REFERENCES LFM1(VendorNo)


);

CREATE TABLE LFB1 (
    VendorNo VARCHAR(10) NOT NULL,
    CompanyCode VARCHAR(6) NOT NULL,
    PRIMARY KEY(VendorNo,CompanyCode),
FOREIGN KEY (VendorNo) REFERENCES LFA1(VendorNo)

);
-- drop table LFB1;
CREATE TABLE LFBK (
    VendorNo VARCHAR(10) NOT NULL,
    BankKey VARCHAR(15) NOT NULL,
    BankCountry CHAR(3) NOT NULL,
    BankAcc VARCHAR(18),
    PRIMARY KEY (VendorNo, BankKey),
FOREIGN KEY (VendorNo) REFERENCES LFA1(VendorNo)

);

CREATE TABLE LFB5 (
    VendorNo VARCHAR(10) NOT NULL,
    CompanyCode VARCHAR(6) NOT NULL,
    DunningArea CHAR(3),
    PRIMARY KEY (VendorNo, CompanyCode,DunningArea),
FOREIGN KEY (VendorNo, CompanyCode) REFERENCES LFB1(VendorNo,CompanyCode)


);
-- —---------------------------Customer Master Data —--------------------------------------------------------------

CREATE TABLE KNA1 (
    CustomerNo VARCHAR(10) NOT NULL PRIMARY KEY
);
CREATE TABLE KNB1 (
    CustomerNo VARCHAR(10) NOT NULL,
    CompanyCode VARCHAR(6) NOT NULL,
    PRIMARY KEY (CustomerNo, CompanyCode),
FOREIGN KEY (CustomerNo) REFERENCES KNA1(CustomerNo)



);

CREATE TABLE KNVV (
    CustomerNo VARCHAR(10) NOT NULL,
    SalesOrg VARCHAR(4) NOT NULL,
    DistributionCh VARCHAR(4) NOT NULL,
    Division VARCHAR(4) NOT NULL,
    PRIMARY KEY (CustomerNo, SalesOrg, DistributionCh, Division),
    FOREIGN KEY (CustomerNo) REFERENCES KNA1(CustomerNo)

);

CREATE TABLE KNVP (
    CustomerNo VARCHAR(10) NOT NULL,
    SalesOrg VARCHAR(4) NOT NULL,
    DistributionCh VARCHAR(4) NOT NULL,
    Division VARCHAR(4) NOT NULL,
    PartnerFunction VARCHAR(5) NOT NULL,
    PartnerCounter VARCHAR(5) NOT NULL,
    PRIMARY KEY (CustomerNo, SalesOrg, DistributionCh, Division,PartnerFunction),
 FOREIGN KEY (CustomerNo,SalesOrg, DistributionCh, Division) REFERENCES KNVV(CustomerNo, SalesOrg, DistributionCh, Division)


);
CREATE TABLE KNVD (
    CustomerNo VARCHAR(10) NOT NULL,
    SalesOrg VARCHAR(4) NOT NULL,
    DistributionCh VARCHAR(4) NOT NULL,
    Division VARCHAR(4) NOT NULL,
    OutputType VARCHAR(5) NOT NULL,
    MessLanguage VARCHAR(5) NOT NULL,
    PRIMARY KEY (CustomerNo, SalesOrg, DistributionCh, Division,OutputType),
 FOREIGN KEY (CustomerNo, SalesOrg, DistributionCh, Division) REFERENCES KNVV(CustomerNo, SalesOrg, DistributionCh, Division)


);

CREATE TABLE KNB5 (
    CustomerNo VARCHAR(10) NOT NULL,
    CompanyCode VARCHAR(6) NOT NULL,
    DunningArea VARCHAR(4) NOT NULL,
    PRIMARY KEY (CustomerNo, CompanyCode, DunningArea),
FOREIGN KEY (CustomerNo,CompanyCode) REFERENCES KNB1(CustomerNo,CompanyCode)

);





