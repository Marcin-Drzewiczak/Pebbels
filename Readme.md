# Pebble Bot

Pebble Bot is a Discord bot that allows users to draw white and black pebbles from a virtual bag and roll dice with a specified number of sides.

## Features

- Draw white and black pebbles from a bag and display the results using emotes and numbers.
- Roll dice with a specified number of sides.

## Requirements

- Python 3.9 or newer
- `discord.py` library
- Docker and Docker Compose (optional)

## Installation

1. Clone the repository or download the source code.

    ```
    git clone https://github.com/yourusername/pebble-bot.git
    ```

2. Install the required dependencies.

    ```
    pip install -r requirements.txt
    ```

3. Set up a Discord bot and obtain its token. See the [official Discord documentation](https://discord.com/developers/docs/intro) for instructions on creating a bot and adding it to your server.

4. Update the `TOKEN` variable in the `bot.py` script with your bot's token.

    ```python
    TOKEN = 'your-bot-token'
    ```

## Running the Bot

You can run the bot using Python or Docker Compose.

### Using Python

Run the following command in your terminal:

    python bot.py


### Using Docker Compose

1. Set the `TOKEN` environment variable to your bot's token in the `docker-compose.yml` file.

    ```yaml
    environment:
      - TOKEN=your-bot-token
    ```

2. Build and run the Docker container with the following command:

    ```
    docker-compose up --build
    ```
   
    BOT_TOKEN=your-bot-token docker-compose up --build


## Usage

The bot supports the following commands:

- `!pebbles <white> <black> <draw>`: Draws a specified number of white and black pebbles from a bag.
- `!roll <dice>`: Rolls specified number of dice with specified number of sides (e.g., `2d6`).
- `!help`: Displays information on how to use the bot.

## Contributing

Please feel free to open an issue or submit a pull request with any improvements or suggestions.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
