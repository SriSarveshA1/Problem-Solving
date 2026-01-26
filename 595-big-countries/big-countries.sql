# Write your MySQL query statement below
select w.name as name ,w.population as population ,w.area as area from World w where w.area >= 3000000 or population>=25000000;