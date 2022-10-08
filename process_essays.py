# import required module
import os
import re
import subprocess

images_dir = "./resources/image_exports"

essays = [
        ("letter_to_a_young_poet", 35, 38),
        ("old_music", 39, 43),
        ("letter_to_a_philistine", 44, 49),
        ("language", 50, 55),
        ("the_refuge", 56, 60),
        ("conscerning_the_soul", 61, 69),
        ("artists_and_psychoanalysis", 70, 75),
        ("from_my_diary", 76, 82),
        ("fanatsies", 83, 88),
        ("on_poems", 89, 93),
        ("the_brothers_karmazov", 94, 109),
        ("thoughts_on_the_idiot", 109, 116),
        ("books_on_trial", 117, 119),
        ("variations_on_a_theme", 120, 124),
        ("on_reading_books", 125, 131),
        ("a_poets_preface", 132, 136),
        ("about_jean_paul", 137, 146),
        ("exotic_art", 147, 149),
        ("on_holderlin", 150, 153),
        ("postscript_to_novalis", 154, 156),
        ("about_dostoevsky", 157, 159),
        ("our_ages_yearning", 160, 165),
        ("a_nights_work", 166, 170),
        ("a_virtuosos_concert", 171, 176),
        ("the_magic_of_the_book", 177, 186),
        ("about_good_and_bad_critics", 187, 200),
        ("my_belief", 201, 204),
        ("gratitude_to_goethe", 205, 212),
        ("a_bit_of_theology", 213, 225),
        ("on_reading_a_novel", 226, 230),
        ("from_a_diary", 231, 235),
        ("memories_of_klingsors_summer", 236, 238),
        ("postscript_to_steppenwolf", 239, 240),
        ("favorite_reading", 241, 244),
        ("the_peach_tree", 245, 248),
        ("dream_gift", 249, 253),
        ("description_of_a_landscape", 254, 264),
        ("mysteries", 265, 277),
        ("the_omitted_word", 278, 281),
        ("happiness", 282, 292),
        ("on_old_age", 293, 295),
        ("interpreting_kafka", 296, 298),
        ("anti-semitism", 299, 301),
        ("joseph_knecht_to_carlo", 302, 308),
        ("caesarius_of_heisterbach", 311, 317),
        ("giovanni_boccaccio", 318, 328),
        ("casanova", 329, 333),
        ("hans_christian_anderson", 334, 335),
        ("walt_whitman", 336, 337),
        ("august_strindberg", 338, 340),
        ("selma_lagerlof", 341, 347),
        ("maurice_maeterlinck", 348, 352),
        ("romain_rolland", 353, 357),
        ("andre_gide", 358, 360),
        ("rainer_maria_rilke", 361, 366),
        ("d_h_lawrence", 367, 369),
        ("thomas_wolfe", 370, 373),
        ("j_d_salinger", 374, 375),
        ("sigmund_freud", 379, 381),
        ("c_g_jung", 382, 384),
        ("jacob_burckhardt", 385, 386),
        ("karl_markx", 387, 387),
        ("henri_bergson", 388, 389),
        ("count_hermann", 390, 393),
        ("oswald_spengler", 394, 394),
        ("jose_ortega", 395, 396),
        ("leopold_ziegler", 397, 398),
        ("introduction_oriental_lit", 401, 402),
        ("hinduism", 403, 404),
        ("the_speeches_of_buddha", 405, 408),
        ("chinese_lit", 409, 415),
        ("view_of_the_far_east", 416, 417),
]

# Scan images within the page range and return utf-8 string
def get_text_from_images(page_start, page_end):
    full_content = ""
    for i in range(page_start, page_end+1):
        prefix = ""
        if i <= 99:
            prefix = "0"

        content = subprocess.run([
                'tesseract', 
                "./resources/image_exports/My belief _ essays on life and art - Hesse, Hermann, 1877-1962_Page_{}{}_Image_0002.jpg".format(prefix, i), 
                "-", 
                "-l", 
                "eng"
                ], stdout=subprocess.PIPE).stdout.decode("utf-8")

        # Remove first two lines to remove the consistent headers on most pages
        content = '\n'.join(content.split('\n')[2:])

        full_content += content

    return full_content

# Do basic cleaning of text
def clean_text(content):

    # remove any dash then newline 
    content = content.replace("-\n", "")

    # replace newlines with spaces
    content = re.sub(r"([^^])(\n)", r"\1 ", content)

    # replace lone newlines with paragraph tab
    content = re.sub(r"\n", r"\n\t", content)

    return content

for essay in essays:
    print("Processing {}...".format(essay))

    content = get_text_from_images(essay[1], essay[2])
    content = clean_text(content)

    f = open("./exports/automated/{}.txt".format(essay[0]), "a")
    f.write(content)
    f.close()

