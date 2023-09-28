USE FoodDistribution;

select Code_article as "code article", Libelle, Conditionnement, famille, PU_HT as "prix unitaire" from conditionnement
left join principale on Conditionnement.id = conditionnement_id
left join famille on famille_id = famille.id