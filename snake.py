import curses
from random import randint


def main(stdscr):
    curses.curs_set(0)
    sh, sw = stdscr.getmaxyx()
    w = curses.newwin(sh, sw, 0, 0)
    w.keypad(True)
    w.timeout(100)

    snk_x = sw // 4
    snk_y = sh // 2
    snake = [
        [snk_y, snk_x],
        [snk_y, snk_x - 1],
        [snk_y, snk_x - 2],
    ]

    food = [sh // 2, sw // 2]
    w.addch(food[0], food[1], curses.ACS_PI)

    key = curses.KEY_RIGHT

    while True:
        next_key = w.getch()
        key = key if next_key == -1 else next_key

        if key == curses.KEY_DOWN:
            new_head = [snake[0][0] + 1, snake[0][1]]
        elif key == curses.KEY_UP:
            new_head = [snake[0][0] - 1, snake[0][1]]
        elif key == curses.KEY_LEFT:
            new_head = [snake[0][0], snake[0][1] - 1]
        elif key == curses.KEY_RIGHT:
            new_head = [snake[0][0], snake[0][1] + 1]
        else:
            continue

        if (
            new_head[0] in [0, sh]
            or new_head[1] in [0, sw]
            or new_head in snake
        ):
            msg = "Game Over!"
            w.addstr(sh // 2, sw // 2 - len(msg) // 2, msg)
            w.refresh()
            curses.napms(2000)
            break

        snake.insert(0, new_head)

        if new_head == food:
            food = None
            while food is None:
                nf = [randint(1, sh - 2), randint(1, sw - 2)]
                if nf not in snake:
                    food = nf
            w.addch(food[0], food[1], curses.ACS_PI)
        else:
            tail = snake.pop()
            w.addch(tail[0], tail[1], " ")

        w.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)


if __name__ == "__main__":
    curses.wrapper(main)
