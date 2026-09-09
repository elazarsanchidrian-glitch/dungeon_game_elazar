# Text-Based Dungeon Crawler

A text-based dungeon crawler inspired by the dungeons of **The Elder Scrolls II: Daggerfall** and **EverQuest**.

The game is built around exploration, random encounters, combat, character progression, NPC interaction, loot, and the search for a way out of a dangerous underground dungeon.

## How the Game Plays Out

You begin your adventure at the **Dungeon Entrance**.

From there, the dungeon expands as you explore it. Rooms are generated as you move, and each room can contain different scenery, sounds, items, monsters, and occasionally NPCs.

Your overall goal is simple:

> **Explore the dungeon, survive its dangers, discover what lies within it, and find the exit.**

The dungeon is deliberately unpredictable, so each new run can play out differently.

---

## 1. Create Your Character

Before entering the dungeon, you create your character.

You choose:

- **Name**
- **Gender**
- **Race**
- **Class**

### Races

Each race provides a different passive ability and starting-stat bonus:

- **Human** — Adaptable
- **Elf** — Arcane Affinity
- **Dwarf** — Tough
- **Orc** — Brutal
- **Halfling** — Lucky

### Classes

You can choose between:

- **Warrior** — Strong melee fighter
- **Mage** — Focuses on magicka and magical abilities
- **Rogue** — Fast fighter with strong stamina and Backstab

Your class also determines your starting equipment and special ability.

---

## 2. Enter the Dungeon

After character creation, you begin at the safe **Dungeon Entrance**.

The dungeon uses coordinate-based movement:

- `north`
- `south`
- `east`
- `west`

The dungeon is effectively open-ended, and new rooms are generated as you move into unexplored areas.

The game shows your current dungeon coordinates, allowing you to keep track of where you have traveled.

---

## 3. Explore Each Room

Use:

```text
look
```

to examine your surroundings.

Exploring a room can reveal:

- The room's description
- Atmospheric sights
- Sounds coming from the darkness
- Items
- Monsters
- NPCs

The dungeon contains many different types of rooms, including:

- Dark Hallways
- Caverns
- Crypts
- Abandoned Armories
- Forgotten Libraries
- Underground Shrines
- Collapsed Chambers
- Underground Lakes
- Bloodstained Chambers
- Ancient Prisons
- Mysterious Chambers
- Torchlit Corridors

Because rooms are randomly generated, exploration is an important part of every playthrough.

---

## 4. Find and Use Items

Items can appear throughout the dungeon or be dropped by defeated monsters.

You can:

```text
take <item>
use <item>
equip <item>
inspect <item>
```

Possible finds include weapons, armor, shields, potions, gold, rings, coins, and other pieces of loot.

Equipment affects your combat effectiveness and defense, while consumables can restore health or magicka.

Some monsters can also drop special loot based on their type.

---

## 5. Encounter Monsters

Dangerous creatures can appear when you enter unexplored rooms.

Possible enemies include:

- Goblins
- Skeletons
- Bandits
- Trolls
- Orcs
- Demons
- Spirits
- Vampires

Not every room contains an enemy, so the dungeon alternates between quiet exploration and sudden danger.

When a monster appears, combat begins.

---

## 6. Combat

During combat, you can choose between several actions:

1. **Attack**
2. **Dodge**
3. **Escape**
4. **Dialogue**
5. **Ability**
6. **Use Item**

### Attack

Your normal attack deals damage based on your character class, passive, and equipped weapon.

If the attack misses, the monster gets an opportunity to attack you.

### Dodge

You have a chance to dodge an incoming attack.

A successful dodge avoids the damage. If the dodge fails, the monster hits you.

### Escape

You can attempt to flee from a monster.

A successful escape removes the monster from the current encounter, while a failed escape allows the monster to attack.

### Dialogue

Some monsters can be talked to.

Dialogue uses a speech check with a percentage chance of success. If successful, the monster leaves you alone. If it fails, the monster attacks.

This gives you another way to survive an encounter without necessarily killing everything you meet.

### Abilities

Each class has its own special ability:

- **Warrior — Power Strike**
- **Mage — Fireball**
- **Rogue — Backstab**

Abilities consume stamina or magicka and are stronger than a normal attack.

The Rogue's Backstab also has a chance to deal critical damage.

---

## 7. Progress Through Experience and Loot

Defeating monsters rewards you with **XP**.

When you gain enough XP, you level up.

Leveling up increases your maximum health and also improves your stamina and magicka.

Enemies can also drop loot after being defeated.

This creates a natural progression loop:

```text
Explore
   ↓
Encounter
   ↓
Fight / Dodge / Escape / Talk
   ↓
Gain XP and Loot
   ↓
Improve Your Character
   ↓
Explore Deeper
```

The further you explore, the more important it becomes to manage your health, equipment, inventory, and resources.

---

## 8. Meet NPCs

Occasionally, you may discover a neutral NPC while exploring.

Two types of NPCs can appear:

### Lost Traveler

The Lost Traveler is a weary adventurer who has become trapped in the dungeon.

Talking to travelers can add information and atmosphere to the adventure, giving the dungeon a sense that other people have attempted to survive it before you.

### Wandering Merchant

The Wandering Merchant carries supplies that can help you continue your journey.

You can talk to the merchant and purchase useful equipment and consumables with your gold.

NPC encounters are intentionally uncommon, so finding another person in the darkness can feel like an important discovery.

---

## 9. Discover the Dungeon's Secrets

The dungeon is not simply a straight path from the entrance to the exit.

As you explore, pay attention to what you see and hear.

The descriptions of rooms, monster encounters, unusual locations, and NPC conversations help build the feeling that the dungeon is an old and dangerous place with secrets hidden inside it.

NPCs and encounters can provide context about the dungeon and the dangers within it.

The player is encouraged to explore rather than simply move in one direction.

---

## 10. The Forbidden Boss Chamber

There is a chance that a newly discovered room will become a:

**Forbidden Boss Chamber**

This is an extremely rare special room.

The chamber is described as unnaturally still, with ancient symbols covering the walls and a huge sealed chamber dominating the room.

The boss encounter is even rarer.

If the boss appears, you face the:

# Dungeon Warden

The Dungeon Warden is a powerful guardian with:

- **300 HP**
- **35 attack damage**
- Very low dialogue success chance
- Unique combat dialogue
- Unique attack reactions
- Unique death dialogue

The Warden is far more dangerous than the ordinary creatures encountered throughout the dungeon.

If you discover this chamber, be prepared for a serious fight.

---

## 11. Defeat the Dungeon Warden

The Dungeon Warden can be fought using the same combat system as other monsters.

You can:

- Attack
- Dodge
- Escape
- Attempt dialogue
- Use your class ability
- Use items

However, the Warden has a very low chance of being convinced through dialogue, making combat the more reliable way to defeat it.

When the Warden dies, you receive XP and the boss can generate special loot.

There is also an exceptionally rare chance for the Warden to drop an:

**Ancient Dungeon Key**

The key is a rare item connected to the dungeon's deeper secrets.

---

## 12. Finding the Exit

The dungeon contains a **guaranteed normal exit**.

Its location is randomized when the dungeon begins and is placed several rooms away from the entrance.

The exit appears as a special room:

**Dungeon Exit**

When you discover it, you are told that a massive ancient doorway stands before you and that cold air is flowing from beyond it.

Reach the exit to complete the run.

```text
Dungeon Entrance
       ↓
     Explore
       ↓
  Find Clues / NPCs
       ↓
 Fight, Escape & Loot
       ↓
   Gain Experience
       ↓
Explore Further
       ↓
Discover the Dungeon's Secrets
       ↓
[Optional Rare Encounter]
 Forbidden Boss Chamber
       ↓
  Dungeon Warden
       ↓
 Defeat the Warden
       ↓
Possible Ancient Dungeon Key
       ↓
Continue Exploring
       ↓
   Dungeon Exit
       ↓
     VICTORY
```

The boss is an optional and exceptionally rare encounter; the normal exit exists independently and can be found through continued exploration.

---

## 13. Survive or Die

The dungeon is dangerous.

If your health reaches zero, the run ends in **Game Over**.

Managing your resources is therefore just as important as dealing damage.

Use potions when necessary, upgrade your equipment, choose when to fight, and know when to run.

Sometimes surviving an encounter is more valuable than winning it.

---

## 14. Useful Commands

### Movement

```text
north
south
east
west
```

### Exploration

```text
look
```

### Items

```text
take <item>
use <item>
equip <item>
inspect <item>
```

### Interaction

```text
talk
talk <npc>
```

### Combat

```text
attack
```

During combat, the game also accepts:

```text
attack
dodge
escape
dialogue
ability
use
```

### Character

```text
inventory
stats
objective
```

### Save / Load

```text
save
load
```

### Quit

```text
quit
```

---

## 15. The Core Gameplay Loop

The game is built around a simple roguelike-style exploration loop:

**Explore → Discover → Encounter → Survive → Progress → Explore Again**

There is no single fixed route through the dungeon.

You create your character, enter the darkness, explore unknown rooms, interact with whoever you find, fight or avoid monsters, collect equipment and treasure, gain experience, and eventually search for the way out.

The rare possibility of discovering the Forbidden Boss Chamber adds another layer of mystery to exploration.

**How deep can you go before the dungeon claims you?**

---

## Inspiration

This project is a text-based dungeon crawler inspired by classic RPG dungeon design, particularly the open-ended dungeon exploration of **The Elder Scrolls II: Daggerfall** and the atmosphere and encounters of **EverQuest**.

It was created as an end-of-semester Python project.
