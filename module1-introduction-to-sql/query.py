# rpg queries
total_characters = """
SELECT COUNT(DISTINCT character_id)
	AS total_characters
FROM charactercreator_character;
"""

total_mage = """
SELECT COUNT(DISTINCT character_ptr_id)
	AS total_mages
FROM charactercreator_mage;
"""

total_thief = """
SELECT COUNT(DISTINCT character_ptr_id)
	AS total_thieves
FROM charactercreator_thief;
"""

total_cleric = """
SELECT COUNT(DISTINCT character_ptr_id)
	AS total_clerics
FROM charactercreator_cleric;
"""

total_fighter = """
SELECT COUNT(DISTINCT character_ptr_id)
	AS total_fighters
FROM charactercreator_fighter;
"""

total_items = """
SELECT COUNT(DISTINCT item_id)
	AS total_items
FROM armory_item;
"""

total_weapons = """
SELECT COUNT(DISTINCT item_id)
	AS total_weapon_items
FROM armory_item
INNER JOIN armory_weapon
	ON item_id = item_ptr_id;
"""

total_non_weapons = """
SELECT COUNT(DISTINCT item_id)
	AS total_nonweapon_items
FROM armory_item
LEFT JOIN armory_weapon
	ON item_id = item_ptr_id
WHERE item_ptr_id IS NULL;
"""

# Character items assumes two of the same item counts as having two items
# Assumes only want the number of items without matched to each character
character_items = """
SELECT COUNT(item_id) AS character_items
FROM charactercreator_character_inventory
GROUP BY character_id
LIMIT 20;
"""

# Character weapns makes same assumptions as character items
character_weapons = """
SELECT COUNT(item_ptr_id) AS character_weapons
FROM charactercreator_character_inventory
LEFT JOIN armory_weapon
	ON item_id = item_ptr_id
GROUP BY character_id
LIMIT 20;
"""

average_items = """
SELECT AVG(item_count.char_items)
	AS average_items
FROM
	(select count(*) as char_items
	FROM charactercreator_character_inventory inv
	GROUP BY inv.character_id) item_count
"""

average_weapons = """
SELECT AVG(weapon_count.char_weapons)
	AS average_weapons
FROM
	(select count(item_ptr_id) as char_weapons
	FROM charactercreator_character_inventory inv
	LEFT JOIN armory_weapon
		ON inv.item_id = armory_weapon.item_ptr_id
	GROUP BY inv.character_id) weapon_count
"""

QUERY_LIST = [total_characters, total_mage, total_thief, total_cleric, total_fighter,
                total_items, total_weapons, total_non_weapons, character_items, character_weapons,
                average_items, average_weapons]



# buddymove queries
rows_count = """
SELECT COUNT(*)
FROM review;
"""

min_100_nature_shopping = """
SELECT COUNT(*)
FROM review
WHERE Nature >= 100
AND Shopping >= 100;
"""

average_buddy_table = """
SELECT AVG(Sports), AVG(Religious), AVG(Nature),
	AVG(Theatre), AVG(Shopping), AVG(Picnic)
FROM review;
"""

BUDDY_QUERY_LIST = [rows_count, min_100_nature_shopping, average_buddy_table]