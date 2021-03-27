# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 17:46:59 2021

@author: DaddyDog
"""
import logging
from sheep_grammar import sheep_grammar


def main():
    logging.basicConfig(filename='log_sheep_noises.txt', level=logging.DEBUG)

    for philosophical_conversation in range(0,20):
        print(sheep_grammar("Winnie").talk_to_me('says'))
        print(sheep_grammar("Flossy").talk_to_me('replies'))
        print(' ')


if __name__ == '__main__':
    main()