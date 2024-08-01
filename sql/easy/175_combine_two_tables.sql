-- Write your MySQL query statement below
-- Using a left join since we want the full table of the person, and we dont care that much about having the full address table.
SELECT FirstName,LastName,City,State
FROM Person
LEFT JOIN Address
USING(PersonId)