-- select last_name, count(*) from actor
-- group by (last_name)

-- select last_name, actor_id from actor
-- where last_name =
-- (select random_nom 
-- from 
-- (select last_name as random_nom from actor
-- order by rand()
-- limit 1) as random_table)
-- limit 1

-- select film_id, actor.last_name, actor.actor_id 
-- from film_actor
-- left join actor on
-- film_actor.actor_id = actor.actor_id
-- where actor.actor_id =
-- (select actor.actor_id 
-- from actor
-- where last_name =
-- (select random_nom 
-- from 
-- (select last_name as random_nom from actor
-- order by rand()
-- limit 1) as random_table)
-- limit 1)

select film.film_id, actor.first_name, actor.last_name, actor.actor_id, film.title
from actor
left join film_actor on film_actor.actor_id = actor.actor_id 
left join film on film_actor.film_id = film.film_id
where actor.actor_id =
(select actor.actor_id 
from actor
where last_name =
(select random_nom 
from 
(select last_name as random_nom from actor
order by rand()
limit 1) as random_table)
limit 1)






 


