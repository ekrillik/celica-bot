import discord

class EmbedClass:
    def choose_build(self, build_array, choice):
        for i in build_array:
            if choice == i['set_name']:
                build = i
        return build

    def choose_cub_skills(self, active, passive, choice):
        if(choice == "active"):
            return active
        else:
            return passive

    def create_build_embed(self, build, choice, colour=0xffffff, chibi_avatar=""): 
        name = build['unit_name']
        frame = build['frame_name']
        thumbnail_url = build['thumbnail_url']
        builds = build['builds']

        selection = self.choose_build(builds, choice)
        description = "\n".join(selection['description'])
        memories = "\n".join(selection['memories'])
        memory_resonance = "\n".join(selection['memory_resonance'])

        embed = discord.Embed(
            title=f"{name}: {frame}",
            description=f"{selection['set_type'] + " " + "Set"}"
        )
        embed.add_field(name="Usage", value=selection['set_type'])
        embed.add_field(name="Game Modes", value=selection['game_modes'])
        embed.add_field(
            name="Description", 
            value=description,
            inline=False
        )
        embed.add_field(
            name="Memories", 
            value=memories,
            inline=False
        )
        embed.add_field(
            name="Memory Resonances", 
            value=memory_resonance,
            inline=False
        )
        embed.add_field(
            name="Harmony Recommendation", 
            value=f"{selection['harmony_rec']}",
            inline=False
        )
        embed.set_thumbnail(url=thumbnail_url)
        return embed

    def create_memory_embed(self, memory):
        
        # print(memory['rarity'])
        stars = memory['rarity']
        
        match stars:
            case 2:
                stars = "★★"
                colour = 0x75d17d
            case 3:
                stars = "★★★"
                colour = 0x3c76bd
            case 4:
                stars = "★★★★"
                colour = 0xd667f0
            case 5:
                stars = "★★★★★"
                colour = 0xf79514
            case 6:
                stars = "★★★★★★"
                colour = 0xfc5f21

        embed = discord.Embed(
            title=f"{memory['name']} {stars}",
            description="",
            color=discord.Color(colour)
        )
        embed.add_field(
            name=f"2pc Set Bonus",
            value=f"{memory['2pc']}",
            inline=False
        )
        if (memory['4pc'] == ""):
            a = ""
        else:
            embed.add_field(
                name=f"4pc Set Bonus",
                value=f"{memory['4pc']}",
                inline=False
            )

        if ('6pc' in memory):
            embed.add_field(
                name=f"6pc Set Bonus",
                value=f"{memory['6pc']}",
                inline=False
            )
        else:
            a = ""
        
        embed.add_field(
            name="ATK",
            value=f"{memory['atk']}",
        )
        embed.add_field(
            name="CRIT",
            value=f"{memory['crit']}",
        ),
        embed.add_field(
            name="DEF",
            value=f"{memory['def']}",
        )
        embed.add_field(
            name="HP",
            value=f"{memory['hp']}",
        )
        embed.set_thumbnail(url=memory['thumbnail'])
        return embed

    def create_weapon_embed(self, weapon, chibi_avatar=""):
        effect = weapon['effect']
        stars = weapon['rarity']
        
        match stars:
            case 2:
                stars = "★★"
                colour = 0x75d17d
            case 3:
                stars = "★★★"
                colour = 0x3c76bd
            case 4:
                stars = "★★★★"
                colour = 0xd667f0
            case 5:
                stars = "★★★★★"
                colour = 0xf79514
            case 6:
                stars = "★★★★★★"
                colour = 0xfc5f21

        embed = discord.Embed(
            title=f"{weapon['name']} {stars}",
            description=f"{weapon['weapon_type']}",
            color=discord.Color(colour)
        )
        embed.add_field(
            name=f"{effect['effect_name']}",
            value=f"{effect['effect_desc']}",
            inline=False
        ),
        embed.add_field(
            name="ATK",
            value=f"{weapon['atk']}",
        ),
        embed.add_field(
            name="CRIT",
            value=f"{weapon['crit']}",
        ),
        embed.set_thumbnail(url=weapon['thumbnail'])
        return embed

    def create_cub_embed(self, cub, choice, colour=0xffffff, chibi_avatar=""):
        
        active_skills = cub['active_skills']
        passive_skills = cub['passive_skills']

        if(choice == "active"):
            name = "**Active Skills**"
        else:
            name = "**Passive Skills**"

        skills = self.choose_cub_skills(active_skills, passive_skills, choice)

        embed = discord.Embed(
            title=f"{cub['name']}",
            description=f"{cub['cub_type']}",
            # color=discord.colour(value=0xfc5f21)
        )
        embed.set_thumbnail(url=cub['thumbnail'])
        embed.add_field(
                name=name,
                value="",
                inline=False
            )
        for i in skills:
            embed.add_field(
                name=i['skill_name'], 
                value=i['skill_desc'],
                inline=False
            )
        return embed

    def skillsEmbed(self, skill, selection, cur_page = 0, colour=0xffffff, chibi_avatar=""):
        match selection:
            case "Basic Attack" | "Red Orb" | "Blue Orb" | "Yellow Orb" :
                embed = discord.Embed(title=f"Skill - {selection}", description=f"**{skill[cur_page]['name']}**")
                embed.add_field(
                    name="",
                    value=f"**Trigger - {skill[cur_page]['button_press']}**",
                    inline=False
                )
                description = skill[cur_page]['description']
                embed.add_field(
                    name="",
                    value=f"{description['desc']}",
                    inline=False
                )
                results = description['result']
                if len(results) > 0:
                    for result in results:
                        embed.add_field(
                            name="",
                            value=f"{result}",
                            inline=False
                        )
                embed.set_footer(text=f"{cur_page + 1}/{len(skill)}")
            case "Core Passive":
                embed = discord.Embed(title=f"Skill - {selection}", description=f"**{skill['name']} - {skill['skills'][cur_page]['name']}**")
                embed.add_field(
                    name="",
                    value=f"**Trigger - {skill['skills'][cur_page]['button_press']}**",
                    inline=False
                )
                descriptions = skill['skills'][cur_page]['description']
                if len(descriptions) > 0:
                    for description in descriptions:
                        embed.add_field(
                            name="",
                            value=f"{description}",
                            inline=False
                        )
                results = skill['skills'][cur_page]['result']
                if len(results) > 0:
                    for result in results:
                        embed.add_field(
                            name="",
                            value=f"{result}",
                            inline=False
                        )
                embed.set_footer(text=f"{cur_page + 1}/{len(skill['skills'])}")
            case "Signature/Ultimate":
                embed = discord.Embed(title=f"Skill - {selection}", description=f"**{skill['name']} - {skill['skills'][cur_page]['name']}**")
                embed.add_field(
                    name="",
                    value=f"**Trigger - {skill['skills'][cur_page]['button_press']}**",
                    inline=False
                )
                description = skill['skills'][cur_page]['description']
                embed.add_field(
                    name="",
                    value=f"{description['desc']}",
                    inline=False
                )
                results = description['result']
                if len(results) > 0:
                    for result in results:
                        embed.add_field(
                            name="",
                            value=f"{result}",
                            inline=False
                        )
                embed.set_footer(text=f"{cur_page + 1}/{len(skill['skills'])}")
            case "Leader Passive" | "Class Passive":
                embed = discord.Embed(title=f"Skill - {selection}", description=f"**{skill['name']}**")
                description = skill['description']
                embed.add_field(
                    name="",
                    value=f"{description['desc']}",
                    inline=False
                )
            case "QTE":
                embed = discord.Embed(title=f"Skill - {selection}", description=f"**{skill['name']}**")
                embed.add_field(
                    name="",
                    value=f"{skill['description']}",
                    inline=False
                )
                for result in skill['results']:
                    embed.add_field(
                        name="",
                        value=f"{result}",
                        inline=False
                    )
            case "SS" | "SSS" | "S+":
                embed = discord.Embed(title=f"Skill - {selection}", description=f"**{skill['name']}**")
                levels = skill['levels']
                for level in levels:
                    embed.add_field(
                        name=f"{level['rank']}",
                        value=f"{level['desc']}",
                        inline=False
                    )
            case "Leap":
                embed = discord.Embed(title=f"Skill - {selection}", description=f"**{skill[cur_page]['name']}**")
                embed.add_field(
                    name="",
                    value=f"{skill[cur_page]['description']}",
                    inline=False
                )
                embed.add_field(
                    name="",
                    value=f"{skill[cur_page]['level9']}",
                    inline=False
                )
                level18 = skill[cur_page]['level18']
                embed.add_field(
                    name="",
                    value=f"{skill[cur_page]['level18'][0]}",
                    inline=False
                )
                for idx, result in enumerate(level18):
                    if idx == 0:
                        continue
                    embed.add_field(
                        name="",
                        value=f"{result}",
                        inline=False
                    )
        return embed

    def create_cublist_embed(self, cubs):
        embed = discord.Embed(
            title=f"List of CUBs",
            description="",
            color=discord.Color(0x3d6e41)
        )
        for cub in cubs:
            if(cub['sig_character'] != "N/A"):
                embed.add_field(
                    name="",
                    value=f"`{cub['base_rank']}・{cub['name']}  ({cub['sig_character']})`",
                    inline=False
                )
            else:
                embed.add_field(
                    name="",
                    value=f"`{cub['base_rank']}・{cub['name']}`",
                    inline=False
                )
        return embed

    def create_list_embed(self, name, items, curpage, maxlistcount):

        embed = discord.Embed(
            title=f"List of {name}",
            description="",
            color=discord.Color(0xb8f2e4)
        )
        for i in items:
            embed.add_field(
                name = "",
                value = i.replace('#', '★'),
                inline=False
            )
        embed.set_footer(text=f"Page {curpage}/{maxlistcount}")
        return embed

    def create_about_embed(self):
        embed = discord.Embed(
            title=f"About this Bot",
            description=f"Hi Commandant! I'm Celica, your guide to Babylonia and the world of Punishing: Gray Raven."
        )
        embed.add_field(
            name="Disclaimer",
            value=f"This bot is a community project initiated by Ek(#ek3970). It is not in any way affiliated with Kuro Games or their staff. If you would like to ask questions about the bot, please send me a DM or ping me on the Punishing: Gray Raven Official Discord. (Also Scire is not best girl. I was just held at gunpoint to give her that nickname.)",
            inline=False
        )
        return embed
    
    def credits_embed(self, credits, cur_page, max_len):
        embed = discord.Embed(
            title=f"Credits",
            description="Thanks to all of you who have helped out in the making of this bot. Without you it would have taken me much longer to get this off the ground."
        )
        embed.add_field(name=credits['title'], value=credits['description'], inline=False)

        if 'people' in credits:
            for name in credits['people']:
                embed.add_field(name="", value=f"{name}", inline=False)
        embed.set_footer(text=f"Page {cur_page + 1}/{max_len} ")
        return embed