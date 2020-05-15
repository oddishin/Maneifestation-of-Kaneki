
# ----------------------
# CHARACTER DEFINITIONS
# ----------------------

define kan = Character("Kaneki", color="#34558b")
define hid = Character("Hide", color="ffa500")
define tou = Character("Touka", color="#65187a")
define rize = Character("Rize", color="#a674be")
define dr = Character("Dr. Kanou", color="#982020")
define nur = Character("Nurse Taguchi", color="#a5ffcb")
define news = Character("Newscaster", color="#b98a5a")

# ------------------------
# SPRITE / BG DEFINITIONS
# BG = 1280 x 720
# Sprite = 200 x 680
# ------------------------

image black = "black.png"

# ------
# ACT 1
# ------

image kan_hide = im.Scale("act1/cg_kaneki_hide_1.png", 1280, 720)
image kan_hide2 = im.Scale("act1/cg_kaneki_hide_2.png", 1280, 720)
image kan_hide3 = im.Scale("act1/cg_kaneki_hide_3.png", 1280, 720)
image kan_hide_tou = im.Scale("act1/cg_kaneki_hide_touka.png", 1280, 720)
image rize_walk = im.Scale("act1/cg_rize_walking.png", 1280, 720)
image touka = im.Scale("act1/cg_touka_smile.png", 1280, 720)
image rize = im.Scale("act1/cg_rize_enter.png", 1280, 720)
image hide_leave = im.Scale("act1/hide_leave.png", 1280, 720)

# ------
# ACT 2
# ------

image city_night = im.Scale("act2/bg_city_night.png", 1280, 720)
image bike = im.Scale("act2/cg_hide_bike.png", 1280, 720)
image kan_read1 = im.Scale("act2/cg_kaneki_reading_1.png", 1280, 720)
image kan_read2 = im.Scale("act2/cg_kaneki_reading_2.png", 1280, 720)
image rize_read = im.Scale("act2/cg_rize_reading.png", 1280, 720)
image restaurant = im.Scale("act3/bg_restaurant.png", 1280, 720)
image date1 = im.Scale("act3/cg_date_1.png", 1280, 720)

# ------
# ACT 3
# ------

image end_date_cg = im.Scale("act3/cg_end_date.png", 1280, 720)
image walk = im.Scale("act3/cg_walking.png", 1280, 720)
image cough = im.Scale("act3/cg_cough.png", 1280, 720)
image end_date_bg = im.Scale("act4/bg_end_date.png", 1280, 720)
image street = im.Scale("act4/bg_bridge_street.png", 1280, 720)
image park = im.Scale("act4/bg_park_night.png", 1280, 720)
image alley1 = im.Scale("act4/cg_alley.png", 1280, 720)

# ------
# ACT 4
# ------

image alley2 = im.Scale("act4/cg_alley_1.png", 1280, 720)
image realize1 = im.Scale("act4/cg_alley_3.png", 1280, 720)
image realize2 = im.Scale("act4/cg_alley_4.png", 1280, 720)
image realize3 = im.Scale("act4/cg_alley_2.png", 1280, 720)
image bite = im.Scale("act4/cg_bite.png", 1280, 720)
image kan_run = im.Scale("act4/cg_kaneki_running.png", 1280, 720)
image scared = im.Scale("act4/cg_kaneki_scared.png", 1280, 720)
image evil_smile = im.Scale("act4/cg_rize_evilsmile.png", 1280, 720)
image evil_con = im.Scale("act4/cg_rize_evilconfused.png", 1280, 720)

# ------
# ACT 5
# ------

image eye_closed = im.Scale("act5/cg_kaneki_eye_closed.png", 1280, 720)
image eye_open = im.Scale("act5/cg_kaneki_eye_open.png", 1280, 720)
image kan_float = im.Scale("act5/cg_kaneki_float_smile.png", 1280, 720)
image kan_hosp = im.Scale("act5/cg_kaneki_hospital.png", 1280, 720)
image kan_rize_float = im.Scale("act5/cg_kaneki_rize_float.png", 1280, 720)
image kan_water = im.Scale("act5/cg_kaneki_water.png", 1280, 720)
image water = im.Scale("act5/cg_water.png", 1280, 720)

# --------
# SPRITES
# --------

image kaneki_ = im.Scale("kaneki_sprite.png", 178, 680)
image hide_ = im.Scale("hide_sprite.png", 206, 680)
image touka_ = im.Scale("touka_sprite.png", 217, 680)
image rize_ = im.Scale("rize_sprite.png", 264, 680)

# ----------------
# TRANSFORMATIONS
# ----------------

transform partialright:
    xalign 0.75
    yalign 2.5

transform partialleft:
    xalign 0.25
    yalign 2.5

transform centerright:
    xalign 0.70
    yalign 2.5

transform centerleft:
    xalign 0.30
    yalign 2.5

define slow_fade = Fade(1.0, 0.0, 1.0)
define sslow_fade = Fade(2.0, 0.0, 2.0)
define slow_dissolve = Dissolve(1.0)
define sslow_dissolve = Dissolve(2.0)