CREATE VIEW gold.calender AS
SELECT * 
from OPENROWSET(BULK 'https://adventureorksdatalake.dfs.core.windows.net/silver/AdventureWorks_Calendar/',
FORMAT = 'parquet');

CREATE VIEW gold.customers AS
SELECT * 
from OPENROWSET(BULK 'https://adventureorksdatalake.dfs.core.windows.net/silver/AdventureWorks_Customers/',
FORMAT = 'parquet');

CREATE VIEW gold.product_cat AS
SELECT * 
from OPENROWSET(BULK 'https://adventureorksdatalake.dfs.core.windows.net/silver/AdventureWorks_Product_Categories/',
FORMAT = 'parquet');

CREATE VIEW gold.product_returns AS
SELECT * 
from OPENROWSET(BULK 'https://adventureorksdatalake.dfs.core.windows.net/silver/AdventureWorks_Product_Returns/',
FORMAT = 'parquet');

CREATE VIEW gold.product_subcat AS
SELECT * 
from OPENROWSET(BULK 'https://adventureorksdatalake.dfs.core.windows.net/silver/AdventureWorks_Product_Subcategories/',
FORMAT = 'parquet');

CREATE VIEW gold.products AS
SELECT * 
from OPENROWSET(BULK 'https://adventureorksdatalake.dfs.core.windows.net/silver/AdventureWorks_Products/',
FORMAT = 'parquet');

CREATE VIEW gold.sales AS
SELECT * 
from OPENROWSET(BULK 'https://adventureorksdatalake.dfs.core.windows.net/silver/AdventureWorks_sales/',
FORMAT = 'parquet');

CREATE VIEW gold.territories AS
SELECT * 
from OPENROWSET(BULK 'https://adventureorksdatalake.dfs.core.windows.net/silver/AdventureWorks_Territories/',
FORMAT = 'parquet');
