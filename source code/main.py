from sentence_generator import random_sentence
from gui import CustomGui


def main():
    generator_func = random_sentence
    size_window = "1500x800"
    fb_color = "yellow"
    bg_color = "black"
    results_color = "red"

    my_gui = CustomGui(size_window, fb_color, bg_color, results_color, generator_func)
    my_gui.show()


if __name__ == '__main__':
    main()
