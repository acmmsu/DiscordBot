import discord

from encrypt import encrypt_basic, decrypt_basic
from rsa-functions import gen_keys, encrypt_decrypt

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
    async def on_message(message: discord.Message):
        if message.author == client.user:
            return

        # Get message command 
        if message.content.startswith('/hello'):
            await message.channel.send('Hello!')
        
        if message.content.startswith('/encrypt'):
            await message.channel.send(encrypt_basic(message.content[8:]))
        
        if message.content.startswith('/decrypt'):
            await message.channel.send(decrypt_basic(message.content[8:]))
            
        if message.content.startswith('/rsa-generate-keys'):
            await message.channel.send(gen_keys())
            
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