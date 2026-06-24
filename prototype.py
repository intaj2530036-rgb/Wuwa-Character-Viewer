import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# --- Data ---
game_data = {
    "Wuthering Waves": ["Rover", "Carlotta", "Jiyan", "Shorekeeper", "Changli"],
    "Genshin Impact": ["Lumine", "Hu Tao", "Zhongli", "Raiden Shogun", "Nahida"],
    "Arknights": ["Amiya", "Skadi", "Surtr", "Edmin", "W"]
}

class GameViewer(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Multi-Game Viewer")
        self.geometry("400x600")
        self.configure(fg_color="#0A192F")

        # --- Dropdown ---
        self.selected_game = ctk.StringVar(value="Wuthering Waves")

        self.dropdown = ctk.CTkOptionMenu(
            self,
            values=list(game_data.keys()),   # ["Wuthering Waves", "Genshin Impact", "Arknights"]
            variable=self.selected_game,
            command=self.switch_game,         # called automatically on selection
            fg_color="#1E3A5F",
            button_color="#2A5298",
            button_hover_color="#3B6FD4"
        )
        self.dropdown.pack(pady=20)

        # --- Scrollable Frame ---
        self.scroll_frame = ctk.CTkScrollableFrame(
            self,
            width=300,
            height=400,
            corner_radius=15,
            fg_color="#111827"
        )
        self.scroll_frame.pack(pady=10)

        # Load default game on startup
        self.load_characters("Wuthering Waves")

    def switch_game(self, selected):       # 'selected' is passed automatically by CTkOptionMenu
        self.load_characters(selected)

    def load_characters(self, game):
        # Clear existing characters first
        for widget in self.scroll_frame.winfo_children():
            widget.destroy()

        # Populate with new list
        for character in game_data[game]:
            label = ctk.CTkLabel(
                self.scroll_frame,
                text=character,
                font=("Arial", 16),
                fg_color="#1E3A5F",
                corner_radius=8
            )
            label.pack(pady=5, padx=10, fill="x")

app = GameViewer()
app.mainloop()