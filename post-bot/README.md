# ManoBot: Discord Embed Bot

This Discord bot allows users with a specific role to post messages as embeds to predefined channels or any specified channel using different commands. The bot includes commands for posting job and service announcements, as well as a flexible command for posting to any channel.

## Features

- Post job announcements to a predefined channel.
- Post service offerings to a predefined channel.
- Post embed messages to any specified channel with a custom title and message.

## Commands

### /postjob

Posts a job announcement to the predefined job channel.

**Usage:**
```
/postjob <message>
```

**Example:**
```
/postjob "We are hiring a new software developer!"
```

### /postservices

Posts a service offering to the predefined service channel.

**Usage:**
```
/postservices <message>
```

**Example:**
```
/postservices "Offering web development services at competitive prices."
```

### /post

Posts an embed message to any specified channel with a custom title and message.

**Usage:**
```
/post #channelname <Title> <Message-content>
```

**Example:**
```
/post #channelname "Title" "Message content goes here."
```

## Setup

### Prerequisites

- Python 3.6+
- Discord account and server where the bot will be used

### Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/Susmita-Dey/post-bot.git
   cd post-bot
   ```

2. **Create a virtual environment and activate it:**
   ```sh
   python -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Create a `.env` file and add your environment variables:**
   ```sh
   DISCORD_BOT_TOKEN=your_bot_token
   ALLOWED_ROLE_ID=role_id
   JOB_CHANNEL_ID=job_channel_id
   SERVICE_CHANNEL_ID=service_channel_id
   ```

### Running the Bot

1. **Start the bot:**
   ```sh
   python bot.py
   ```

### Deploying the bot
Create an account on Render. Install Render on your git repository and hit deploy

## Permissions

Ensure the bot has the following permissions in your Discord server:

- Send Messages
- Embed Links
- Manage Roles (if you want the bot to verify roles)

## Troubleshooting

- **Bot not responding to commands:**
  - Check that the bot has the required permissions.
  - Verify that the environment variables are correctly set.
  - Ensure the bot is running and connected to the Discord server.

- **Environment variable errors:**
  - Ensure all necessary environment variables are set in the `.env` file.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
