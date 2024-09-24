from turtle import *


def setup(*, drawing_speed: str = "fastest"):
    speed(drawing_speed)
    colormode(255)
    rt(270)


def compute_and_plot_tree(
    *,
    size: int = 90,
    level: int = 9,
    angle: int | float = 20,
    current_width: int = 12,
    shrinking_ratio: int | float = 0.85,
    stepcount: int = 1
) -> None:
    if level == 0:
        return
    width(current_width)
    pencolor(0, 255 // level, 0)
    fd(size)
    rt(angle)
    _ = "recursive call for right subtree"
    compute_and_plot_tree(
        size=shrinking_ratio * size,
        level=level - 1,
        angle=angle,
        current_width=(current_width // stepcount) + 1,
        shrinking_ratio=shrinking_ratio,
        stepcount=stepcount + 1,
    )
    pencolor(0, 255 // level, 0)
    lt(2 * angle)
    _ = "recursive call for left subtree"
    compute_and_plot_tree(
        size=shrinking_ratio * size,
        level=level - 1,
        angle=angle,
        current_width=(current_width // stepcount) + 1,
        shrinking_ratio=shrinking_ratio,
        stepcount=stepcount + 1,
    )
    pencolor(0, 255 // level, 0)
    rt(angle)
    fd(-size)


def main(*args, **kwargs) -> None:
    """Computing and plotting fractal tree via turltle graphics."""
    """https://en.wikipedia.org/wiki/Fractal_canopy"""
    setup()
    compute_and_plot_tree()


if __name__ == "__main__":
    main()
