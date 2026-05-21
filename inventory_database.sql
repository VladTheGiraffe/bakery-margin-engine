INSERT INTO bakery_demo.recipe_ingredients (recipe_id, item_id, quantity)
VALUES (
    (SELECT recipe_id
    FROM recipes
    WHERE product = 'Potato Chips'),
    (SELECT item_id
    FROM ingredients
    WHERE ingredient = 'Potato Chips'),
    1
)
