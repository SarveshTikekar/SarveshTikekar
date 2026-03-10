from datetime import datetime

import gifos
from zoneinfo import ZoneInfo
import re, textwrap

FONT_FILE_LOGO = "./fonts/Poppins-Black.ttf"
FONT_FILE_BITMAP = "./fonts/JetBrainsMonoNerdFont-Regular.ttf"
FONT_FILE_TRUETYPE = "./fonts/JetBrainsMonoNerdFont-Regular.ttf"
FONT_FILE_MONA = "./fonts/Inversionz.otf"


def main():
    t = gifos.Terminal(1000, 650, 15, 15, FONT_FILE_BITMAP, 15)
    t.set_fps(15)
    year_now = datetime.now(ZoneInfo("Asia/Kolkata")).strftime("%Y")
    
    quotes = {
        1:  "Initializing kernel...",
        10: "Mounting /dev/brain...",
        20: "Parsing Readme logic...",
        30: "Loading shell scripts...",
        40: "Starting aysnc workers...",
        50: "Optimizing backend connections...",
        60: "SSHing for some integrations...",
        70: "Importing Stats...",
        80: "Verifying credentials...",
        90: "Finalizing system rice...",
        100: "README Loaded"
    }
    
    current_quote="Awaiting signal"
    for i in range(0, 101, 5):
        
        if i in quotes:
            current_quote = quotes[i]

        bar_length = i // 5
        progress_bar = f"[{'#' * bar_length}{' ' * (20 - bar_length)}]"
        t.delete_row(2)
        t.gen_text(f"{current_quote} {progress_bar} {i}%", 2)
        t.clone_frame(2) 

    t.gen_text("\x1b[96m", 2, count=0, contin=True)  
    t.set_font(FONT_FILE_LOGO, 66)

    os_logo_text = "सिद्धिर्भवति कर्मजा"
    mid_row = (t.num_rows + 1) // 2
    mid_col = (t.num_cols - len(os_logo_text) + 1) // 2
    effect_lines = gifos.effects.text_scramble_effect_lines(
        os_logo_text, 3, include_special=False
    )
    for i in range(len(effect_lines)):
        t.delete_row(mid_row + 1)
        t.gen_text(effect_lines[i], mid_row + 1, mid_col + 1)
    

    t.set_font(FONT_FILE_BITMAP, 15)
    t.clear_frame()
    t.clone_frame(5)
    t.toggle_show_cursor(False)
    t.gen_text("\x1b[93mSarv OS v1.1 (tty1)\x1b[0m", 1, count=5)
    t.gen_text("login: ", 3, count=5)
    t.toggle_show_cursor(True)
    t.gen_typing_text("Sarvesh Tikekar", 3, contin=True)
    t.gen_text("", 4, count=5)
    t.toggle_show_cursor(False)
    t.gen_text("password: ", 4, count=5)
    t.toggle_show_cursor(True)
    t.gen_typing_text("*!@#*$*%^&*", 4, contin=True)
    t.toggle_show_cursor(False)
    time_now = datetime.now(ZoneInfo("Asia/Kolkata")).strftime(
        "%a %b %d %I:%M:%S %p %Z %Y"
    )
    t.gen_text(f"Last login: {time_now} on tty1", 6)

    t.gen_prompt(7, count=5)
    prompt_col = t.curr_col
    t.toggle_show_cursor(True)
    t.gen_typing_text("\x1b[91mclea", 7, contin=True)
    t.delete_row(7, prompt_col) 
    t.gen_text("\x1b[92mclear\x1b[0m", 7, count=3, contin=True)

    git_user_details = gifos.utils.fetch_github_stats("SarveshTikekar")
    user_age = gifos.utils.calc_age(30, 5, 2004)
    t.clear_frame()
    user_details_lines = f"""
    \x1b[30;101mSarveshTikekar@git\x1b[0m
    --------------
    \x1b[96mHost:   \x1b[93mDon Bosco Institute of Technology
    \x1b[96mKernel: \x1b[93mComputer Science & Engineering
    \x1b[96mUptime: \x1b[93m{user_age.years} years, {user_age.months} months, {user_age.days} days\x1b[0m
    
    \x1b[30;101mContact\x1b[0m
    --------------
    \x1b[96mEmail: \x1b[93msarvesh1.tikekar@gmail.com\x1b[0m
    
    \x1b[30;101mGitHub Stats:\x1b[0m
    --------------
    \x1b[96mUser Rating: \x1b[93m{git_user_details.user_rank.level}\x1b[0m
    \x1b[96mTotal Stars Earned: \x1b[93m{git_user_details.total_stargazers}\x1b[0m
    \x1b[96mTotal Commits ({int(year_now) - 1}): \x1b[93m{git_user_details.total_commits_last_year}\x1b[0m
    \x1b[96mTotal PRs: \x1b[93m{git_user_details.total_pull_requests_made}\x1b[0m
    \x1b[96mMerged PR %: \x1b[93m{git_user_details.pull_requests_merge_percentage}\x1b[0m
    \x1b[96mTotal Contributions: \x1b[93m{git_user_details.total_repo_contributions}\x1b[0m
    """
    t.gen_prompt(1)
    prompt_col = t.curr_col
    t.clone_frame(10)
    t.toggle_show_cursor(True)
    t.delete_row(1, prompt_col)

    t.gen_typing_text("\x1b[92mwhoami\x1b[0m", 1, contin=True)

    t.set_font(FONT_FILE_MONA, 16, 0)
    t.toggle_show_cursor(False)
    monaLines = r"""
    \x1b[49m     \x1b[90;100m}}\x1b[49m     \x1b[90;100m}}\x1b[0m
    \x1b[49m    \x1b[90;100m}}}}\x1b[49m   \x1b[90;100m}}}}\x1b[0m
    \x1b[49m    \x1b[90;100m}}}}}\x1b[49m \x1b[90;100m}}}}}\x1b[0m
    \x1b[49m   \x1b[90;100m}}}}}}}}}}}}}\x1b[0m
    \x1b[49m   \x1b[90;100m}}}}}}}}}}}}}}\x1b[0m
    \x1b[49m   \x1b[90;100m}}\x1b[37;47m}}}}}}}\x1b[90;100m}}}}}\x1b[0m
    \x1b[49m  \x1b[90;100m}}\x1b[37;47m}}}}}}}}}}\x1b[90;100m}}}\x1b[0m
    \x1b[49m  \x1b[90;100m}}\x1b[37;47m}\x1b[90;100m}\x1b[37;47m}}}}}\x1b[90;100m}\x1b[37;47m}}\x1b[90;100m}}}}\x1b[0m
    \x1b[49m  \x1b[90;100m}\x1b[37;47m}}\x1b[90;100m}\x1b[37;47m}}}}}\x1b[90;100m}\x1b[37;47m}}}\x1b[90;100m}}}\x1b[0m
    \x1b[90;100m}}}\x1b[37;47m}}}}\x1b[90;100m}}}\x1b[37;47m}}}}}\x1b[90;100m}}}}\x1b[0m
    \x1b[49m  \x1b[90;100m}\x1b[37;47m}}}}}\x1b[90;100m}}\x1b[37;47m}}}}}\x1b[90;100m}}}\x1b[0m
    \x1b[49m \x1b[90;100m}}\x1b[37;47m}}}}}}}}}}}}\x1b[90;100m}}}\x1b[0m
    \x1b[90;100m}\x1b[49m  \x1b[90;100m}}\x1b[37;47m}}}}}}}}\x1b[90;100m}}}\x1b[49m  \x1b[90;100m}\x1b[0m
    \x1b[49m        \x1b[90;100m}}}}}\x1b[0m
    \x1b[49m       \x1b[90;100m}}}}}}}\x1b[0m
    \x1b[49m       \x1b[90;100m}}}}}}}}\x1b[0m
    \x1b[49m      \x1b[90;100m}}}}}}}}}}\x1b[0m
    \x1b[49m     \x1b[90;100m}}}}}}}}}}}\x1b[0m
    \x1b[49m     \x1b[90;100m}}}}}}}}}}}}\x1b[0m
    \x1b[49m     \x1b[90;100m}}\x1b[49m \x1b[90;100m}}}}}}\x1b[49m \x1b[90;100m}}\x1b[0m
    \x1b[49m        \x1b[90;100m}}}}}}}\x1b[0m
    \x1b[49m         \x1b[90;100m}}}\x1b[49m \x1b[90;100m}}\x1b[0m
    """
    t.gen_text(monaLines, 10)

    t.set_font(FONT_FILE_BITMAP)
    t.toggle_show_cursor(True)
    # t.pasteImage("./temp/SarveshTikekar.jpg", 3, 5, sizeMulti=0.5)
    t.gen_text(user_details_lines, 2, 35, count=5, contin=True)
    t.gen_prompt(t.curr_row)
    t.gen_typing_text(
        "\x1b[92m# Check out the rest of the profile below! Happy Coding and Debugging ",
        t.curr_row,
        contin=True,
    )
    # t.save_frame("fetch_details.png")
    t.gen_text("", t.curr_row, count=100, contin=True)
    t.gen_prompt(t.curr_row + 2)
    t.gen_typing_text("\x1b[92mreboot\x1b[0m", t.curr_row, contin=True)
    t.gen_gif()
   
if __name__ == "__main__":
    main()
