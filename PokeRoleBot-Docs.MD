<h1>Table of Contents:</h1>

* [Slash Commands](#slash-commands)
	*  /encounter description
	*  Quick Reference commands
* [Quick Reference](#quick-reference)
	* Pokemon Stats
	* What Moves a Pokemon can learn
	* Finding Move Definitions
	* Items and what they do
	* Abilities
	* Habitats
* [Lists](#lists)
	* How do they work?
	* Creating, Modifying, and Deleting them
	* Quickly adding lots of similar pokemon
	* Adding pokemon from a habitat
	* Overview of item lists
* [Random Encounters](#random-encounters)
	* How do they work?
	* %encounter
	* %boss
	* I want a chance for a rarer encounter mixed in
* [Misc Commands](#misc-commands)
	* Random from a list
	* Status Tracker between turns
	* Items found in shops, sorted by price
* [Settings](#settings)
	* What each setting does
	* How to add items to random encounters
		
-----------------------------------------------------------------

<h3>Slash Commands</h3>

-----------------------------------------------------------------

Slash commands are a "new" feature by discord, which allow bots to have easily accessible commands in the servers they are in. Typing a '/' into the chatbox will let you see all available commands in a server, and each command will display the options you can give.
	
For example, `/encounter` not only has the `pokemon` option, but additonally has `number` (has many to generate), `rank` (what rank should the pokemon be), and `smart_stats` (generate with improved stat distribution).
`/encounter pokemon:Pikachu, Squirtle number:2 rank:Amateur` is equivalent to `%encounter 2 amateur Pikachu, Squirtle`.
It may look longer, but the command and options conveniently autofill with tab (or you can click on the menu that pops up).
	
Nearly all of PokeRole Helper's commands have been converted to Slash Commands. If you have suggestions for more commands or buttons for existing commands, please let me know with `/feedback`!

-----------------------------------------------------------------

<h3>Quick Reference</h3>

-----------------------------------------------------------------

- **Pokemon Stats** --> `%stats <pokemon>`

example: `%stats squirtle`

This command tells you the type, base/max stats, abilities, and suggested rank of the \<pokemon>.

- **What Moves a Pokemon can learn** --> `%pokelearns <pokemon>`

example: `%pokelearns squirtle`

This command tells you what moves a pokemon can learn, organized by rank.

- **Finding Move Definitions** --> `%move <move>`
 
example: `%move tackle`
 
This command tells you everything relating to the move.
 
- **Items and what they do** --> `%item`

example: `%item <item>` OR `%item`

This command gives you the item's description, and any properties it has.
You may use %item by itself for a list of catagories.

- **Ability Descriptions** --> `%ability <ability>`

example: `%ability run away`

This command gives you the description of the ability.

- **Habitats** --> `%habitat`

example: `%habitat` OR `%habitat tide pools`

This command is similar to `%item`, using `%habitat` by iself lists catagories,
and using `%habitat <habitat>` lists that habitat's suggested inhabitants.
(All habitats and the pokemon in them were originally created by theworldofpokemon.com)

[Check out how to filter pokemon from a habitat into a list!](#filtering-by-habitat)

-----------------------------------------------------------------

<h3>Lists</h3>

-----------------------------------------------------------------
Quick note: `%lists` will display every available list.
- How do they work?

Lists are a collection of either pokemon or items. They are very convenient in situations where you want a random pokemon from a group. Item lists work slightly differently.

Pokemon lists are the most common, so I'll go over them first.

- **Creating, Modifying, and Deleting lists** --> `%list <listname> (add/show/del) (poke1, poke2, etc)`
	- **Creating Lists**:
	
		Lets say you have a set group of pokemon for a grassland/field area. (In this example those pokemon will be Ponyta, Furret, Sentret, and Watchog.)
		
		Keep in mind everyone can see your list's name, so **try to make the name unique but not too personal**. (If you see a list that suites your needs feel free to use it - but if you're able to modify it please @shadeslayer in the pokerole discord. That's not supposed to happen)
		
		Since my username is ShadeSlayer I'll use shade_ to prefix my lists. This is just personal preference, any name will work.
		
		To create my grassland list I'll use **%list shade_grassland add Ponyta, Furret, Sentret, Watchog**
		
		Ta-da! You can try `%list shade_grassland` to check that it worked.
		
	- **Modifying Lists**:
		
		This is very similar to creating a list.
		
		Lets add Gligar to the previous example of shade_grassland:
		
		`%list shade_grassland add Gligar`
		
		And that's it!
		
	- **Deleting Lists:**
		
		To delete a list you have 3 options (using shade_grassland as the example):
		1. %list shade_grassland del
		
			This option deletes the list itself. Use with caution.
			
		2. %list shade_grassland del gligar, ponyta, etc
			
			This option allows you to delete specific pokemon from the list.
			
		3. %listsub shade_grassland shade_field
		
			This option removes the pokemon in *shade_grassland* that are in common with *shade_field*.
			
			More in-depth examples [here](#listsub)

- **Quickly adding lots of similar pokemon**
	- **The filter command and why it's so useful** --> `%filter listname rank type type2 includeLowerRanks generation`
		
		This command may look complicated, but it's a lot simpler to use than it appears.
		(Keep in mind that %filter only appends pokemon - it's possible to accidentally create duplicate pokemon)
		
		First off: the arguments. What do they mean?
		
		1. **`listname`**
		
		This is the list that you want the pokemon to go in. This command will create the list if necessary.
		
		2. **`rank`**
		
		The suggested rank of pokemon you want in the list. 'Beginner', for example, will return the pokemon like bulbasaur, pidgey, swinub, etc.
		
		3. **`type`**
		
		The pokemon type you want (Grass/Fire/etc). This parameter is currently required bc there are... a lot of pokemon.
		
		4. **`type2`**
		
		The secondary type you want. You can put 'any' to accept all secondary typings, or 'none' to restrict to only single-type pokemon.
		
		If you have a specific area in mind, it might be useful to combine 'grass poison' and 'grass ground', or subtract(#listsub) 'grass none' from a list made with 'grass poison'.
		
		5. **`includeLowerRanks`**
		
		If rank is 'Amateur', include 'Starter' and 'Beginner'?
		6. **`generation`**
		
		Restrict the search to a generation? (1 = Kanto, 2 = Johto, ..., 8 = Galar)
		
		Default is all generations/no restriction.
		
	- **<h4 id='listsub'>Listsub and why it's useful</h4>** --> `%listsub list1 list2`
		
		Want to subtract two lists? This command is the one you want.
		
		Let's say you have a list for a grassland. shade_grassland has every Beginner-rank grass-type.
		You also have a list for a forest. shade_forest has Bellsprout, Pidgey, Bulbasaur, Houndour.
		
		In this case I want to remove the pokemon in shade_grassland that are also in shade_forest (Bellsprout, Bulbasaur).
		
		`%listsub shade_grassland shade_forest` will remove the pokemon from shade_grassland, and will not affect the list shade_forest.
		
- **<h4 id='filtering-by-habitat'>Filtering Pokemon into a list from a habitat</h4>** --> `%filterhabitat list [rank] [includeLowerRanks] habitat`

	(`%fh list habitat` for the short version)

	Want to add a specific biome to a list? Combine different habitats together? This command lets you do just that!
	
	To get started, you'll need to have a habitat in mind. Finding one is easy, simply type `%habitat`, choose a biome from the list, and type `%habitat <biome>` i.e. `%habitat ocean biomes`.
	
	In this example I'll use the Tide Pool biome from the Ocean Biomes option.
	
	I'll add the pokemon ranked Amateur and lower to the list, since Pro is stronger than I want for this occasion.
	
	`%filterhabitat tide_bois amateur tide pools`
	
	And Voila! The pokemon are added!
	
	(Note: if I wanted *only* Amateur ranks, type `false` after the rank, like so:
	`%filterhabitat tide_bois amateur False tide pools`)
		
- <h5>Overview of item lists</h5>
		
	Item lists are new, so if they don't work correctly please @shadeslayer
		
	These lists use the same format as [weighted encounters](#weighted-encounters). That is, you need to specify the item rarity up front. (Note: To make all the items guaranteed and the same rarity, give them a 100% chance.)

	Format: `%list <listname> add xx% pokeball, greatball yy% oran berry, cheri berry zz% black belt, bright powder`

	For example: I want to make a list for what berries are found in a forest. I'll name the list 'shade_berries' (name doesn't matter, just make it somewhat unique). I want to make *oran berries, cheri berries, and chesto berries* common, *wacan berries, shuca berries, and tanga berries* uncommon, and *sitrus berries, lum berries, and jaboca berries* rare.
	
	I decide that there should be a 30% chance to draw nothing. I arbitrarily decide that common rarity should be a 40% chance, uncommon has 25% chance, and rare has a 5% chance.
	
	`%list shade_berries add 40% oran berry, cheri berry, chesto berry, 25% wacan berry, shuca berry, tanga berry, 5% sitrus berry, lum berry, jaboca berry` (note the missing 30%, this is to note the 30% chance for nothing)
	
	Now that I have an item list, I can either use [`%random`](#random-from-a-list) to draw a random item, or change the [`%settings`](#how-to-add-items-to-random-encounters) to make pokemon in `%encounter` start with it!
	
-----------------------------------------------------------------

<h3>Random Encounters</h3>

-----------------------------------------------------------------
- **How do they work?**

	`%encounter` was created to make random encounters more streamlined. It uses information from `%stats`, `%pokelearns`, and `%moves` to give a nice presentation of a randomly generated pokemon. (If you have feedback on how to make this output look nicer, please DM shadeslayer)
	
	Note that you can use a **shorter form for quick use** - `%e poke1, list1` for encounter, and `%we xx% poke1 yy% list1` for the weighted encounter
- **Encounters** --> `%encounter <number> <rank> <poke1, poke2, list>`
	
	This command creates *\<number>* of pokemon randomly selected from *\<poke1, poke2, list>* at the rank *\<rank>*.
	
	\<Number> can be 1-6 (to avoid spam)
	
	\<Rank> can be any basic rank ('Starter', 'Beginner', etc) or 'Base' - pokemon generated are at their suggested ranks. Useful if you have a Shinx and Luxray in the same list and want them to retain their suggested power levels.
	
	\<poke1, poke2, list> is any combination of pokemon and lists. `Chansey, Litwick, Pidgey`. `shade_forest`. `shade_forest, Chansey`. (Note: lists are case-sensitive)
- **I want a chance for rarer encounters to be mixed in** --> `%wEncounter <number> <rank> <separatePools> <pokemon>`

	This command allows you to have weighted/chance based encounters!
	
	\<number> and \<rank> are the exact same as in `%encounter`.
	\<separatePools> is the following: do you want pokemon from different rarities to be mixed together, or do you want them to be in 'packs'?
	If it's `True`: Pokemon are grouped by rarity. This allows you to separate encounters further, and makes something like `50% pidgey, spinarak, growlithe 50% pidgey, ponyta, ekans` easier to visualize.
	If it's `False`: Pokemon are drawn completely randomly from the given percents.
	
	Here's an example:
	
	My forest area is filled with wurmple and pidgey. Occasionally you'll find a diglett. Rarely you'll find a ponyta. I want the party to encounter a group of 3 pokemon. I want these pokemon to be from the same rarity (all ponyta, all diglett, or mixed pidgey and wurmple). These pokemon should all be at their suggested ranks.
	
	Aribitrarily, I decide that wurmple and pidgey have a 80% chance to be seen, diglett have a 17% chance to be seen, and ponyta have the remaining 3%.
	
	`%wEncounter 3 base True 80% wurmple, pidgey 17% diglett 3% ponyta`
	
	Generally though, separatePools `False` is recommended. Also note that you can mix pokemon and lists.

-----------------------------------------------------------------

<h3>Misc Commands</h3>

-----------------------------------------------------------------
* <h5>Random from a list</h5>

	`%random <list>` will return a plain random value from a list.

* <h5>Status Tracker between turns</h5>

	The `%tracker` command is essentially a simple note tracker, useful for keeping track of status effects between turns. You can add statuses (or anything), view them, or delete them by name or number.
	
	For example, lets say you have a pokemon battle between a poochyena and a flareon. The first turn the flareon lands flamethrower and applies Burn 2. `%tracker add Burn 2` or `%tracker add Burn 2 (poochyena)` will add the status to the list. At the end of the turn (or whenever is necessary) `%tracker` will let you see all current status effects. This command is more useful in large battles or battles prone to rapidly changing status effects.
	
	`%tracker add <status>` will add <status> to the list.
	
	`%tracker` will send the full list of <statuses>, numbered by the order you added them.
	
	`%tracker del <status>` or `%tracker del <number>` will delete the status by exact \<name> or \<number>.
	
	`%tracker change <number> <status>` will change the status in \<number> to \<status>. Useful for changing Burn 2 to Burn 1, etc.

* <h5>Items found in shops, sorted by price</h5>

	The `%shop` command displays items that can be found in shops, sorted by their prices.
	(The `%item` command will display items by category, and provides lookup for item descriptions and effects)
	
	For example, your player has 1000 poke to spend. `%shop 1000` will display all items up to and including 1000 poke.
	Alternatively, if your player is overflowing with cash and wants to only see the highest priced goods, `%shop 1000 True` or `%shop 1000 t` will show all items that cost 1000 poke or more.
	
	Any price value will work.

-----------------------------------------------------------------

<h3>Settings</h3>

-----------------------------------------------------------------
Basic format: `%settings <setting_name> <value>`
* <h5>What each setting does</h5>

	`ability_one_chance` - chance for pokemon to have their primary ability (default: 50)
	
	`ability_two_chance` - chance for pokemon to have their secondary ability (default: 49)
	
	`ability_hidden_chance` - chance for pokemon to have their hidden ability (default: 1)
	
	`shiny_chance` - chance for pokemon to be shiny (default: .00012 --> .012%)
	
	`pre_evo_moves` - If a pokemon has previous evolutions, should it inherit moves from a previous evolution? You can also choose to have it inherit from the previous rank. (Yes/No/Lower)
	
	`code_block` - Display `%encounter` text in a `code block like this`? (default: False)
	
	`show_move_description` - Show the full move description in `%encounter`? (default: True)
	
	`encounter_item` - What item list should `%encounter` check for items?
	
	`display_list` - Display lists grouped by Rank or by Odds? (default: Rank)
	
	`random_rolls` - Should encounters come with 4 random rolls on all moves for accuracy and damage? (default: False)
* <h5>How to add items to random encounters</h5>

	Once you have an [item list](#overview-of-item-lists), simply type `%settings encounter_item <listname>` where \<listname> is the name of an itemlist.
	
	You can type `%settings encounter_item` to remove the list.
