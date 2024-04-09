CREATE OR REPLACE PROCEDURE CreateAccount(FirstName VARCHAR, LastName VARCHAR, RoleId INT, Active BOOLEAN)
LANGUAGE plpgsql
AS $$
BEGIN
   INSERT INTO Account (UserUUID, UserFName, UserLName, AccountRoleId, isActive)
   VALUES 
   (uuid_generate_v4(),FirstName,LastName,RoleId,Active);
END;
$$;

-- CALL CreateAccount ('David', 'Danes', 3, False );

CREATE OR REPLACE FUNCTION GetAccountById(UserId UUID)
RETURNS TABLE (
    UserUUID UUID,
    UserFName VARCHAR,
    UserLName VARCHAR,
    CreatedOn TIMESTAMP,
    AccountRoleId INT,
    IsActive BOOLEAN
) 
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT account.UserUUID, account.UserFName, account.UserLName, account.CreatedOn, account.AccountRoleId, account.isActive
    FROM Account
    WHERE account.UserUUID = UserId ; 
END;
$$;

-- select * from  GetAccountById('2d81650b-5de9-4442-bc4b-d9990dbb296e');

CREATE OR REPLACE FUNCTION GetAccounts()
RETURNS TABLE (
    UserUUID UUID,
    UserFName VARCHAR,
    UserLName VARCHAR,
    CreatedOn TIMESTAMP,
    AccountRoleId INT,
    IsActive BOOLEAN
) 
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT account.UserUUID, account.UserFName, account.UserLName, account.CreatedOn, account.AccountRoleId, account.isActive
    FROM Account ; 
END;
$$;

-- SELECT * from GetAccounts();

CREATE OR REPLACE PROCEDURE UpdateAccount(UserId UUID, 
    FirstName VARCHAR DEFAULT NULL, 
    LastName VARCHAR DEFAULT NULL, 
    RoleId INT DEFAULT NULL, 
    Active BOOLEAN DEFAULT NULL)--Add Parameter called UserId Here. Add Optional parameters for RoleId, FirstName, and LastName
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE Account            -- Update statement to update a user's Role, FirstName, or LastName 
    SET UserFName = COALESCE(FirstName, Account.UserFName), 
        UserLName = COALESCE(LastName, Account.UserLName),
        AccountRoleId = COALESCE(RoleId, Account.AccountRoleId ), 
        isActive = COALESCE(Active, Account.isActive)
    WHERE Account.UserUUID = UserId;                                 -- where account.UserUUID = UserId
END;
$$;

-- CALL UpdateAccount(UserId => ,FirstName => ,LastName => ,RoleId =>,Active => )

CREATE OR REPLACE PROCEDURE DeleteAccount(UserID UUID)
LANGUAGE plpgsql
AS $$
BEGIN
DELETE FROM Account
WHERE UserUUID = UserId;
    -- Your SQL statements here
END;
$$;

-- CALL DeleteAccount(UserId => 'fb78ae80-ad7f-45f2-a86e-9efd750df977');

CREATE OR REPLACE PROCEDURE CreateAccountRole(AccountRoleName VARCHAR)
LANGUAGE plpgsql
AS $$
BEGIN
INSERT INTO Account_Role (AccountRoleName)
VALUES (AccountRoleName);
END;
$$;

-- CALL CreateAccountRole (AccountRoleName => 'Billing');


CREATE OR REPLACE FUNCTION GetAccountRoles()
RETURNS TABLE
(
    AccountRoleId INT,
    AccountRoleName VARCHAR
) 
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT Account_Role.AccountRoleId,
    Account_Role.AccountRoleName
    FROM Account_Role; 
END;
$$;

