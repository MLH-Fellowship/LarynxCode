import subprocess,sys,click
from subprocess import Popen,CREATE_NEW_CONSOLE
from selenium import webdriver
import six
from pyfiglet import figlet_format
from click_help_colors import HelpColorsGroup, HelpColorsCommand

# Coloring libraries
# Try colorama
try:
    import colorama
    colorama.init()
except ImportError:
    colorama = None
# Try termcolor
try:
    from termcolor import colored
except ImportError:
    colored = None

# Help section coloring and Grouping
@click.group(
    cls=HelpColorsGroup,
    help_headers_color='yellow',
    help_options_color='cyan'
)
def cli_group():
    pass

# Styling
def log(string, color, font="slant", figlet=False):
    if colored:
        if not figlet:
            six.print_(colored(string, color))
        else:
            six.print_(colored(figlet_format(
                string, font=font), color))
    else:
        six.print_(string)

@cli_group.command()
@click.option('--voice', default = False, help = "Use --voice if you want to code using your voice.")
@click.option('--start', help = "To start voice coding, execute this command in the console : python -m dragonfly load --engine sapi5inproc _*.py --no-recobs-messages. Wait till the program says beginning loop, then clearly speak out your commands")
def enable_voice_coding(voice,start):
    """Enables voice coding."""
    log("Larynx Code", color="blue", figlet=True)
    log("Welcome to Larynx Code. We enable voice coding in your eitor and general navigations.", "green")
    log("A new window will open up shortly, run the command : python -m dragonfly load --engine sapi5inproc _*.py --no-recobs-messages, to enable voice coding", "yellow")
    log("LarynxCode --> developed by Balaka Biswas and Leshna Balara, with Click.", "cyan")
    encoding = 'latin1'
    p = subprocess.Popen(
        ['start', 'cmd', '/k', 'cd /caster'],
        creationflags = CREATE_NEW_CONSOLE,
        shell = True,
        stdin = subprocess.PIPE,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE
    )

@cli_group.command()
@click.option('--casterhelp', default = False, help = 'Call this option if you need to refer to the Caster Guide web app')
@click.option("--google", help = "Chooses default browser as Google Chrome")
def chelp(casterhelp,google):
    """Command for launching user guide."""
    log("Larynx Code", color="blue", figlet=True)
    log("Welcome to Larynx Code. We enable voice coding in your eitor and general navigations.", "green")
    log("A new window will open up shortly, directing you to a simple guide. Detailed guides will get downloaded automatically.", "yellow")
    log("Developed by Balaka Biswas. Hosted on Heroku.", "cyan")
    driver = webdriver.Chrome("C:\\chromedriver.exe")
    driver.get("https://larynxcode.herokuapp.com/")
    while True:
        pass
    driver.close()

'''cli_group.add_command(enable_voice_coding)
cli_group.add_command(caster_help)'''

if __name__ == "__main__":
    cli_group()       
