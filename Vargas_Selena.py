# ============================================================
# DS3850 — Project 5: Personal Budget Tracker GUI
# Name: Selena Vargas
# Section: DS 3850-001
# Date: 3/08/2026
# ============================================================
import customtkinter as ctk
# ── App appearance ───────────────────────────────────────────
ctk.set_appearance_mode('light')
ctk.set_default_color_theme('blue')
# ── Main window ──────────────────────────────────────────────
root = ctk.CTk()
root.title('Personal Budget Tracker')
root.geometry('580x640')
root.resizable(False, False)
# ── Data storage ─────────────────────────────────────────────
budget_items = [] # Each item: {'desc': ..., 'amount': ..., 'category': ...}
# ── Category options ─────────────────────────────────────────
CATEGORIES = ['Housing', 'Food', 'Transportation',
 'Utilities', 'Entertainment', 'Other']
# ────────────────────────────────────────────────────────────
# FORM WIDGETS (add your Labels, Entries, OptionMenu here)
# ────────────────────────────────────────────────────────────
# TODO: Description label and entry
# TODO: Amount label and entry
# TODO: Category label and OptionMenu
# TODO: Status label (shows success or error messages)
# TODO: Buttons (Add Item, Clear Form, Clear All)
# TODO: Display area (CTkTextbox) and Total label
# ────────────────────────────────────────────────────────────
# FUNCTIONS
# ────────────────────────────────────────────────────────────
def add_item():
 """Validate inputs and add item to budget_items list."""
 # TODO: Get values from desc_entry, amount_entry, category_menu
 # TODO: Validate description is not empty
 # TODO: Validate amount is a positive number (try/except)
 # TODO: Append dict to budget_items
 # TODO: Call refresh_display()
 # TODO: Show success message in status_label
 # TODO: Clear desc_entry and amount_entry
 pass
def clear_form():
 """Clear the Description and Amount fields only."""
 # TODO: Delete contents of desc_entry and amount_entry
 # TODO: Reset status_label
 pass
def clear_all():
 """Remove all items and reset the display."""
 # TODO: Clear budget_items list
 # TODO: Call refresh_display()
 # TODO: Reset status_label
 pass
def refresh_display():
 """Rebuild the textbox display from budget_items list."""
 # TODO: Enable the textbox, clear it
 # TODO: If list is empty, show 'No items yet.'
 # TODO: Loop through budget_items and insert formatted lines
 # TODO: Insert a separator line and total at the bottom
 # TODO: Disable the textbox
 pass
# ── Wire buttons to functions ─────────────────────────────────
# TODO: Set command= on each button
# ── Initial display ───────────────────────────────────────────
refresh_display()
root.mainloop()