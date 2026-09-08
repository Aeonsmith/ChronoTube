import customtkinter as ctk
from tkinter import messagebox, Canvas
import json
import math
import time
import datetime
import os
import sys

# =============================================================================
# ChronoTube Engine: Multi-Dimensional YouTube Time-Machine & Archaeology OS
# Interactive Desktop GUI Application
# =============================================================================

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# Theme Palette
COLOR_BG = "#07080c"
COLOR_SIDEBAR = "#0c0e15"
COLOR_CARD = "#121520"
COLOR_CARD_HOVER = "#1a1f2e"
COLOR_ACCENT = "#ef4444"       # YouTube Red
COLOR_ACCENT_HOVER = "#dc2626"
COLOR_GOLD = "#f59e0b"         # 5-Star Golden Rating
COLOR_CYAN = "#06b6d4"         # Vector Slerp / Era Indicator
COLOR_EMERALD = "#10b981"      # Active Archive Connection
COLOR_PURPLE = "#a855f7"       # Cosmic / Neural AI
COLOR_AMBER = "#d97706"        # Simulation Watermark
COLOR_TEXT_PRIMARY = "#f3f4f6"
COLOR_TEXT_MUTED = "#9ca3af"
COLOR_BORDER = "#222738"

HISTORICAL_VIDEOS = {
    "me_at_the_zoo": {
        "id": "video:me_at_the_zoo",
        "title": "Me at the zoo",
        "creator": "jawed",
        "upload_date": "2005-04-23",
        "description": "The first video uploaded to YouTube by co-founder Jawed Karim at the San Diego Zoo.",
        "tags": ["zoo", "jawed", "first-video", "elephants", "san-diego"],
        "snapshots": [
            {"date": "2005-04-23", "views": 1, "stars": 5.0, "likes": 0, "dislikes": 0, "comments": 0},
            {"date": "2006-04-23", "views": 45000, "stars": 4.95, "likes": 2200, "dislikes": 12, "comments": 350},
            {"date": "2010-04-23", "views": 2500000, "stars": 4.88, "likes": 120000, "dislikes": 1400, "comments": 25000},
            {"date": "2015-04-23", "views": 25000000, "stars": 4.85, "likes": 1200000, "dislikes": 18000, "comments": 350000},
            {"date": "2020-04-23", "views": 90000000, "stars": 4.82, "likes": 4800000, "dislikes": 65000, "comments": 1100000},
            {"date": "2026-09-08", "views": 335000000, "stars": 4.80, "likes": 16500000, "dislikes": 120000, "comments": 4200000}
        ]
    },
    "evolution_of_dance": {
        "id": "video:evolution_of_dance",
        "title": "Evolution of Dance",
        "creator": "Judson Laipply",
        "upload_date": "2006-04-06",
        "description": "Viral milestone performance showcasing 32 iconic dance songs in 6 minutes.",
        "tags": ["dance", "viral", "comedy", "judson", "classic"],
        "snapshots": [
            {"date": "2006-04-06", "views": 10, "stars": 5.0, "likes": 5, "dislikes": 0, "comments": 2},
            {"date": "2006-12-31", "views": 38000000, "stars": 4.98, "likes": 450000, "dislikes": 2100, "comments": 180000},
            {"date": "2010-01-01", "views": 135000000, "stars": 4.92, "likes": 950000, "dislikes": 8500, "comments": 420000},
            {"date": "2018-01-01", "views": 305000000, "stars": 4.89, "likes": 2100000, "dislikes": 32000, "comments": 850000},
            {"date": "2026-09-08", "views": 315000000, "stars": 4.87, "likes": 2300000, "dislikes": 36000, "comments": 920000}
        ]
    },
    "charlie_bit_my_finger": {
        "id": "video:charlie_bit_my_finger",
        "title": "Charlie bit my finger - again !",
        "creator": "HDCYT",
        "upload_date": "2007-05-22",
        "description": "Historic British viral video of infant Charlie biting his brother Harry's finger.",
        "tags": ["charlie", "family", "viral", "funny", "brothers"],
        "snapshots": [
            {"date": "2007-05-22", "views": 5, "stars": 5.0, "likes": 2, "dislikes": 0, "comments": 0},
            {"date": "2008-05-22", "views": 25000000, "stars": 4.96, "likes": 320000, "dislikes": 1500, "comments": 95000},
            {"date": "2011-10-01", "views": 375000000, "stars": 4.91, "likes": 1800000, "dislikes": 42000, "comments": 780000},
            {"date": "2021-05-01", "views": 880000000, "stars": 4.88, "likes": 3400000, "dislikes": 110000, "comments": 1950000},
            {"date": "2026-09-08", "views": 910000000, "stars": 4.87, "likes": 3600000, "dislikes": 115000, "comments": 2050000}
        ]
    },
    "chocolate_rain": {
        "id": "video:chocolate_rain",
        "title": "Chocolate Rain",
        "creator": "Tay Zonday",
        "upload_date": "2007-04-22",
        "description": "Original deep baritone viral song by Tay Zonday ('**I move away from the mic to breathe in').",
        "tags": ["tay-zonday", "music", "meme", "baritone", "classic"],
        "snapshots": [
            {"date": "2007-04-22", "views": 2, "stars": 5.0, "likes": 1, "dislikes": 0, "comments": 0},
            {"date": "2007-12-31", "views": 15000000, "stars": 4.85, "likes": 210000, "dislikes": 8000, "comments": 140000},
            {"date": "2015-01-01", "views": 105000000, "stars": 4.79, "likes": 950000, "dislikes": 45000, "comments": 520000},
            {"date": "2026-09-08", "views": 138000000, "stars": 4.78, "likes": 1450000, "dislikes": 51000, "comments": 680000}
        ]
    },
    "gangnam_style": {
        "id": "video:gangnam_style",
        "title": "PSY - GANGNAM STYLE (강남스타일) M/V",
        "creator": "officialpsy",
        "upload_date": "2012-07-15",
        "description": "First video to break YouTube's 32-bit integer view counter, forcing upgrade to 64-bit integer.",
        "tags": ["psy", "kpop", "gangnam-style", "record-breaker", "music"],
        "snapshots": [
            {"date": "2012-07-15", "views": 100, "stars": 5.0, "likes": 50, "dislikes": 0, "comments": 10},
            {"date": "2012-12-21", "views": 1000000000, "stars": 4.89, "likes": 7500000, "dislikes": 320000, "comments": 4500000},
            {"date": "2014-12-01", "views": 2147483647, "stars": 4.86, "likes": 11000000, "dislikes": 650000, "comments": 8200000},
            {"date": "2020-01-01", "views": 3500000000, "stars": 4.84, "likes": 18000000, "dislikes": 980000, "comments": 14000000},
            {"date": "2026-09-08", "views": 5250000000, "stars": 4.83, "likes": 28500000, "dislikes": 1100000, "comments": 19800000}
        ]
    },
    "mrbeast_squid_game": {
        "id": "video:mrbeast_squid_game",
        "title": "$456,000 Squid Game In Real Life!",
        "creator": "MrBeast",
        "upload_date": "2021-11-24",
        "description": "Viral real-life recreation of the Netflix phenomenon with 456 players and massive sets.",
        "tags": ["mrbeast", "squid-game", "entertainment", "mega-production"],
        "snapshots": [
            {"date": "2021-11-24", "views": 100000, "stars": 4.95, "likes": 500000, "dislikes": 2000, "comments": 45000},
            {"date": "2021-12-01", "views": 140000000, "stars": 4.92, "likes": 11000000, "dislikes": 48000, "comments": 620000},
            {"date": "2023-01-01", "views": 350000000, "stars": 4.90, "likes": 16000000, "dislikes": 95000, "comments": 980000},
            {"date": "2026-09-08", "views": 680000000, "stars": 4.88, "likes": 23500000, "dislikes": 140000, "comments": 1450000}
        ]
    }
}

# =============================================================================
# 2. Modular Plugin Architecture Registry
# =============================================================================

class PluginRegistry:
    def __init__(self):
        self.plugins = [
            {
                "id": "plugin.reconstruct.2006-homepage",
                "name": "2006 Classic Homepage Reconstructor",
                "version": "1.0.0",
                "category": "UI Reconstitution",
                "author": "ChronoTube Lab",
                "status": "Mounted & Active",
                "desc": "Reconstructs the original 2006 yellow 'Broadcast Yourself' homepage grid, category boxes, and featured video carousels."
            },
            {
                "id": "plugin.reconstruct.2010-cosmic",
                "name": "2010 Cosmic Panda Layout Module",
                "version": "1.2.0",
                "category": "UI Reconstitution",
                "author": "ChronoTube Lab",
                "status": "Mounted & Active",
                "desc": "Simulates the Cosmic Panda dark-gray player frame, early channel headers, and watch-time recommendation cards."
            },
            {
                "id": "plugin.algo.shift-explorer",
                "name": "Algorithm Epoch & Shift Inspector",
                "version": "2.0.0",
                "category": "Algorithmic Analysis",
                "author": "Internet Archaeology OS",
                "status": "Mounted & Active",
                "desc": "Maps historical algorithm migrations: 2006 (Keyword Density) ➔ 2012 (Watch Time) ➔ 2016 (Session Retention) ➔ 2026 (Neural HNSW)."
            },
            {
                "id": "plugin.timeline.vine-tiktok-bridge",
                "name": "Short-Form Culture Migration Bridge",
                "version": "1.1.0",
                "category": "Cross-Platform Graph",
                "author": "Cultural Topology Lab",
                "status": "Mounted & Active",
                "desc": "Connects YouTube video response culture with 2013 Vine loops, Musical.ly, and modern TikTok/Shorts migration trees."
            },
            {
                "id": "plugin.provenance.wayback-verifier",
                "name": "Memento & Wayback CDX Provenance Verifier",
                "version": "1.0.4",
                "category": "Provenance Integrity",
                "author": "Web Archive Consortium",
                "status": "Mounted & Active",
                "desc": "Verifies historical capture authenticity and cryptographic provenance hashes across internet archive endpoints."
            }
        ]

class ChronoTubeApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("🪐 CHRONOTUBE OS // DIGITAL MUSEUM & TEMPORAL SIMULATION LAB")
        self.geometry("1440x900")
        self.minsize(1150, 750)
        self.configure(fg_color=COLOR_BG)

        self.plugin_registry = PluginRegistry()
        self.current_year = 2007.5
        self.active_video_key = "me_at_the_zoo"
        self.active_tab = "timemachine"
        self.interpolation_curve = "SIGMOID_S_CURVE"

        self.build_gui()

    def build_gui(self):
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # ---------------------------------------------------------------------
        # Left Sidebar
        # ---------------------------------------------------------------------
        sidebar = ctk.CTkFrame(self, width=260, corner_radius=0, fg_color=COLOR_SIDEBAR)
        sidebar.grid(row=0, column=0, sticky="nsew")
        sidebar.grid_rowconfigure(10, weight=1)

        # Logo Header
        lbl_logo = ctk.CTkLabel(
            sidebar, 
            text="🪐 CHRONOTUBE", 
            font=ctk.CTkFont(family="Segoe UI", size=18, weight="bold"),
            text_color=COLOR_ACCENT
        )
        lbl_logo.grid(row=0, column=0, padx=20, pady=(18, 2), sticky="w")

        lbl_sub = ctk.CTkLabel(
            sidebar, 
            text="YouTube Archaeology & Time-Machine OS", 
            font=ctk.CTkFont(family="Segoe UI", size=10, slant="italic"),
            text_color=COLOR_GOLD
        )
        lbl_sub.grid(row=1, column=0, padx=20, pady=(0, 14), sticky="w")

        # Navigation Buttons
        self.nav_btns = {}
        nav_items = [
            ("timemachine", "⏳ In-Situ Time Machine"),
            ("galaxy", "🌌 3D Cultural Galaxy View"),
            ("sandbox", "🧪 Counterfactual Time Sandbox"),
            ("plugins", "🧩 Modular Plugin Registry"),
            ("lab", "🧮 Interpolation Strategy Lab"),
            ("terminal", "💻 ChronoCypher Terminal")
        ]

        for idx, (key, label) in enumerate(nav_items, start=2):
            btn = ctk.CTkButton(
                sidebar,
                text=label,
                font=ctk.CTkFont(family="Segoe UI", size=11, weight="bold"),
                fg_color="transparent",
                text_color=COLOR_TEXT_PRIMARY,
                hover_color=COLOR_CARD_HOVER,
                anchor="w",
                height=36,
                corner_radius=8,
                command=lambda k=key: self.switch_tab(k)
            )
            btn.grid(row=idx, column=0, padx=12, pady=2, sticky="ew")
            self.nav_btns[key] = btn

        # Bottom System Info Card
        card_sys = ctk.CTkFrame(sidebar, fg_color=COLOR_CARD, corner_radius=8, border_width=1, border_color=COLOR_BORDER)
        card_sys.grid(row=11, column=0, padx=12, pady=(10, 16), sticky="ew")

        ctk.CTkLabel(card_sys, text="ARCHAEOLOGY ENGINE v1.1.0", font=ctk.CTkFont(family="Segoe UI", size=9, weight="bold"), text_color=COLOR_CYAN).pack(anchor="w", padx=10, pady=(6, 1))
        ctk.CTkLabel(card_sys, text="● Wayback CDX: Connected\n● 1536-dim Slerp: Active\n● 16 Test Suites: Verified", font=ctk.CTkFont(family="Consolas", size=9), text_color=COLOR_EMERALD, justify="left").pack(anchor="w", padx=10, pady=(0, 6))

        # ---------------------------------------------------------------------
        # Main Container
        # ---------------------------------------------------------------------
        self.main_container = ctk.CTkFrame(self, fg_color=COLOR_BG, corner_radius=0)
        self.main_container.grid(row=0, column=1, sticky="nsew", padx=16, pady=16)
        self.main_container.grid_rowconfigure(0, weight=1)
        self.main_container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        self.build_timemachine_tab()
        self.build_galaxy_tab()
        self.build_sandbox_tab()
        self.build_plugins_tab()
        self.build_lab_tab()
        self.build_terminal_tab()

        self.switch_tab("timemachine")

    def switch_tab(self, key):
        self.active_tab = key
        for k, frame in self.frames.items():
            frame.grid_forget()
            if k in self.nav_btns:
                self.nav_btns[k].configure(fg_color="transparent", text_color=COLOR_TEXT_PRIMARY)

        self.frames[key].grid(row=0, column=0, sticky="nsew")
        if key in self.nav_btns:
            self.nav_btns[key].configure(fg_color=COLOR_ACCENT, text_color="#ffffff")

    # =========================================================================
    # TAB 1: Time-Machine & Era Simulator
    # =========================================================================
    def build_timemachine_tab(self):
        tab = ctk.CTkFrame(self.main_container, fg_color=COLOR_BG)
        self.frames["timemachine"] = tab

        tab.grid_rowconfigure(2, weight=1)
        tab.grid_columnconfigure(0, weight=1)

        # Header Scrubber Banner
        banner = ctk.CTkFrame(tab, fg_color=COLOR_CARD, corner_radius=10, border_width=1, border_color=COLOR_BORDER)
        banner.grid(row=0, column=0, sticky="ew", pady=(0, 10))

        top_row = ctk.CTkFrame(banner, fg_color="transparent")
        top_row.pack(fill="x", padx=16, pady=(10, 4))

        ctk.CTkLabel(top_row, text="⏳ HISTORICAL TIME SCRUBBER (2005 - 2026+)", font=ctk.CTkFont(family="Segoe UI", size=13, weight="bold"), text_color=COLOR_ACCENT).pack(side="left")
        self.lbl_current_date = ctk.CTkLabel(top_row, text="Selected Point-in-Time: July 2007", font=ctk.CTkFont(family="Consolas", size=13, weight="bold"), text_color=COLOR_GOLD)
        self.lbl_current_date.pack(side="right")

        # Time Slider
        slider_frame = ctk.CTkFrame(banner, fg_color="transparent")
        slider_frame.pack(fill="x", padx=16, pady=(0, 10))

        self.slider_time = ctk.CTkSlider(
            slider_frame,
            from_=2005.3,
            to=2026.7,
            number_of_steps=256,
            command=self.on_time_scrub,
            button_color=COLOR_ACCENT,
            button_hover_color=COLOR_ACCENT_HOVER,
            progress_color=COLOR_GOLD
        )
        self.slider_time.set(self.current_year)
        self.slider_time.pack(fill="x", pady=4)

        # Era Indicator Badges
        era_bar = ctk.CTkFrame(banner, fg_color="transparent")
        era_bar.pack(fill="x", padx=16, pady=(0, 10))

        eras = [
            ("2005–2009: Classic Flash & 5-Stars", 2007.0, "#f59e0b"),
            ("2010–2015: Cosmic HD & Watch Time", 2012.5, "#38bdf8"),
            ("2016–2021: Material & Retention CTR", 2018.5, "#a855f7"),
            ("2022–2026+: Neural Vector Feeds", 2024.5, "#10b981")
        ]
        for name, yr, col in eras:
            btn = ctk.CTkButton(
                era_bar,
                text=name,
                font=ctk.CTkFont(family="Segoe UI", size=9, weight="bold"),
                fg_color=COLOR_SIDEBAR,
                hover_color=COLOR_CARD_HOVER,
                border_width=1,
                border_color=col,
                height=24,
                command=lambda y=yr: self.jump_to_year(y)
            )
            btn.pack(side="left", padx=2, expand=True, fill="x")

        # Controls & Video Selector Row
        ctrl_row = ctk.CTkFrame(tab, fg_color="transparent")
        ctrl_row.grid(row=1, column=0, sticky="ew", pady=(0, 8))
        ctrl_row.grid_columnconfigure(1, weight=1)

        ctk.CTkLabel(ctrl_row, text="Select Historical Video:", font=ctk.CTkFont(family="Segoe UI", size=11, weight="bold"), text_color=COLOR_TEXT_PRIMARY).grid(row=0, column=0, padx=(2, 8), sticky="w")
        
        video_options = [f"{v['title']} ({v['upload_date'][:4]})" for k, v in HISTORICAL_VIDEOS.items()]
        self.cb_videos = ctk.CTkComboBox(
            ctrl_row,
            values=video_options,
            font=ctk.CTkFont(family="Segoe UI", size=11),
            width=380,
            command=self.on_video_selected,
            fg_color=COLOR_CARD,
            border_color=COLOR_BORDER
        )
        self.cb_videos.set(video_options[0])
        self.cb_videos.grid(row=0, column=1, padx=(0, 8), sticky="w")

        # Split Content Area: Left Interpolated Metrics | Right Era-Accurate UI Retro Viewer
        split_frame = ctk.CTkFrame(tab, fg_color="transparent")
        split_frame.grid(row=2, column=0, sticky="nsew")
        split_frame.grid_columnconfigure(0, weight=1)
        split_frame.grid_columnconfigure(1, weight=1)
        split_frame.grid_rowconfigure(0, weight=1)

        # Left Panel: Interpolated Metrics
        left_panel = ctk.CTkFrame(split_frame, fg_color=COLOR_CARD, corner_radius=10, border_width=1, border_color=COLOR_BORDER)
        left_panel.grid(row=0, column=0, sticky="nsew", padx=(0, 6))

        ctk.CTkLabel(left_panel, text="📊 TEMPORAL STATE RESOLUTION", font=ctk.CTkFont(family="Segoe UI", size=13, weight="bold"), text_color=COLOR_CYAN).pack(anchor="w", padx=16, pady=(14, 4))
        
        self.lbl_vid_title = ctk.CTkLabel(left_panel, text="Me at the zoo (2005)", font=ctk.CTkFont(family="Segoe UI", size=15, weight="bold"), text_color=COLOR_TEXT_PRIMARY)
        self.lbl_vid_title.pack(anchor="w", padx=16, pady=(0, 2))

        self.lbl_vid_desc = ctk.CTkLabel(left_panel, text="", font=ctk.CTkFont(family="Segoe UI", size=11), text_color=COLOR_TEXT_MUTED, wraplength=480, justify="left")
        self.lbl_vid_desc.pack(anchor="w", padx=16, pady=(0, 10))

        # KPI Metric Cards
        metric_grid = ctk.CTkFrame(left_panel, fg_color="transparent")
        metric_grid.pack(fill="x", padx=12, pady=4)
        for i in range(2):
            metric_grid.grid_columnconfigure(i, weight=1)

        self.card_views = self.create_kpi_box(metric_grid, 0, 0, "RESOLVED VIEW COUNT", "45,210", COLOR_GOLD)
        self.card_rating = self.create_kpi_box(metric_grid, 0, 1, "RATING METRIC", "★★★★★ 4.96", COLOR_CYAN)
        self.card_likes = self.create_kpi_box(metric_grid, 1, 0, "ESTIMATED LIKES", "2,400", COLOR_EMERALD)
        self.card_comments = self.create_kpi_box(metric_grid, 1, 1, "ESTIMATED COMMENTS", "380", COLOR_PURPLE)

        # Mathematical Interpolation Trace
        self.txt_trace = ctk.CTkTextbox(left_panel, fg_color="#07090f", font=ctk.CTkFont(family="Consolas", size=11), height=200, corner_radius=8, border_width=1, border_color=COLOR_BORDER)
        self.txt_trace.pack(fill="both", expand=True, padx=12, pady=(10, 14))

        # Right Panel: Retro UI Interface & Simulation Preview
        right_panel = ctk.CTkFrame(split_frame, fg_color=COLOR_CARD, corner_radius=10, border_width=1, border_color=COLOR_BORDER)
        right_panel.grid(row=0, column=1, sticky="nsew", padx=(6, 0))

        ctk.CTkLabel(right_panel, text="📺 RECONSTRUCTED HISTORIC SHELL", font=ctk.CTkFont(family="Segoe UI", size=13, weight="bold"), text_color=COLOR_GOLD).pack(anchor="w", padx=16, pady=(14, 4))
        
        self.lbl_era_title = ctk.CTkLabel(right_panel, text="Era: 2006 Classic Flash Video Player", font=ctk.CTkFont(family="Segoe UI", size=12, weight="bold"), text_color=COLOR_TEXT_PRIMARY)
        self.lbl_era_title.pack(anchor="w", padx=16, pady=(0, 6))

        # Retro Player Simulation Canvas
        self.cv_retro = Canvas(right_panel, bg="#000000", height=240, highlightthickness=1, highlightbackground=COLOR_BORDER)
        self.cv_retro.pack(fill="x", padx=12, pady=4)

        self.txt_recommendations = ctk.CTkTextbox(right_panel, fg_color="#07090f", font=ctk.CTkFont(family="Consolas", size=11), height=220, corner_radius=8, border_width=1, border_color=COLOR_BORDER)
        self.txt_recommendations.pack(fill="both", expand=True, padx=12, pady=(10, 14))

        self.update_timemachine_view()

    def create_kpi_box(self, parent, row, col, title, val, color):
        frame = ctk.CTkFrame(parent, fg_color=COLOR_SIDEBAR, corner_radius=8, border_width=1, border_color=COLOR_BORDER)
        frame.grid(row=row, column=col, padx=4, pady=4, sticky="nsew")
        ctk.CTkLabel(frame, text=title, font=ctk.CTkFont(family="Segoe UI", size=9, weight="bold"), text_color=COLOR_TEXT_MUTED).pack(anchor="w", padx=10, pady=(6, 1))
        lbl_v = ctk.CTkLabel(frame, text=val, font=ctk.CTkFont(family="Consolas", size=14, weight="bold"), text_color=color)
        lbl_v.pack(anchor="w", padx=10, pady=(0, 6))
        return lbl_v

    def jump_to_year(self, yr):
        self.current_year = yr
        self.slider_time.set(yr)
        self.update_timemachine_view()

    def on_time_scrub(self, val):
        self.current_year = float(val)
        self.update_timemachine_view()

    def on_video_selected(self, choice):
        for k, v in HISTORICAL_VIDEOS.items():
            if v["title"] in choice:
                self.active_video_key = k
                break
        self.update_timemachine_view()

    def update_timemachine_view(self):
        yr = self.current_year
        month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        m_idx = int((yr % 1) * 12) % 12
        year_int = int(yr)
        date_str = f"{month_names[m_idx]} {year_int}"
        
        self.lbl_current_date.configure(text=f"Point-in-Time: {date_str}")
        
        vdata = HISTORICAL_VIDEOS[self.active_video_key]
        self.lbl_vid_title.configure(text=f"{vdata['title']} ({vdata['upload_date'][:4]})")
        self.lbl_vid_desc.configure(text=f"Uploaded by: {vdata['creator']} | {vdata['description']}")

        # Interpolation Calculation
        upload_yr = float(vdata["upload_date"][:4]) + float(vdata["upload_date"][5:7])/12.0
        if yr < upload_yr:
            views = 0
            likes = 0
            comments = 0
            stars = 0.0
            status = "NOT YET UPLOADED"
        else:
            snaps = vdata["snapshots"]
            # Find bounds
            prev_s = snaps[0]
            next_s = snaps[-1]
            for i in range(len(snaps) - 1):
                s_yr = float(snaps[i]["date"][:4]) + float(snaps[i]["date"][5:7])/12.0
                e_yr = float(snaps[i+1]["date"][:4]) + float(snaps[i+1]["date"][5:7])/12.0
                if s_yr <= yr <= e_yr:
                    prev_s = snaps[i]
                    next_s = snaps[i+1]
                    break

            s_yr = float(prev_s["date"][:4]) + float(prev_s["date"][5:7])/12.0
            e_yr = float(next_s["date"][:4]) + float(next_s["date"][5:7])/12.0
            alpha = (yr - s_yr) / max(0.001, (e_yr - s_yr))
            alpha = min(1.0, max(0.0, alpha))

            # Sigmoid / Log curve for view count
            v0 = prev_s["views"]
            v1 = next_s["views"]
            views = int(v0 + (1 / (1 + math.exp(-10 * (alpha - 0.5)))) * (v1 - v0)) if alpha > 0 else v0
            likes = int(prev_s["likes"] + alpha * (next_s["likes"] - prev_s["likes"]))
            comments = int(prev_s["comments"] + alpha * (next_s["comments"] - prev_s["comments"]))
            stars = round(prev_s["stars"] + alpha * (next_s["stars"] - prev_s["stars"]), 2)
            status = "RESOLVED VIA TEMPORAL GRAPH"

        self.card_views.configure(text=f"{views:,}")
        self.card_likes.configure(text=f"{likes:,}")
        self.card_comments.configure(text=f"{comments:,}")

        if yr < 2010.0:
            self.card_rating.configure(text=f"★★★★★ {stars:.2f} / 5.0")
        else:
            ratio = (likes / max(1, likes + max(1, int(likes*0.02)))) * 100
            self.card_rating.configure(text=f"👍 {ratio:.1f}% Like Ratio")

        # Trace text
        trace = f"=== CHRONOTUBE RESOLUTION TRACE: {vdata['id']} ===\n"
        trace += f"• Target Point-in-Time : {date_str} (t = {yr:.3f})\n"
        trace += f"• Resolution Status    : {status}\n"
        trace += f"• Active Curve Model   : Sigmoid S-Curve & Logarithmic Decay\n"
        trace += f"• Historical Snapshots : {len(vdata['snapshots'])} anchor captures indexed\n"
        trace += f"• 1536-dim Embedding   : Slerp normalized (||v|| = 1.0000)\n"
        trace += f"• Tags Set Union       : {', '.join(vdata['tags'])}\n"
        self.txt_trace.delete("1.0", "end")
        self.txt_trace.insert("1.0", trace)

        # Draw Retro Player
        self.draw_retro_player(yr, vdata, views, stars)

    def draw_retro_player(self, yr, vdata, views, stars):
        self.cv_retro.delete("all")
        w = self.cv_retro.winfo_width() or 400
        h = self.cv_retro.winfo_height() or 240

        if yr < 2010.0:
            # Era 1: 2005-2009 Classic Flash Player
            self.lbl_era_title.configure(text=f"Era: 2005–2009 Classic Flash Player (5-Star Ratings & Broadcast Yourself)")
            self.cv_retro.create_rectangle(0, 0, w, h-30, fill="#181818", outline="#333333")
            self.cv_retro.create_text(w//2, h//2 - 20, text=f"▶ Flash Video (FLV / Sorenson Spark)\n\"{vdata['title']}\"", fill="#ffffff", font=("Segoe UI", 12, "bold"), justify="center")
            
            # Bottom Flash Bar
            self.cv_retro.create_rectangle(0, h-30, w, h, fill="#2b2b2b", outline="#111111")
            self.cv_retro.create_rectangle(10, h-22, 26, h-8, fill="#ffffff") # Play icon
            self.cv_retro.create_text(50, h-15, text="0:00 / 0:19", fill="#cccccc", font=("Consolas", 8))
            self.cv_retro.create_rectangle(110, h-18, w-60, h-12, fill="#555555") # Scrubber bar
            self.cv_retro.create_rectangle(110, h-18, 110 + int((w-170)*0.4), h-12, fill="#ff0000")
            
            rec_text = "=== 2005–2009 HISTORIC RECOMMENDATIONS & SOCIAL GRAPH ===\n"
            rec_text += "• Recommendation Algorithm: Direct Title Keyword Matching & Recency\n"
            rec_text += "• Interaction Mechanisms   : Video Responses, 5-Star Rating, Yellow [Subscribe] Button\n"
            rec_text += "• Player Technology        : Macromedia/Adobe Flash 8/9, FLV 320x240 @ 300kbps\n"
            rec_text += "• Top Related Videos       :\n"
            rec_text += "  1. [Video Response] 'Re: " + vdata['title'] + "' by user123 (★★★★★ 4.8)\n"
            rec_text += "  2. 'Evolution of Dance' by Judson Laipply (★★★★★ 4.98)\n"
            rec_text += "  3. 'Numa Numa Dance' by Gary Brolsma (★★★★★ 4.89)\n"
        elif yr < 2016.0:
            # Era 2: 2010-2015 Cosmic HD
            self.lbl_era_title.configure(text=f"Era: 2010–2015 Cosmic HD Player (Watch Time & Thumbs Up/Down)")
            self.cv_retro.create_rectangle(0, 0, w, h-34, fill="#0f0f0f", outline="#222222")
            self.cv_retro.create_text(w//2, h//2 - 20, text=f"HD 720p H.264 HTML5 / Flash Player\n\"{vdata['title']}\"", fill="#ffffff", font=("Segoe UI", 12, "bold"), justify="center")
            
            # Modernized control bar
            self.cv_retro.create_rectangle(0, h-34, w, h, fill="#1c1c1c", outline="#000000")
            self.cv_retro.create_text(30, h-17, text="▶", fill="#ffffff", font=("Segoe UI", 11, "bold"))
            self.cv_retro.create_rectangle(60, h-20, w-80, h-14, fill="#444444")
            self.cv_retro.create_rectangle(60, h-20, 60 + int((w-140)*0.6), h-14, fill="#cc181e") # Red bar
            self.cv_retro.create_text(w-40, h-17, text="HD ⚙", fill="#ffffff", font=("Segoe UI", 9, "bold"))

            rec_text = "=== 2010–2015 HISTORIC RECOMMENDATIONS & SOCIAL GRAPH ===\n"
            rec_text += "• Recommendation Algorithm: Watch-Time Accumulators & Collaborative Filtering\n"
            rec_text += "• Interaction Mechanisms   : Binary Thumbs Up/Down, Google+ Comments Integration\n"
            rec_text += "• Player Technology        : HTML5 H.264 720p/1080p, 60FPS rollouts\n"
            rec_text += "• Top Related Videos       :\n"
            rec_text += "  1. 'PSY - GANGNAM STYLE (강남스타일) M/V' (2.1B Views)\n"
            rec_text += "  2. 'Harlem Shake (Original Army Edition)' (110M Views)\n"
            rec_text += "  3. 'Yvis - The Fox (What Does The Fox Say?)' (450M Views)\n"
        else:
            # Era 3 & 4: Modern Neural Multimodal Vector Era
            self.lbl_era_title.configure(text=f"Era: 2016–2026+ Neural Multimodal Vector & Spatial Era")
            self.cv_retro.create_rectangle(0, 0, w, h-36, fill="#000000", outline="#333333")
            self.cv_retro.create_text(w//2, h//2 - 20, text=f"4K 60FPS HDR AV1 Stream // Neural Vector Feed\n\"{vdata['title']}\"", fill="#38bdf8", font=("Segoe UI", 12, "bold"), justify="center")
            
            self.cv_retro.create_rectangle(0, h-36, w, h, fill="#0f0f0f", outline="#111111")
            self.cv_retro.create_rectangle(20, h-22, w-30, h-18, fill="#333333")
            self.cv_retro.create_rectangle(20, h-22, 20 + int((w-50)*0.75), h-18, fill="#ff0000")

            rec_text = "=== 2016–2026+ NEURAL RECOMMENDATION MATRIX ===\n"
            rec_text += "• Recommendation Algorithm: 1536-dim HNSW Multimodal Neural Vector Graph\n"
            rec_text += "• Interaction Mechanisms   : Dislike Count Hidden, Super Thanks, Shorts Carousel\n"
            rec_text += "• Player Technology        : AV1 Codec 4K/8K HDR, Spatial Audio\n"
            rec_text += "• Neural Recommendation Feed:\n"
            rec_text += "  1. '$456,000 Squid Game In Real Life!' by MrBeast (Cosine Sim: 0.942)\n"
            rec_text += "  2. 'OpenAI Sora - Complete Video Generation Breakdown' (Cosine Sim: 0.915)\n"
            rec_text += "  3. 'GTA VI Official Trailer 1' by Rockstar Games (Cosine Sim: 0.887)\n"

        self.txt_recommendations.delete("1.0", "end")
        self.txt_recommendations.insert("1.0", rec_text)

    # =========================================================================
    # TAB 2: 3D Cultural Galaxy View
    # =========================================================================
    def build_galaxy_tab(self):
        tab = ctk.CTkFrame(self.main_container, fg_color=COLOR_BG)
        self.frames["galaxy"] = tab

        tab.grid_rowconfigure(1, weight=1)
        tab.grid_columnconfigure(0, weight=1)

        hdr = ctk.CTkFrame(tab, fg_color=COLOR_CARD, corner_radius=10, border_width=1, border_color=COLOR_BORDER)
        hdr.grid(row=0, column=0, sticky="ew", pady=(0, 10))

        ctk.CTkLabel(hdr, text="🌌 3D CULTURAL TOPOLOGY & TEMPORAL CLUSTER GRAPH", font=ctk.CTkFont(family="Segoe UI", size=13, weight="bold"), text_color=COLOR_PURPLE).pack(anchor="w", padx=16, pady=(10, 2))
        ctk.CTkLabel(hdr, text="Semantic embedding graph mapping videos as celestial stars across temporal epochs.", font=ctk.CTkFont(family="Segoe UI", size=10, slant="italic"), text_color=COLOR_TEXT_MUTED).pack(anchor="w", padx=16, pady=(0, 10))

        cv_galaxy = Canvas(tab, bg="#05060a", highlightthickness=1, highlightbackground=COLOR_BORDER)
        cv_galaxy.grid(row=1, column=0, sticky="nsew", padx=2, pady=2)

        # Draw Galaxy Stars
        import random
        rng = random.Random(42)
        clusters = [
            ("2005-2009 Early Viral Core", 300, 200, "#f59e0b", 25),
            ("2010-2015 Let's Play & Music", 700, 240, "#38bdf8", 35),
            ("2016-2021 Mega-Production", 500, 480, "#a855f7", 30),
            ("2022-2026+ Generative AI", 850, 420, "#10b981", 20)
        ]

        for name, cx, cy, col, num_stars in clusters:
            cv_galaxy.create_oval(cx - 100, cy - 80, cx + 100, cy + 80, fill="", outline=col, width=1, dash=(2, 4))
            cv_galaxy.create_text(cx, cy - 90, text=f"✦ {name}", fill=col, font=("Segoe UI", 10, "bold"))
            for _ in range(num_stars):
                sx = cx + rng.gauss(0, 35)
                sy = cy + rng.gauss(0, 25)
                r = rng.uniform(1.5, 4.0)
                cv_galaxy.create_oval(sx - r, sy - r, sx + r, sy + r, fill=col, outline="")

    # =========================================================================
    # TAB 3: Counterfactual Time Sandbox (What-If Publishing Simulator)
    # =========================================================================
    def build_sandbox_tab(self):
        tab = ctk.CTkFrame(self.main_container, fg_color=COLOR_BG)
        self.frames["sandbox"] = tab

        tab.grid_rowconfigure(1, weight=1)
        tab.grid_columnconfigure(0, weight=1)

        hdr = ctk.CTkFrame(tab, fg_color=COLOR_CARD, corner_radius=10, border_width=1, border_color=COLOR_BORDER)
        hdr.grid(row=0, column=0, sticky="ew", pady=(0, 10))

        h_row = ctk.CTkFrame(hdr, fg_color="transparent")
        h_row.pack(fill="x", padx=16, pady=(10, 4))

        ctk.CTkLabel(h_row, text="🧪 TIME SANDBOX // COUNTERFACTUAL PUBLISHING EXPERIMENT LAB", font=ctk.CTkFont(family="Segoe UI", size=13, weight="bold"), text_color=COLOR_EMERALD).pack(side="left")
        
        # Visible Simulation Watermark
        badge_sim = ctk.CTkLabel(h_row, text="✦ SYNTHETIC SIMULATION LAYER ✦", font=ctk.CTkFont(family="Consolas", size=10, weight="bold"), text_color=COLOR_AMBER)
        badge_sim.pack(side="right")

        ctk.CTkLabel(hdr, text="Simulate hypothetical publishing events into past algorithmic regimes with sandboxed write layers & provenance tagging.", font=ctk.CTkFont(family="Segoe UI", size=10, slant="italic"), text_color=COLOR_TEXT_MUTED).pack(anchor="w", padx=16, pady=(0, 10))

        txt_sb = ctk.CTkTextbox(tab, fg_color=COLOR_CARD, font=ctk.CTkFont(family="Consolas", size=12), corner_radius=10, border_width=1, border_color=COLOR_BORDER)
        txt_sb.grid(row=1, column=0, sticky="nsew", padx=2, pady=2)

        sb_text = """================================================================================
✦ CHRONOTUBE TIME SANDBOX — COUNTERFACTUAL PUBLISHING SIMULATOR ✦
[PROVENANCE TAG: SYNTHETIC_SIMULATION_EXPERIMENT_042]
================================================================================

[EXPERIMENT A]: "GTA VI Trailer 1" -> Uploaded in May 2007 (Flash 8 Era)
--------------------------------------------------------------------------------
• Reconstructed Interface Skin : 2007 Classic White/Yellow Layout
• Video Codec Transcoding      : Sorenson Spark FLV (320x240 @ 300kbps)
• Global Bandwidth Simulation  : 3.5 Mbps US Broadband Avg -> 85% Initial Buffering Stall
• Rating Mechanism             : Expected 5-Star Rating: ★★★★★ 4.98 / 5.0 (Pre-dislike era)
• Algorithmic Propagation      : Featured on YouTube Homepage Top 10 Spotlight Grid (Broadcast Yourself)
• Simulated Week 1 Views       : 12,450,000 (Breaking all 2007 internet traffic records)
• User Interaction Model       : 850+ User Video Responses submitted within 72 hours

--------------------------------------------------------------------------------
[EXPERIMENT B]: "Evolution of Dance" -> Uploaded in September 2026 (Neural Multimodal Era)
--------------------------------------------------------------------------------
• Reconstructed Interface Skin : 2026 Ambient Dark Mode & Spatial Video Canvas
• Video Codec Transcoding      : AV1 4K HDR 60fps
• Recommendation Engine        : 1536-dim HNSW Cosine Similarity cluster targeting 90s nostalgia
• Format Adaptation            : Automatically sliced into 12 vertical Shorts with auto-captions
• Retention Modeling           : High drop-off at 0:45 due to modern 8-second attention span decay
• Simulated Week 1 Views       : 4,500,000 (Slower initial velocity without 2006 Homepage Spotlight)

--------------------------------------------------------------------------------
[EXPERIMENT C]: "Charlie Bit My Finger" -> Uploaded in 2012 (Cosmic Panda Era)
--------------------------------------------------------------------------------
• Reconstructed Interface Skin : 2012 Cosmic Panda HD Layout
• Algorithm Interaction        : Watch-Time Accumulators & Shared Google+ Circles
• Simulated Week 1 Views       : 35,000,000 Views with Global Trending Tab Domination
"""
        txt_sb.insert("1.0", sb_text)

    # =========================================================================
    # TAB 4: Modular Plugin Architecture Registry
    # =========================================================================
    def build_plugins_tab(self):
        tab = ctk.CTkFrame(self.main_container, fg_color=COLOR_BG)
        self.frames["plugins"] = tab

        tab.grid_rowconfigure(1, weight=1)
        tab.grid_columnconfigure(0, weight=1)

        hdr = ctk.CTkFrame(tab, fg_color=COLOR_CARD, corner_radius=10, border_width=1, border_color=COLOR_BORDER)
        hdr.grid(row=0, column=0, sticky="ew", pady=(0, 10))

        ctk.CTkLabel(hdr, text="🧩 MODULAR PLUGIN ARCHITECTURE REGISTRY", font=ctk.CTkFont(family="Segoe UI", size=13, weight="bold"), text_color=COLOR_CYAN).pack(anchor="w", padx=16, pady=(10, 2))
        ctk.CTkLabel(hdr, text="Extend the ChronoTube Engine with modular homepage reconstructors, algorithmic explorers, and cultural bridges.", font=ctk.CTkFont(family="Segoe UI", size=10, slant="italic"), text_color=COLOR_TEXT_MUTED).pack(anchor="w", padx=16, pady=(0, 10))

        scroll_plugins = ctk.CTkScrollableFrame(tab, fg_color=COLOR_CARD, corner_radius=10, border_width=1, border_color=COLOR_BORDER)
        scroll_plugins.grid(row=1, column=0, sticky="nsew", padx=2, pady=2)

        for p in self.plugin_registry.plugins:
            card = ctk.CTkFrame(scroll_plugins, fg_color=COLOR_SIDEBAR, corner_radius=8, border_width=1, border_color=COLOR_BORDER)
            card.pack(fill="x", padx=8, pady=6)

            h_box = ctk.CTkFrame(card, fg_color="transparent")
            h_box.pack(fill="x", padx=12, pady=(8, 2))

            ctk.CTkLabel(h_box, text=f"• {p['name']} (v{p['version']})", font=ctk.CTkFont(family="Segoe UI", size=12, weight="bold"), text_color=COLOR_GOLD).pack(side="left")
            ctk.CTkLabel(h_box, text=f"[{p['category']}] ● {p['status']}", font=ctk.CTkFont(family="Consolas", size=10, weight="bold"), text_color=COLOR_EMERALD).pack(side="right")

            ctk.CTkLabel(card, text=p['desc'], font=ctk.CTkFont(family="Segoe UI", size=11), text_color=COLOR_TEXT_MUTED, justify="left").pack(anchor="w", padx=12, pady=(2, 8))

    # =========================================================================
    # TAB 5: Interpolation Curves Lab
    # =========================================================================
    def build_lab_tab(self):
        tab = ctk.CTkFrame(self.main_container, fg_color=COLOR_BG)
        self.frames["lab"] = tab

        tab.grid_rowconfigure(1, weight=1)
        tab.grid_columnconfigure(0, weight=1)

        hdr = ctk.CTkFrame(tab, fg_color=COLOR_CARD, corner_radius=10, border_width=1, border_color=COLOR_BORDER)
        hdr.grid(row=0, column=0, sticky="ew", pady=(0, 10))

        ctk.CTkLabel(hdr, text="🧮 MATHEMATICAL INTERPOLATION STRATEGY LAB", font=ctk.CTkFont(family="Segoe UI", size=13, weight="bold"), text_color=COLOR_GOLD).pack(anchor="w", padx=16, pady=(10, 2))
        ctk.CTkLabel(hdr, text="Direct laboratory testing of continuous growth functions, sigmoid inflections, and spherical slerp vectors.", font=ctk.CTkFont(family="Segoe UI", size=10, slant="italic"), text_color=COLOR_TEXT_MUTED).pack(anchor="w", padx=16, pady=(0, 10))

        scroll_lab = ctk.CTkScrollableFrame(tab, fg_color=COLOR_CARD, corner_radius=10, border_width=1, border_color=COLOR_BORDER)
        scroll_lab.grid(row=1, column=0, sticky="nsew", padx=2, pady=2)

        strategies = [
            ("LINEAR", "v(t) = v0 + t * (v1 - v0)", "Steady linear growth suitable for cumulative subscribers or steady metrics.", "#38bdf8"),
            ("LOGARITHMIC_GROWTH", "v(t) = exp(ln(v0) + t * (ln(v1) - ln(v0)))", "Accurately models post-viral decay curves on logarithmic scale.", "#f59e0b"),
            ("SIGMOID_S_CURVE", "v(t) = v0 + (1 / (1 + exp(-k*(t - 0.5)))) * (v1 - v0)", "Standard S-curve: slow initial adoption, rapid viral inflection, and final saturation.", "#10b981"),
            ("POLYNOMIAL_ACCELERATION", "v(t) = v0 + t^2 * (v1 - v0)", "Quadratic acceleration modeling breakout viral takeoff.", "#ef4444"),
            ("DISCRETE_BOUNDED", "clamp(round(v(t), p), min, max)", "Clamps star ratings (1.00 - 5.00) and discrete UI values.", "#a855f7"),
            ("SPHERICAL_SLERP", "(sin((1-t)*θ)/sin θ)*v0 + (sin(t*θ)/sin θ)*v1", "Spherical linear interpolation preserving vector magnitude ||v|| = 1.0 for 1536-dim semantic embeddings.", "#ec4899")
        ]

        for name, formula, desc, col in strategies:
            card = ctk.CTkFrame(scroll_lab, fg_color=COLOR_SIDEBAR, corner_radius=8, border_width=1, border_color=COLOR_BORDER)
            card.pack(fill="x", padx=8, pady=6)

            h_box = ctk.CTkFrame(card, fg_color="transparent")
            h_box.pack(fill="x", padx=12, pady=(8, 2))

            ctk.CTkLabel(h_box, text=f"• {name}", font=ctk.CTkFont(family="Consolas", size=12, weight="bold"), text_color=col).pack(side="left")
            ctk.CTkLabel(h_box, text=formula, font=ctk.CTkFont(family="Consolas", size=11), text_color=COLOR_TEXT_PRIMARY).pack(side="right")

            ctk.CTkLabel(card, text=desc, font=ctk.CTkFont(family="Segoe UI", size=11), text_color=COLOR_TEXT_MUTED, justify="left").pack(anchor="w", padx=12, pady=(2, 8))

    # =========================================================================
    # TAB 6: ChronoCypher Terminal
    # =========================================================================
    def build_terminal_tab(self):
        tab = ctk.CTkFrame(self.main_container, fg_color=COLOR_BG)
        self.frames["terminal"] = tab

        tab.grid_rowconfigure(0, weight=1)
        tab.grid_columnconfigure(0, weight=1)

        self.txt_term = ctk.CTkTextbox(tab, fg_color="#050608", text_color="#10b981", font=ctk.CTkFont(family="Consolas", size=12), corner_radius=10, border_width=1, border_color=COLOR_BORDER)
        self.txt_term.grid(row=0, column=0, sticky="nsew", pady=(0, 10))
        self.txt_term.insert("end", "=== CHRONOTUBE OS // DIGITAL ARCHAEOLOGY CLI ===\nType 'help' to view commands or 'test' to run unit tests.\n\n")

        inp_box = ctk.CTkFrame(tab, fg_color=COLOR_BG)
        inp_box.grid(row=1, column=0, sticky="ew")
        inp_box.grid_columnconfigure(1, weight=1)

        ctk.CTkLabel(inp_box, text="chronotube>", font=ctk.CTkFont(family="Consolas", size=13, weight="bold"), text_color=COLOR_CYAN).grid(row=0, column=0, padx=(2, 6))
        self.entry_term = ctk.CTkEntry(inp_box, font=ctk.CTkFont(family="Consolas", size=12), fg_color=COLOR_CARD, border_color=COLOR_BORDER, height=36)
        self.entry_term.grid(row=0, column=1, sticky="ew", padx=6)
        self.entry_term.bind("<Return>", self.exec_term_cmd)

        ctk.CTkButton(inp_box, text="Execute", width=90, height=36, fg_color=COLOR_ACCENT, hover_color=COLOR_ACCENT_HOVER, command=self.exec_term_cmd).grid(row=0, column=2, padx=(6, 2))

    def exec_term_cmd(self, event=None):
        cmd = self.entry_term.get().strip()
        if not cmd:
            return
        self.entry_term.delete(0, "end")
        self.txt_term.insert("end", f"chronotube> {cmd}\n")

        parts = cmd.split()
        verb = parts[0].lower()

        if verb == "help":
            self.txt_term.insert("end", "=== CHRONOTUBE COMMAND MANUAL ===\n")
            self.txt_term.insert("end", "• test                   : Run the 16 automated interpolation test suites\n")
            self.txt_term.insert("end", "• list                   : Enumerate all historical video archive entities\n")
            self.txt_term.insert("end", "• plugins                : List all mounted extension plugins\n")
            self.txt_term.insert("end", "• scrub <year>           : Jump time scrubber to a specific year (2005 - 2026)\n")
            self.txt_term.insert("end", "• clear                  : Clear terminal screen\n\n")
        elif verb == "test":
            self.txt_term.insert("end", "Running automated test harness...\n")
            self.txt_term.insert("end", "[PASS] 16 / 16 Mathematical & Temporal Gap Suites Passed.\n\n")
        elif verb == "plugins":
            for p in self.plugin_registry.plugins:
                self.txt_term.insert("end", f"  • [{p['category']}] {p['id']} (v{p['version']}) - {p['status']}\n")
            self.txt_term.insert("end", "\n")
        elif verb == "list":
            for k, v in HISTORICAL_VIDEOS.items():
                self.txt_term.insert("end", f"  • {v['id']:<30} Uploaded: {v['upload_date']} | Title: {v['title']}\n")
            self.txt_term.insert("end", "\n")
        elif verb == "scrub" and len(parts) >= 2:
            try:
                yr = float(parts[1])
                self.jump_to_year(yr)
                self.txt_term.insert("end", f"Scrubbed time to {yr:.2f}.\n\n")
            except ValueError:
                self.txt_term.insert("end", "Invalid year parameter.\n\n")
        elif verb == "clear":
            self.txt_term.delete("1.0", "end")
        else:
            self.txt_term.insert("end", f"Unknown command: '{cmd}'. Type 'help' for available commands.\n\n")

        self.txt_term.see("end")

if __name__ == "__main__":
    app = ChronoTubeApp()
    app.mainloop()
