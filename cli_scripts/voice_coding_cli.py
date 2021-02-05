import subprocess,sys,click

@click.command()
@click.option('--voice/--no-voice', default = False, help = "Use --voice if you want to code using your voice.")
@click.option('--speech', prompt = "What is your default Speech Recognition engine ? ", help = "Choose your default Speech Recognition engine")
def enable_voice_coding(voice,speech):
    """Welcome to LarynxCode. This is a simple CLI that enables you to allow voice programming on your editor."""
    if voice:
        if speech == 'wsr':
            cmds = [b'cd ..\..\..',b'c:',b'cd Caster',b'python -m dragonfly load --engine sapi5inproc _*.py --no-recobs-messages']
            encoding = 'latin1'
            p = subprocess.Popen(
                'cmd.exe',
                stdin = subprocess.PIPE,
                stdout = subprocess.PIPE,
                stderr = subprocess.PIPE
            )
            for cmd in cmds:
                p.stdin.write(cmd + b"\n")
            p.stdin.close()
            click.echo(p.stdout.read())
        else:
            click.echo("Not supported as of now")

if __name__ == "__main__":
    enable_voice_coding()
