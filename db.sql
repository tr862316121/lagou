CREATE DATABASE lagou;
USE lagou;
CREATE TABLE result (
	ID INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	ResultId VARCHAR(200) NOT NULL,
	
	CompanyId BIGINT,
	PositionId BIGINT,
	CreateTimeSort BIGINT,
	
	PositionName NVARCHAR(100),
	PositionType NVARCHAR(100),
	CreateTime VARCHAR(50),
	CompanyShortName NVARCHAR(200),
	City NVARCHAR(80),
	CompanyName NVARCHAR(200),
    CompanyLogo VARCHAR(200)
)

insert into result(ResultId, CompanyId, PositionId, CreateTimeSort, PositionName, PositionType, CreateTime, CompanyShortName, City, CompanyName, CompanyLogo ) values 
('MTE0MjM3LTE3ODQ2NzEtMTQ2MjQwNDAzNDAwMA==', 114237, 1784671, 1462404034000, '销售专员', '销售', '2016-05-05 07:20:34', '厦门笨鸟电子商务有限公司', '上海', '笨鸟社交上海分公司', 'i/image/M00/03/CD/Cgp3O1bDyBKACV66AAxOb_S_ZUA765.jpg');


