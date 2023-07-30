from time import sleep

import keyboard
import datetime

WHITE_TURN = True
WHITE_TIME = 0
WHITE_INCREMENT = 0
BLACK_TIME = 0
BLACK_INCREMENT = 0


def callback(event: keyboard.KeyboardEvent):
    global WHITE_TURN, WHITE_TIME, BLACK_TIME

    if event.event_type == "up":
        if event.name == "f10":
            if WHITE_TURN:
                BLACK_TIME += BLACK_INCREMENT
            else:
                WHITE_TIME += WHITE_INCREMENT
            WHITE_TURN = not WHITE_TURN


def parse_time(raw_time):
    if "+" in raw_time:
        split_time = raw_time.split("+")
        return int(split_time[0].strip()) * 60, int(split_time[1].strip())
    else:
        return int(raw_time.strip()) * 60, 0


def main():
    global WHITE_TIME
    global WHITE_INCREMENT
    global BLACK_TIME
    global BLACK_INCREMENT
    white_time = input(
        "Enter the time control for White (in minutes, with optional increment +X): "
    )

    WHITE_TIME, WHITE_INCREMENT = parse_time(white_time)

    black_time = input(
        "Enter the time control for Black (in minutes, with optional increment +X): "
    )

    BLACK_TIME, BLACK_INCREMENT = parse_time(black_time)

    input(
        "Press any key to start the clock. When a player is done their turn, press F10 to stop their clock and start their opponent's clock. "
    )
    keyboard.hook(callback)

    while WHITE_TIME > 0 and BLACK_TIME > 0:
        print(
            f"White: {str(datetime.timedelta(seconds=WHITE_TIME))}\tBlack: {str(datetime.timedelta(seconds=BLACK_TIME))}",
            end="",
        )
        if WHITE_TURN:
            WHITE_TIME -= 1
        else:
            BLACK_TIME -= 1

        sleep(1)
        print("\r", end="")

    if WHITE_TIME <= 0:
        print("White flagged, Black wins!")
    else:
        print("Black flagged, White wins!")


if __name__ == "__main__":
    main()
