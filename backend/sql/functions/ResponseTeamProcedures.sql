-- Table ResponseTeam {
--   ResponseTeamUUID uuid 
--   ResponseTeamDescription text 
--   ResponseTeamName varchar
-- }

CREATE OR REPLACE PROCEDURE CreateResponseTeam(TeamName VARCHAR, TeamDesc TEXT)
LANGUAGE plpgsql
AS $$
BEGIN
   INSERT INTO ResponseTeam (ResponseTeamUUID, ResponseTeamDescription, ResponseTeamName)
   VALUES 
   (uuid_generate_v4(),TeamDesc,LastName,TeamName);
END;
$$;

CREATE OR REPLACE FUNCTION GetResponseTeams()
RETURNS TABLE (
    ResponseTeamUUID UUID,
    ResponseTeamDescription TEXT,
    ResponseTeamName VARCHAR
) 
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT ResponseTeam.ResponseTeamUUID, ResponseTeam.ResponseTeamDescription, ResponseTeam.ResponseTeamName
    FROM ResponseTeam ; 
END;
$$;

CREATE OR REPLACE FUNCTION GetResponseTeamById(TeamId UUID)
RETURNS TABLE (
    ResponseTeamUUID UUID,
    ResponseTeamDescription TEXT,
    ResponseTeamName VARCHAR
) 
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT ResponseTeam.ResponseTeamUUID, ResponseTeam.ResponseTeamDescription, ResponseTeam.ResponseTeamName
    FROM ResponseTeam
    WHERE ResponseTeam.ResponseTeamUUID = TeamId ; 
END;
$$;

CREATE OR REPLACE PROCEDURE UpdateResponseTeam(TeamId UUID, 
    TeamDesc VARCHAR DEFAULT NULL, 
    ResponseTeamName VARCHAR DEFAULT NULL
   )--Add Parameter called UserId Here. Add Optional parameters for RoleId, FirstName, and LastName
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE ResponseTeam            -- Update statement to update a user's Role, FirstName, or LastName 
    SET ResponseTeamDescription = COALESCE(TeamDesc, ResponseTeam.ResponseTeamDescription), 
        ResponseTeamName = COALESCE(TeamName, ResponseTeam.ResponseTeamName)
    WHERE ResponseTeam.ResponseTeamUUID = TeamId;                                 -- where account.UserUUID = UserId
END;
$$;

CREATE OR REPLACE PROCEDURE DeleteResponseTeam(TeamId UUID)
LANGUAGE plpgsql
AS $$
BEGIN
DELETE FROM ResponseTeam
WHERE ResponseTeamUUID = TeamId;
END;
$$;

CREATE OR REPLACE PROCEDURE InsertResponseTeamUser(UserId UUID, TeamId UUID)
LANGUAGE plpgsql
AS $$
BEGIN
   INSERT INTO ResponseTeam_Account (UserUUID, ResponseTeamUUID)
   VALUES (UserId, TeamId);
END;
$$;

CREATE OR REPLACE PROCEDURE DeleteResponseTeamUser(UserId UUID, TeamId UUID)
LANGUAGE plpgsql
AS $$
BEGIN
DELETE FROM ResponseTeam_Account
WHERE ResponseTeamUUID = TeamId AND UserUUID = UserId;
END;
$$;

-- Table ResponseTeam_Account { 
--   UserUUID uuid 
--   ResponseTeamUUID uuid
-- }
