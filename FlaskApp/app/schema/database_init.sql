-- Login psql terminal --
$su postgres
$psql


-- Create Super User --
BEGIN transaction;
CREATE USER postgres WITH SUPERUSER LOGIN;
CREATE USER stockwebuser WITH SUPERUSER LOGIN;
COMMIT;

-- Create Database --
BEGIN transaction;
CREATE DATABASE stockmonster;
COMMIT;

-- tests ran --
-- stockmonster=# \du
--                                List of roles
--   Role name   |                   Attributes                   | Member of 
-- --------------+------------------------------------------------+-----------
--  postgres     | Superuser                                      | {}
--  stockwebuser | Superuser                                      | {}
