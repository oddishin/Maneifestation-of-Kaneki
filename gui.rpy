# ---------------------------------
## INITIALIZATION
# ---------------------------------

init offset = -2

init python:
    gui.init(1280, 720)

# ---------------------------------
## GUI CONFIGURATION VARIABLES
# ---------------------------------

# -----------------
## COLORS
# -----------------

define gui.accent_color = '#cc0000'
define gui.idle_color = '#888888'
define gui.idle_small_color = '#aaaaaa'
define gui.hover_color = '#e06666'
define gui.selected_color = '#ffffff'
define gui.insensitive_color = '#8888887f'
define gui.muted_color = '#510000'
define gui.hover_muted_color = '#7a0000'
define gui.text_color = '#ffffff'
define gui.interface_text_color = '#ffffff'

# ------------------------------
## FONTS / FONT SIZES
# ------------------------------

define gui.text_font = "DejaVuSans.ttf"
define gui.name_text_font = "DejaVuSans.ttf"
define gui.interface_text_font = "DejaVuSans.ttf"
define gui.text_size = 22
define gui.name_text_size = 30
define gui.interface_text_size = 22
define gui.label_text_size = 24
define gui.notify_text_size = 16
define gui.title_text_size = 50

# ------------------------------
## MAIN / GAME MENUS
# ------------------------------

define gui.main_menu_background = im.Scale("images/act1/cg_rize_walking.png", 1280, 720)
define gui.game_menu_background = im.Scale("images/act1/cg_rize_walking.png", 1280, 720)

# --------------------
## DIALOGUE 
# --------------------

define gui.textbox_height = 185
define gui.textbox_yalign = 1.0 3  # bottom-aligned

define gui.name_xpos = 240
define gui.name_ypos = 0

define gui.name_xalign = 0.0  # left-aligned

define gui.namebox_width = None
define gui.namebox_height = None

define gui.namebox_borders = Borders(5, 5, 5, 5)

define gui.namebox_tile = False

define gui.dialogue_xpos = 268
define gui.dialogue_ypos = 50

define gui.dialogue_width = 744

define gui.dialogue_text_xalign = 1.0

# ---------------------
## BUTTONS
# ---------------------

define gui.button_width = None
define gui.button_height = None

define gui.button_borders = Borders(4, 4, 4, 4)

define gui.button_tile = False

define gui.button_text_font = gui.interface_text_font

define gui.button_text_size = gui.interface_text_size

define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.selected_color
define gui.button_text_insensitive_color = gui.insensitive_color

define gui.button_text_xalign = 1.0


define gui.radio_button_borders = Borders(18, 4, 4, 4)

define gui.check_button_borders = Borders(18, 4, 4, 4)

define gui.confirm_button_text_xalign = 0.5

define gui.page_button_borders = Borders(10, 4, 10, 4)

define gui.quick_button_borders = Borders(10, 4, 10, 0)
define gui.quick_button_text_size = 14
define gui.quick_button_text_idle_color = gui.idle_small_color
define gui.quick_button_text_selected_color = gui.accent_color

## Uncomment the following line to set the width of navigation button.
# define gui.navigation_button_width = 250

# ---------------------------
## CHOICE BUTTONS
# ---------------------------

define gui.choice_button_width = 790
define gui.choice_button_height = None
define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(100, 5, 100, 5)
define gui.choice_button_text_font = gui.text_font
define gui.choice_button_text_size = gui.text_size
define gui.choice_button_text_xalign = 0.5
define gui.choice_button_text_idle_color = "#cccccc"
define gui.choice_button_text_hover_color = "#ffffff"
define gui.choice_button_text_insensitive_color = "#444444"

# ----------------------------
## FILE SLOT BUTTONS
# ----------------------------

define gui.slot_button_width = 276
define gui.slot_button_height = 206
define gui.slot_button_borders = Borders(10, 10, 10, 10)
define gui.slot_button_text_size = 14
define gui.slot_button_text_xalign = 0.5
define gui.slot_button_text_idle_color = gui.idle_small_color
define gui.slot_button_text_selected_idle_color = gui.selected_color
define gui.slot_button_text_selected_hover_color = gui.hover_color

define config.thumbnail_width = 256
define config.thumbnail_height = 144

define gui.file_slot_cols = 3
define gui.file_slot_rows = 2

# --------------------------------
## POSITION / SPACING 
# --------------------------------

## The position of the left side of the navigation buttons, relative to the left
## side of the screen.
define gui.navigation_xpos = 40

## The vertical position of the skip indicator.
define gui.skip_ypos = 10

## The vertical position of the notify screen.
define gui.notify_ypos = 45

## The spacing between menu choices.
define gui.choice_spacing = 22

## Buttons in the navigation section of the main and game menus.
define gui.navigation_spacing = 4

## Controls the amount of spacing between preferences.
define gui.pref_spacing = 10

## Controls the amount of spacing between preference buttons.
define gui.pref_button_spacing = 0

## The spacing between file page buttons.
define gui.page_spacing = 0

## The spacing between file slots.
define gui.slot_spacing = 10

## The position of the main menu text.
define gui.main_menu_text_xalign = 0.0

# --------------------
## FRAMES
# --------------------

## Generic frames.
define gui.frame_borders = Borders(4, 4, 4, 4)  # Generic frames
define gui.confirm_frame_borders = Borders(40, 40, 40, 40)  # Confirm screen
define gui.skip_frame_borders = Borders(16, 5, 50, 5)  # Skip screen
define gui.notify_frame_borders = Borders(16, 5, 40, 5)  # Notify screen
define gui.frame_tile = False  

# --------------------------------------
## BARS / SCROLLBARS / SLIDERS 
# --------------------------------------

define gui.bar_size = 25  # Horizontal height, vertical width
define gui.scrollbar_size = 12
define gui.slider_size = 25

define gui.bar_tile = False
define gui.scrollbar_tile = False
define gui.slider_tile = False

define gui.bar_borders = Borders(4, 4, 4, 4)
define gui.scrollbar_borders = Borders(4, 4, 4, 4)
define gui.slider_borders = Borders(4, 4, 4, 4)

define gui.vbar_borders = Borders(4, 4, 4, 4)
define gui.vscrollbar_borders = Borders(4, 4, 4, 4)
define gui.vslider_borders = Borders(4, 4, 4, 4)

define gui.unscrollable = "hide"

# ------------
## HISTORY
# ------------

## The number of blocks of dialogue history Ren'Py will keep.
define config.history_length = 250

## The height of a history screen entry
define gui.history_height = 140

## The position, width, and alignment of the label giving the name of the speaking character.
define gui.history_name_xpos = 155
define gui.history_name_ypos = 0
define gui.history_name_width = 155
define gui.history_name_xalign = 1.0

## The position, width, and alignment of the dialogue text.
define gui.history_text_xpos = 170
define gui.history_text_ypos = 2
define gui.history_text_width = 740
define gui.history_text_xalign = 0.0

# -----------------
## NVL-Mode
# -----------------

## The borders of the background of the NVL-mode background window.
define gui.nvl_borders = Borders(0, 10, 0, 20)

## The maximum number of NVL-mode entries Ren'Py will display.
define gui.nvl_list_length = 6

## The height of an NVL-mode entry. Set this to None to have the entries dynamically adjust height.
define gui.nvl_height = 115

## The spacing between NVL-mode entries when gui.nvl_height is None, and between NVL-mode entries and an NVL-mode menu.
define gui.nvl_spacing = 10

## The position, width, and alignment of the label giving the name of the speaking character.
define gui.nvl_name_xpos = 430
define gui.nvl_name_ypos = 0
define gui.nvl_name_width = 150
define gui.nvl_name_xalign = 1.0

## The position, width, and alignment of the dialogue text.
define gui.nvl_text_xpos = 450
define gui.nvl_text_ypos = 8
define gui.nvl_text_width = 590
define gui.nvl_text_xalign = 0.0

## The position, width, and alignment of nvl_thought text
define gui.nvl_thought_xpos = 240
define gui.nvl_thought_ypos = 0
define gui.nvl_thought_width = 780
define gui.nvl_thought_xalign = 0.0

## The position of nvl menu_buttons.
define gui.nvl_button_xpos = 450
define gui.nvl_button_xalign = 0.0

# ------------------
## LOCALIZATION 
# ------------------

define gui.language = "unicode"

# -----------------------
## MOBILE DEVICES
# -----------------------

init python:

    ## This increases the size of the quick buttons to make them easier to touch on tablets and phones.
    if renpy.variant("touch"):
        gui.quick_button_borders = Borders(40, 14, 40, 0)

    ## This changes the size and spacing of various GUI elements to ensure they are easily visible on phones.
    if renpy.variant("small"):

        ## Font sizes.
        gui.text_size = 30
        gui.name_text_size = 36
        gui.notify_text_size = 25
        gui.interface_text_size = 30
        gui.button_text_size = 30
        gui.label_text_size = 34

        ## Adjust the location of the textbox.
        gui.textbox_height = 240

        gui.name_xpos = 80

        gui.text_xpos = 90
        gui.text_width = 1100

        ## Change the size and spacing of various things.
        gui.slider_size = 36

        gui.choice_button_width = 1240

        gui.navigation_spacing = 20
        gui.pref_button_spacing = 10

        gui.history_height = 190
        gui.history_text_width = 690

        gui.quick_button_text_size = 20

        ## File button layout.
        gui.file_slot_cols = 2
        gui.file_slot_rows = 2

        ## NVL-mode.
        gui.nvl_height = 170

        gui.nvl_name_width = 305
        gui.nvl_name_xpos = 325

        gui.nvl_text_width = 915
        gui.nvl_text_xpos = 345
        gui.nvl_text_ypos = 5

        gui.nvl_thought_width = 1240
        gui.nvl_thought_xpos = 20

        gui.nvl_button_width = 1240
        gui.nvl_button_xpos = 20