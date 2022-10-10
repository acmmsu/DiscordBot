import discord

from tokens import TOKEN

def main():

    intents = discord.Intents.default()
    
    # Enable needed intents
    intents.message_content = True
    intents.messages = True

    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'We have logged in as {client.user}')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        if message.content.startswith('$hello'):
            await message.channel.send('Hello!')
            
    @client.event
    async def on_message_edit(before: discord.Message, after: discord.Message):
        """Output the edited message of a user

        Args:
            before (str): The message before it was edited 
            after (str): The message after it was edited
        """
        await before.channel.send(f'User {after.author} edited this message from \"{before.content}\"')
        

    client.run(TOKEN)


if __name__ == '__main__':
    main()