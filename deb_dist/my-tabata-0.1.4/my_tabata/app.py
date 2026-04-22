# imports
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from .config import load_config
import os
from just_playback import Playback

# Default Fallback Values
SOFT_DEFAULT = 20  # seconds
HARD_DEFAULT = 10  # seconds
STEPS_DEFAULT = 8  # cycles


class Application:
    def __init__(self, root, soft_d, hard_d, steps_d):
        """
        Initialize the Tabata Application.
        :param root: The ttkbootstrap main window.
        :param soft_d, hard_d, steps_d: Default values if config is missing.
        """
        self.lbl_big_timer = None
        self.lbl_status = None
        self.player = Playback()

        # Load configuration from external file or use defaults
        soft_f, hard_f, steps_f = load_config(soft_d, hard_d, steps_d)
        print(f"Config loaded: soft={soft_f}s, hard={hard_f}s, steps={steps_f}")

        self.root = root
        self.soft = soft_f
        self.hard = hard_f
        self.steps = steps_f

        # State Variables
        self.is_running = False
        self.timer_id = None  # Stores the .after() callback to allow cancellation
        self.current_time = 0
        self.mode = "HARD"  # "HARD" = Active, "SOFT" = Rest
        self.current_step = 1

        # Window Settings
        root.geometry("420x650")
        root.title("Tabata Timer Pro")
        root.resizable(False, False)

        self.setup_ui()

    def setup_ui(self):
        """Build the graphical user interface."""
        container = ttk.Frame(self.root, padding=15)
        container.pack(fill=BOTH, expand=True)

        # --- VISUAL TIMER DISPLAY ---
        self.lbl_status = ttk.Label(container, text="READY", font=("Helvetica", 15, "bold"), bootstyle=SECONDARY)
        self.lbl_status.pack(pady=(10, 0))

        self.lbl_big_timer = ttk.Label(container, text="00", font=("Helvetica", 60, "bold"), bootstyle=SUCCESS)
        self.lbl_big_timer.pack(pady=10)

        self.lbl_round_info = ttk.Label(container, text=f"Round: 0 / {self.steps}", font=("Helvetica", 12))
        self.lbl_round_info.pack(pady=5)

        ttk.Separator(container, orient=HORIZONTAL).pack(fill=X, pady=15)

        # --- MANAGEMENT BUTTONS ---
        ttk.Label(container, text="Timer Control:").pack()
        btn_mgmt = ttk.Frame(container)
        btn_mgmt.pack(fill=X, pady=10)

        ttk.Button(btn_mgmt, text="START", bootstyle=SUCCESS, command=self.start).pack(side=LEFT, expand=True, fill=X,
                                                                                       padx=2)
        ttk.Button(btn_mgmt, text="PAUSE", bootstyle=PRIMARY, command=self.pause).pack(side=LEFT, expand=True, fill=X,
                                                                                       padx=2)
        ttk.Button(btn_mgmt, text="RESTART", bootstyle=INFO, command=self.restart).pack(side=LEFT, expand=True, fill=X,
                                                                                        padx=2)
        ttk.Button(btn_mgmt, text="STOP", bootstyle=DANGER, command=self.stop).pack(side=LEFT, expand=True, fill=X,
                                                                                    padx=2)

        # --- SETTINGS / ADJUSTMENTS ---
        # Active Duration
        ttk.Label(container, text="Active Duration (sec):").pack(pady=(10, 0))
        self.lbl_hard = ttk.Label(container, text=self.hard, font=("Helvetica", 12, "bold"))
        self.lbl_hard.pack()

        frame_h = ttk.Frame(container)
        frame_h.pack(fill=X)
        ttk.Button(frame_h, text="+", command=lambda: self.update_val('hard', 1)).pack(side=LEFT, 
                                                                                       expand=True, 
                                                                                       fill=X,
                                                                                       padx=5)
        ttk.Button(frame_h, text="-", command=lambda: self.update_val('hard', -1)).pack(side=RIGHT, 
                                                                                        expand=True, 
                                                                                        fill=X,
                                                                                        padx=5)

        # Break Duration
        ttk.Label(container, text="Break Duration (sec):").pack(pady=(10, 0))
        self.lbl_soft = ttk.Label(container, text=self.soft, font=("Helvetica", 12, "bold"))
        self.lbl_soft.pack()

        frame_s = ttk.Frame(container)
        frame_s.pack(fill=X)
        ttk.Button(frame_s, text="+", command=lambda: self.update_val('soft', 1)).pack(side=LEFT, 
                                                                                       expand=True, 
                                                                                       fill=X,
                                                                                       padx=5)
        ttk.Button(frame_s, text="-", command=lambda: self.update_val('soft', -1)).pack(side=RIGHT, 
                                                                                        expand=True, 
                                                                                        fill=X,
                                                                                        padx=5)

        # Rounds
        ttk.Label(container, text="Rounds:").pack(pady=(10, 0))
        self.lbl_steps = ttk.Label(container, text=self.steps, font=("Helvetica", 12, "bold"))
        self.lbl_steps.pack()

        frame_r = ttk.Frame(container)
        frame_r.pack(fill=X)
        ttk.Button(frame_r, text="+", command=lambda: self.update_val('steps', 1)).pack(side=LEFT, 
                                                                                        expand=True, 
                                                                                        fill=X,
                                                                                        padx=5)
        ttk.Button(frame_r, text="-", command=lambda: self.update_val('steps', -1)).pack(side=RIGHT, 
                                                                                         expand=True,
                                                                                         fill=X, 
                                                                                         padx=5)

        # --- CONFIGURATION ---
        ttk.Separator(container, orient=HORIZONTAL).pack(fill=X, pady=15)
        frame_cfg = ttk.Frame(container)
        frame_cfg.pack(fill=X)
        ttk.Button(frame_cfg, text="Delete Config", bootstyle=OUTLINE, command=self.delete).pack(side=LEFT, expand=True,
                                                                                                 fill=X, padx=5)
        ttk.Button(frame_cfg, text="Save Config", bootstyle=SUCCESS, command=self.save_to_file).pack(side=RIGHT,
                                                                                                     expand=True,
                                                                                                     fill=X, padx=5)

    def update_val(self, var_name, delta):
        """Update interval settings and refresh the screen labels."""
        if var_name == 'hard':
            self.hard = max(1, self.hard + delta)
            self.lbl_hard.config(text=str(self.hard))
        elif var_name == 'soft':
            self.soft = max(1, self.soft + delta)
            self.lbl_soft.config(text=str(self.soft))
        elif var_name == 'steps':
            self.steps = max(1, self.steps + delta)
            self.lbl_steps.config(text=str(self.steps))
            self.lbl_round_info.config(text=f"Round: 0 / {self.steps}")

    def start(self):
        """Reset and start the Tabata sequence."""
        if not self.is_running:
            self.is_running = True
            self.current_time = self.hard
            self.mode = "HARD"
            self.current_step = 1
            self.play_beep('start_sound.wav')
            self.countdown()

    def countdown(self):
        """Main timer loop that updates the UI every 1000ms."""
        if not self.is_running:
            return

        # Update visual countdown and colors
        ui_style = SUCCESS if self.mode == "HARD" else DANGER
        self.lbl_status.config(text=self.mode, bootstyle=ui_style)
        self.lbl_big_timer.config(text=str(self.current_time), bootstyle=ui_style)
        self.lbl_round_info.config(text=f"Round: {self.current_step} / {self.steps}")

        if self.current_time > 0:
            self.current_time -= 1
            self.timer_id = self.root.after(1000, self.countdown)
        else:
            self.switch_mode()

    def switch_mode(self):
        """Handle transition between Work and Rest phases."""
        if self.mode == "HARD":
            self.mode = "SOFT"
            self.current_time = self.soft
            self.play_beep('end_bell.wav')
        else:
            self.mode = "HARD"
            self.current_time = self.hard
            self.current_step += 1
            self.play_beep('start_sound.wav')

        if self.current_step <= self.steps:
            self.countdown()
        else:
            self.is_running = False
            self.lbl_status.config(text="FINISHED", bootstyle=INFO)
            self.play_beep('end_cycle.flac')

    def pause(self):
        """Halt the timer and play a notification sound."""
        self.is_running = False
        if self.timer_id:
            self.root.after_cancel(self.timer_id)
        self.lbl_status.config(text="PAUSED", bootstyle=WARNING)
        self.play_beep('short_soft.wav')

    def restart(self):
        """Resume the timer from the current state."""
        if not self.is_running:
            self.is_running = True
            self.countdown()

    def stop(self):
        """Stop the timer and close the application after a short delay."""
        if self.timer_id:
            self.root.after_cancel(self.timer_id)
        self.is_running = False
        print("Stopping app...")
        self.play_beep('short_soft.wav')
        self.root.after(2000, self.root.destroy)

    def play_beep(self, sound_name):
        """Locate and play audio files from the assets folder."""
        base_path = os.path.dirname(__file__)
        path = os.path.join(base_path, "assets", sound_name)

        print(f"DEBUG: Intentando tocar sonido en: {path}")  # <--- Línea de diagnóstico

        if os.path.exists(path):
            try:
                self.player.load_file(path)
                self.player.play()
            except Exception as e:
                print(f"Error al reproducir {sound_name}: {e}")
        else:
            print(f"ADVERTENCIA: El archivo no existe en {path}")

    def save_to_file(self):
        """Write current session settings to configuration.txt."""
        try:
            path = os.path.join(os.path.dirname(__file__), "configuration.txt")
            with open(path, "w", encoding='utf-8') as f:
                f.write(f"{self.soft}\n{self.hard}\n{self.steps}")
            print("Settings saved successfully.")
        except Exception as e:
            print(f"Error saving config: {e}")

    def delete(self):
        """Remove the configuration file from the system."""
        try:
            os.remove(os.path.join(os.path.dirname(__file__), "configuration.txt"))
            print("Config file deleted.")
        except FileNotFoundError:
            pass


def main_func():
    """This function call to  'my-tabata'"""
    app_root = ttk.Window(themename="superhero")
    # Pass values by defect
    tabata_app = Application(app_root, SOFT_DEFAULT, HARD_DEFAULT, STEPS_DEFAULT)
    app_root.mainloop()

if __name__ == "__main__":
    # let run like 'python -m my_tabata.app'
    main_func()