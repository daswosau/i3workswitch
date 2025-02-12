import i3ipc
import argparse
import time

start_time = time.time()

i3 = i3ipc.Connection()

def cycle(num):

    match args.reverse:
        case 1:
            inc=-1
            final = 0
            num-=1
        case 0:
            inc=1
            final = 10
            num+=1

    match args.jump:
        case 1:
            req = 9
        case 0:
            req = int(i3.get_tree().find_focused().workspace().ipc_data["output"][-1])

    for ws in range(num,final,inc):
        if workspaces[f"{ws}"] == req or workspaces[f"{ws}"] == 9:
            match args.move:
                case 0:
                    i3.command(f"workspace number {ws}")
                case 1:
                    i3.command(f"move container to workspace number {ws}")            
            break

def getActiveWorkspace():
    return next(ws for ws in i3.get_workspaces() if ws.focused).num

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="daswosau's automatic workspace switcher.")
    parser.add_argument(
        "--move", 
        action="store_true", 
        help="Move focused window to a new workspace and set focus."
    )
    parser.add_argument(
        "--reverse", 
        action="store_true", 
        help="In reverse order."
    )
    parser.add_argument(
        "--jump", 
        action="store_true", 
        help="Jump to nearest unused.."
    )
    args = parser.parse_args()

    workspaces = {
        "0":9,
        "1":9,
        "2":9,
        "3":9,
        "4":9,
        "5":9,
        "6":9,
        "7":9,
        "8":9,
        "9":9,

    }

    for ws_num, output in [(ws.num, ws.output) for ws in i3.get_workspaces()]:
        workspaces[f"{ws_num}"] = int(output[-1])

    print(workspaces)

    cycle(getActiveWorkspace())



