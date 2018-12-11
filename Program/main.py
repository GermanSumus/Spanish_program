"""
TODO: Make menu more flexible
TODO: Make multiple_choice more flexible ln # 169
FIXED: ValueError raised in check_validity ln # 44
BUG: refresher function not getting called after exiting
    back to menu. multiple_choice starts isnteadself. May
    have a looping error from previus fix in check_validity
"""
import program

program.make_menu()
