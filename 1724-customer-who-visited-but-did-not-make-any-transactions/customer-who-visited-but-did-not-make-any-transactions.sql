SELECT customer_id,count(customer_id) as count_no_trans from Visits v where NOT EXISTS (SELECT visit_id from Transactions t where t.visit_id = v.visit_id) group by customer_id;