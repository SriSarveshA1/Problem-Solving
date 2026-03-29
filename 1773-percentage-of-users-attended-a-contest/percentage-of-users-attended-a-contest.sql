
select contest_id , ROUND((count(user_id) / (select count(*) from users) *100),2) as percentage from register as r
 group by contest_id order by percentage desc, r.contest_id asc;