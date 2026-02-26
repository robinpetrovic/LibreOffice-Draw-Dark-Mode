# LibreOffice Draw Dark Mode

## Personal Note

This is my only project of this kind. I created it from the heart, originally intended **only for my personal use**, because I could not find any solution for LibreOffice Draw’s lack of a dark mode.

I decided to share it with the world because I **know many people face the same problem**, and there was **no solution available online**.  
By publishing it, I wanted to **help others solve this issue** and make working in LibreOffice Draw in dark environments easier for everyone.

## Short Description

I originally developed this Dark Mode macro for personal use...

# LibreOffice Draw Dark Mode

A simple Python macro for LibreOffice Draw that toggles all pages of a document between **light mode** and **dark mode**.
The background becomes dark/light, and all text is inverted (white/black).
Images remain unchanged.

---

## Installation

1. Extract the `DrawDarkMode` folder anywhere on your computer.
2. Copy the contents of the `Scripts/python` folder to the LibreOffice scripts folder:

   - **Windows:** `%APPDATA%\LibreOffice\4\user\Scripts\python\`
   - **Linux:** `~/.config/libreoffice/4/user/Scripts/python/`
   - **macOS:** `~/Library/Application Support/LibreOffice/4/user/Scripts/python/`

3. Open LibreOffice Draw.
4. Tools → **Macros → Organize Macros → Python → draw_dark_mode_stable.py → toggle_dark_mode → Run**
   - Dark mode will activate immediately. Click again to switch back to light mode.

---

## Adding a button to the toolbar

1. Tools → **Customize → Toolbars → Draw**
2. Click **Add → Macros → Python → draw_dark_mode_stable.py → toggle_dark_mode**
3. Give it a name, e.g., “Dark Mode”
4. Optional: Choose an icon from the `Icons/dark_mode.png` folder

Now you can toggle dark mode anytime via the toolbar button.

---

## License

This project is licensed under the **MIT License**:

- Anyone may **use, copy, share, and modify** the code freely.
- You must **credit the author, Robin Petrovic**.
- No liability for damages or errors.

See the `LICENSE` file for the full license text.

---

## Notes

- Works only with **LibreOffice Draw**.
- Images are not inverted; only **background and text** are adjusted.

