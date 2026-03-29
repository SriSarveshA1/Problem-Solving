select s.user_id,round(coalesce(c.confirmation_rate,0.00),2) confirmation_rate from signups as s 
left join (select c.user_id, sum( CASE WHEN action='confirmed' then 1 else 0 end) / count(*)  as confirmation_rate from confirmations as c group by c.user_id) as c on c.user_id = s.user_id  
