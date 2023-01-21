# Purge-Bot
A python bot created using discord.py that can bulk-delete messages.

## How to run the bot
1. Upload all files into a replit
- The project was done on replit
- Hosting will become easier this way using UptimeRobot so the replit will always be running (more details on that below)
2. Go to Discord Developer Portal and obtain discord token
- Head to https://discord.com/developers/applications and create a new application
- Name your bot
- Then copy the application id
3. Create a .env file in Replit
- Once the file is created copy the application id into a environment variable
- The below code can be used to get the variable from the .env file named "TOKEN" (this name can be changed but also needs to be changed in the .env file)
`client.run(os.getenv('TOKEN'))`
4. Finally, use UptimeRobot to keep the replit running
- Once an account has been created, add a new monitor with a http(s) monitor type
- Add a name for the monitor and paste the link found in the top right pane of replit
> ![image](https://user-images.githubusercontent.com/75193860/131389713-9a699142-2c3a-4bfc-b127-576f65c32e97.png)
