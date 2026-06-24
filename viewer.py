import customtkinter as ctk
from game_data import character_data
import requests
from io import BytesIO
from PIL import Image

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class GameWindow(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Ghacha Game Character Viewer")
        self.geometry("1200x1000")
        self.config(background="black")

#------drop down bar---------
        self.selected_game=ctk.StringVar(value="Wuthering Waves")

        self.game_dropdown=ctk.CTkOptionMenu(
            self,
            values=list(character_data.keys()),
            variable=self.selected_game,
            command=self.switch_game,
            fg_color="#1E3A5F",
            button_color="#2A5298",
            button_hover_color="#3B6FD4",
            font=("Arial", 14, "bold"),
            width=200
        )
        self.game_dropdown.pack(side="top", pady=5)

#left panel: Scroll bar on character list--------------

        self.list_frame=ctk.CTkScrollableFrame(
            self,
            width=250,
            height=700,
            corner_radius=15,
            fg_color="#111827",
            label_text="Characters",
            label_font=("Arial", 16, "bold"),
            label_fg_color="#0A192F"
        )
        self.list_frame.pack(side="left",fill="y", padx=20, pady=15)

#right panel: Character card area---------------
        self.card_frame=ctk.CTkFrame(
            self,
            corner_radius=20,
            fg_color="#202225"
        )
        self.card_frame.pack(side="right", fill="both", expand=True, padx=15, pady=10)

        self.image_label=ctk.CTkLabel(
            self.card_frame,
            text="No Image",
            width=300,
            height=400,
            corner_radius=15,
            fg_color="#111827",
            font=("Arial", 14)
        )
        self.image_label.pack(pady=30)

        self.name_label=ctk.CTkLabel(self.card_frame, text="Name", font=("Arial", 26, "bold"), text_color="#c0a060")
        self.name_label.pack(pady=5)
        self.element_label=ctk.CTkLabel(self.card_frame, text="Name", font=("Arial", 26, "bold"), text_color="#c0a060")
        self.element_label.pack(pady=5)
        self.weapon_label=ctk.CTkLabel(self.card_frame, text="Name", font=("Arial", 26, "bold"), text_color="#c0a060")
        self.weapon_label.pack(pady=5)
        self.role_label=ctk.CTkLabel(self.card_frame, text="Name", font=("Arial", 26, "bold"), text_color="#c0a060")
        self.role_label.pack(pady=5)
        self.description_label=ctk.CTkLabel(
            self.card_frame, text="Description", font=("Arial", 26, "bold"),
            wraplength=350, text_color="#9ca3af"
        )
        self.description_label.pack(pady=5)

#initial game loading-------------------
        self.load_characters("Wuthering Waves")
    def switch_game(self, selected):
        self.load_characters(selected)

    def load_characters(self, game):
        for widget in self.list_frame.winfo_children():  # was card_frame
            widget.destroy()
        for name in character_data[game].keys():
            character_button = ctk.CTkButton(
                self.list_frame,  # was card_frame
                text=name,
                fg_color="#1E3A5F",
                hover_color="#2A5298",
                anchor="w",
                command=lambda n=name, g=game: self.show_character(g, n)
            )
            character_button.pack(pady=5, fill="x")

    def show_character(self, game, character_name):
        data = character_data[game][character_name]

        self.name_label.configure(text=character_name)
        self.element_label.configure(text=f"Element: {data['element']}")
        self.weapon_label.configure(text=f"Weapon: {data['weapon']}")
        self.role_label.configure(text=f"Role: {data['role']}")
        self.description_label.configure(text=data['description'])

#Image handling------------
        img_path = data["image"]
        if img_path == "":
            self.image_label.configure(image=None, text="No Image")
        else:
            try:
                if img_path.startswith("local:"):
                    filename = img_path.replace("local:", "")
                    pil_image = Image.open(filename)
                else:
                    response = requests.get(img_path, timeout=5)
                    pil_image = Image.open(BytesIO(response.content))

                ctk_img = ctk.CTkImage(light_image=pil_image, dark_image=pil_image, size=(350, 470))
                self.image_label.configure(image=ctk_img, text="")
            except Exception as e:
                print(f"Image load failed: {e}")
                self.image_label.configure(image=None, text="Image Unavailable")
app = GameWindow()
app.mainloop()

