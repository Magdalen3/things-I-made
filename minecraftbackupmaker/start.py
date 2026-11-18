
import string
import os, shutil
from pathlib import Path
from datetime import date
backup_dir = Path.cwd() / "backups"
backup_dir.mkdir(parents=True, exist_ok=True)

if Path("~/.var/app/org.prismlauncher.PrismLauncher/data/PrismLauncher").expanduser().is_dir():
    instance_dir = Path("~/.var/app/org.prismlauncher.PrismLauncher/data/PrismLauncher/instances").expanduser()

instances = {}
select = None
number = None
for number,select in enumerate(instance_dir.iterdir(), start=1):
    if select.is_dir():
        print(f"{number}: {select.name}")
        instances[number] = select

choice = int(input("choose the instance where your world is \n\n"))
instance_selected = instances[choice]

if Path(instance_selected / "minecraft" / "saves").expanduser().is_dir():
    world_select = Path(instance_selected / "minecraft" / "saves").expanduser()
    worlds = {}
    select = None
    number = None   
    for number,select in enumerate(world_select.iterdir(), start=1):
        if select.is_dir():
            print(f"{number}: {select.name}")
            worlds[number] = select
    choice = int(input("choose the world you want to backup \n\n"))
    world_selected = worlds[choice]
    areyousure = False
    while not areyousure:
        print(f"¿este es el mundo al que querés hacer backup? {world_selected.name}\n")
        world_check= input("y/n\n\n")
        if world_check == 'y': areyousure = True
        if world_check == 'n': exit("restart the script")
    today = date.today().strftime("%Y-%m-%d")
    shutil.make_archive(
        str(backup_dir / f"{world_selected.name}_{today}"),
        "zip",
        world_selected
    # pyrefly: ignore [parse-error]
    )
    