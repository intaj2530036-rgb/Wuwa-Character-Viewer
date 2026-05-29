from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO
class WutheringWavesWindow(Tk):
    def __init__(self):
        super().__init__()

        self.title("Wuthering Waves Viewer")
        self.geometry("1500x1000")
        self.resizable(width=True, height=True)
        self.configure(bg="#0A192F")
        #--------------Character Data----------------
        self.character_data = {
            "Rover": {
                "element": "Spectro",
                "weapon": "Sword",
                "role": "DPS",
                "image": "https://wuthering.wiki/img/rolecard_1502.png",
                "description": ""
            },
            "Aemeath": {
                "element": "Fusion",
                "weapon": "Sword",
                "role": "DPS",
                "image": "local:Aemeath_Full_Sprite.jpg",
                "description": "Nope. As long as it's food, me likey. Though... I don't really need to eat anymore, haha."

            },
            "Carlotta": {
                "element": "Glacio",
                "weapon": "Pistol",
                "role": "DPS",
                "image": "https://wuthering.wiki/img/rolecard_1107.png",
                "description": "Desuwaaaaaa-"

            },
            "Changli": {
                "element": "Fusion",
                "weapon": "Sword",
                "role": "DPS",
                "image": "https://wuthering.wiki/img/rolecard_1205.png",
                "description": ""
            },
            "Brant": {
                "element": "Havoc",
                "weapon": "Sword",
                "role": "DPS",
                "image": "https://wuthering.wiki/img/rolecard_1206.png",
                "description": ""
            },
            "Lupa": {
                "element": "Fusion",
                "weapon": "Broadblade",
                "role": "DPS",
                "image": "https://wuthering.wiki/img/rolecard_1207.png",
                "description": "You're gonna keep me from fighting? HAH !! CAREFUL NOW"
            },
            "Augusta": {
                "element": "Electro",
                "weapon": "Broadblade",
                "role": "DPS",
                "image": "https://wuthering.wiki/img/rolecard_1306.png",
                "description": ""
            },
            "Iuno": {
                "element": "Aero",
                "weapon": "Gauntlet",
                "role": "Sub-DPS, Healer",
                "image": "https://wuthering.wiki/img/rolecard_1410.png",
                "description": ""
            },
            "Shorekeeper": {
                "element": "Spectro",
                "weapon": "Rectifier",
                "role": "Support, Healer",
                "image": "https://wuthering.wiki/img/rolecard_1505.png",
                "description": ""
            },
            "Zani": {
                "element": "Spectro",
                "weapon": "Gauntlet",
                "role": "DPS",
                "image": "https://wuthering.wiki/img/rolecard_1507.png",
                "description": "I want a vacation"

            },
            "Jiyan": {
                "element": "Aero",
                "weapon": "Broadblade",
                "role": "DPS",
                "image": "https://wuthering.wiki/img/rolecard_1404.png",
                "description": ""
            },
            "Yinlin": {
                "element": "Electro",
                "weapon": "Rectifier",
                "role": "Sub-DPS",
                "image": "https://wuthering.wiki/img/rolecard_1302.png",
                "description": ""
            },
            "Jinhsi": {
                "element": "Spectro",
                "weapon": "Broadblade",
                "role": "DPS",
                "image": "https://wuthering.wiki/img/rolecard_1304.png",
                "description": ""

            },
            "Encore": {
                "element": "Fusion",
                "weapon": "Rectifier",
                "role": "DPS",
                "image": "https://wuthering.wiki/img/rolecard_1203.png",
                "description": ""
            },
            "Verina": {
                "element": "Spectro",
                "weapon": "Rectifier",
                "role": "Support, Healer",
                "image": "https://wuthering.wiki/img/rolecard_1503.png",
                "description": ""
            },
            "Calcharo": {
                "element": "Electro",
                "weapon": "Broadblade",
                "role": "DPS",
                "image": "https://wuthering.wiki/img/rolecard_1301.png",
                "description": ""
            },
            "Lingyang": {
                "element": "Glacio",
                "weapon": "Gauntlet",
                "role": "DPS",
                "image": "https://wuthering.wiki/img/rolecard_1104.png",
                "description": ""
            },
            "Jianxin": {
                "element": "Aero",
                "weapon": "Gauntlet",
                "role": "Support, Sub-DPS",
                "image": "https://wuthering.wiki/img/rolecard_1405.png",
                "description": ""
            },
            "Mortefi": {
                "element": "Fusion",
                "weapon": "Pistol",
                "role": "Sub-DPS",
                "image": "https://wuthering.wiki/img/rolecard_1204.png",
                "description": ""
            },
            "Sanhua": {
                "element": "Glacio",
                "weapon": "Sword",
                "role": "Sub-DPS",
                "image": "https://wuthering.wiki/img/rolecard_1102.png",
                "description": ""
            },
            "Baizhi": {
                "element": "Glacio",
                "weapon": "Rectifier",
                "role": "Support, Healer",
                "image": "https://wuthering.wiki/img/rolecard_1103.png",
                "description": ""
            },
            "Yangyang": {
                "element": "Aero",
                "weapon": "Sword",
                "role": "Sub-DPS, Support",
                "image": "https://wuthering.wiki/img/rolecard_1402.png",
                "description": ""
            },
            "Chixia": {
                "element": "Fusion",
                "weapon": "Pistol",
                "role": "Sub-DPS",
                "image": "https://wuthering.wiki/img/rolecard_1202.png",
                "description": ""
            },
            "Danjin": {
                "element": "Havoc",
                "weapon": "Sword",
                "role": "DPS",
                "image": "https://wuthering.wiki/img/rolecard_1602.png",
                "description": ""
            },
            "Taoqi": {
                "element": "Havoc",
                "weapon": "Broadblade",
                "role": "Sub-DPS, Support",
                "image": "https://wuthering.wiki/img/rolecard_1601.png",
                "description": ""
            },
            "Yuanwu": {
                "element": "Electro",
                "weapon": "Gauntlet",
                "role": "Sub-DPS, Support",
                "image": "https://wuthering.wiki/img/rolecard_1303.png",
                "description": ""
            },
            "Aalto": {
                "element": "Aero",
                "weapon": "Pistol",
                "role": "Sub-DPS",
                "image": "https://wuthering.wiki/img/rolecard_1403.png",
                "description": ""
            },
            "Youhu": {
                "element": "Glacio",
                "weapon": "Gauntlet",
                "role": "Sub-DPS, Support",
                "image": "https://wuthering.wiki/img/rolecard_1106.png",
                "description": ""
            },
            "Xiangli Yao": {
                "element": "Electro",
                "weapon": "Gauntlet",
                "role": "DPS",
                "image": "https://wuthering.wiki/img/rolecard_1305.png",
                "description": ""
            },
            "Camellya": {
                "element": "Havoc",
                "weapon": "Sword",
                "role": "DPS",
                "image": "https://wuthering.wiki/img/rolecard_1603.png",
                "description": ""
            },
            "Phoebe": {
                "element": "Spectro",
                "weapon": "Rectifier",
                "role": "DPS",
                "image": "https://wuthering.wiki/img/rolecard_1506.png",
                "description": "The fish are over there...wow fish..."
            },
            "Roccia": {
                "element": "Havoc",
                "weapon": "Gauntlet",
                "role": "Sub-DPS",
                "image": "https://wuthering.wiki/img/rolecard_1604.png",
                "description": ""
            },
            "Male Rover": {
                "element": "Spectro",
                "weapon": "Sword",
                "role": "Sub-DPS, Support",
                "description": "You Will Obey!!!",
                "image": "https://wuthering.wiki/img/rolecard_1605.png",
            },
            # Aliases / alternate names:
            "Jueyuan": {  # In-game alias for Verina
                "element": "Spectro",
                "weapon": "Rectifier",
                "role": "Support, Healer",
                "image": "https://wuthering.wiki/img/rolecard_1503.png",
                "description": ""

            }
        }


        f1=Frame(self, width=750, height=750, bg="#111827")
        #f1.pack(side=LEFT, fill=BOTH, expand=True)
        self.title_label=Label(f1, text="Character List", bg="Black", fg="white", font=("Arial", 20))
        self.title_label.pack(side=TOP, fill=BOTH, expand=True)
        characters=["Rover","Aemeath",  "Carlotta", "Changli", "Iuno", "Augusta","Lupa", "Shorekeeper",
        "Brant", "Zani", "Jiyan", "Yinlin", "Jinhsi", "Encore", "Verina", "Calcharo", "Lingyang",
    "Jianxin", "Mortefi", "Sanhua", "Baizhi", "Yangyang", "Chixia", "Danjin",
    "Taoqi", "Yuanwu", "Aalto", "Youhu", "Xiangli Yao", "Camellya", "Phoebe",
    "Male Rover", "Jueyuan"]
        self.listbox= Listbox(f1, bg="#0A192F", fg="#ffffff", font=("Arial", 20), height=30, width=20, )
        for character in characters:
            self.listbox.insert(END, character)
        self.listbox.pack(fill=BOTH, expand=True, pady=10, padx=10)

        def on_select(event):
            selected = self.listbox.get(self.listbox.curselection())
            data = self.character_data[selected]

            self.name_label.config(text=selected)
            self.element_label.config(text=data["element"])
            self.weapon_label.config(text=data["weapon"])
            self.role_label.config(text=data["role"])
            self.description_label.config(text=data["description"])
            #-----image from URL----

            self.image_label.config(text="Loading...", image="")
            self.update()


            if data["image"]:
                if data["image"].startswith("local:"):
                    filename = data["image"].replace("local:", "")
                    img=Image.open(filename)
                else:
                    response = requests.get(data["image"])
                    img = Image.open(BytesIO(response.content))
                img.thumbnail((300, 450))
                photo = ImageTk.PhotoImage(img)
                self.image_label.config(image=photo)
                self.image_label.image = photo
                self.image_label.config(image=photo, text="")
        f1.pack(side=LEFT, fill=BOTH, expand=True)
        self.listbox.bind("<<ListboxSelect>>", on_select)



        f2 = Frame(self, width=750, height=750, bg="#202225")
        f2_title=Label(f2, text="Character Card", bg="Black", fg="White", font=("Arial", 20))
        f2_title.pack(side=TOP,fill=BOTH)
        f2_left = Frame(f2, bg="#202225")
        f2_left.pack(side=LEFT, fill=BOTH, expand=True)
        #title=Label(f2_left, bg="White", fg="Black", font=("Arial", 20))
        #title.pack(side=TOP, fill=BOTH, expand=True)
        image_border=Frame(f2_left, bg="#c0a060", padx=3, pady=3)
        image_border.place(relx=0.5, rely=0.5, anchor=CENTER)


        self.image_label=Label(image_border,bg="#202225", fg="white", font=("Arial", 15))
        self.image_label.pack(side=LEFT, fill=BOTH, expand=True)
        #self.image_label.pack_forget()
        #self.image_label.place(relx=0.5, rely=0.5, anchor="center")

        f2_right = Frame(f2, bg="#202225")
        f2_right.pack(side=RIGHT, fill=BOTH, expand=True, anchor="center")
        info_frame = Frame(f2_right, bg="#202225")
        info_frame.place(relx=0.5, rely=0.5, anchor="center")

        self.name_label = Label(info_frame, text="Name", bg="#202225", fg="white", font=("Arial", 20))
        self.name_label.pack(pady=10)

        self.element_label = Label(info_frame, text="Element", bg="#202225", fg="white", font=("Arial", 15))
        self.element_label.pack(pady=10)

        self.weapon_label = Label(info_frame, text="Weapon", bg="#202225", fg="white", font=("Arial", 15))
        self.weapon_label.pack(pady=10)

        self.role_label = Label(info_frame, text="Role", bg="#202225", fg="white", font=("Arial", 15))
        self.role_label.pack(pady=10)

        self.description_label= Label(info_frame, text="Description", bg="#202225", fg="white", font=("Arial", 15), wraplength=250)
        self.description_label.pack(pady=10)
        f2.pack(side=RIGHT, fill=BOTH, expand=True, pady=10, padx=10)

app = WutheringWavesWindow()
app.mainloop()

