#!/usr/bin/env python3
import ipdb

from classes.many_to_many import Article
from classes.many_to_many import Author
from classes.many_to_many import Magazine

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

    author1 = Author("John Doe")
    magazine1 = Magazine("Tech Monthly", "Technology")
    article1 = author1.add_article(magazine1, "Understanding AI")

    magazine2 = Magazine("Health Weekly", "Health")
    author2 = Author("Jane Smith")
    article2 = author2.add_article(magazine2, "Nutrition for Wellness")

    magazine3 = Magazine("Travel Times", "Travel")
    author1.add_article(magazine3, "Exploring Mountains")

    author3 = Author("Alice Brown")
    article3 = author3.add_article(magazine1, "AI in Everyday Life")

    ipdb.set_trace()
